"""
Author: Your Name Here
Last Updated: [DATE]
Stores all the data representing the state of the "Antarctic Survival" game,
including the board (a 2D grid of Cells), and the current positions of the
player, food, and enemies. Provides methods to query neighboring cells and
to update the game state as the player moves, food is added/eaten, and
enemies are added/moved.
"""

import random

from cell import Cell
from preferences import Preferences

class GameData:
    def __init__(self):
        # The current state of the board
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)] 
                                      for row in range(Preferences.NUM_ROWS)]
        
        # Whether or not the game is over
        self.gameover = False

        # The current cell containing the player
        self.player = self.board[0][0]    # Start at the top left
        self.player.become_player()

        # The number of empty cells on the board, accounting for the player cell
        self.num_empty_cells = Preferences.NUM_CELLS - 1

        # A list of cells containing food
        self.food = []
        # Number of food eaten
        self.score = 0

        # A list of cells containing enemies
        self.enemies = []


    #######################
    # Game Limits Methods #
    #######################

    def at_max_food(self) -> bool:
        """ Check whether we can add more food """
        return len(self.food) / self.num_empty_cells > Preferences.MAX_FOOD
    
    def at_max_enemies(self) -> bool:
        """ Check whether we can add more enemies """
        return len(self.enemies) / self.num_empty_cells > Preferences.MAX_ENEMIES

    def set_game_over(self) -> None:
        """ Turn on the game over flag """
        self.gameover = True


    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_west_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the left of the given cell. 
            If we are at the  edge of the map, return None. """
        row, col = cell.get_row(), cell.get_col()
        # Column 0 is the leftmost column, so there's no cell to the west
        if col == 0:
            return None
        return self.board[row][col - 1]
        
    def get_east_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the right of the given cell.
            If we are at the edge of the map, return None. """
        row, col = cell.get_row(), cell.get_col()
        # The last column has no cell to the east
        if col == Preferences.NUM_COLS - 1:
            return None
        return self.board[row][col + 1]
    
    def get_north_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately above the given cell.
            If we are at the edge of the map, return None. """
        row, col = cell.get_row(), cell.get_col()
        # Row 0 is the top row, so there's no cell to the north
        if row == 0:
            return None
        return self.board[row - 1][col]
        
    def get_south_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately below the given cell.
            If we are at the edge of the map, return None. """
        row, col = cell.get_row(), cell.get_col()
        # The last row has no cell to the south
        if row == Preferences.NUM_ROWS - 1:
            return None
        return self.board[row + 1][col]


    ###########################
    # Player Movement Methods #
    ###########################
        
    def move_player_right(self) -> None:
        """ Move the player one cell to the right if it is empty """
        neighbor = self.get_east_neighbor(self.player)
        # Only move if there is a valid cell in that direction
        if neighbor is not None:
            self.move_player_to_cell(neighbor)

    def move_player_left(self) -> None:
        """ Move the player one cell to the left if it is empty """
        neighbor = self.get_west_neighbor(self.player)
        if neighbor is not None:
            self.move_player_to_cell(neighbor)

    def move_player_up(self) -> None:
        """ Move the player one cell up if it is empty """
        neighbor = self.get_north_neighbor(self.player)
        if neighbor is not None:
            self.move_player_to_cell(neighbor)

    def move_player_down(self) -> None:
        """ Move the player one cell down if it is empty """
        neighbor = self.get_south_neighbor(self.player)
        if neighbor is not None:
            self.move_player_to_cell(neighbor)

    def move_player_to_cell(self, cell: Cell) -> None:
        """ Move the player to the given cell """

        # If there is food in this cell, eat it
        if cell.is_food():
            self.eat_food(cell)
            self.update_player_cell(cell)
        # If there is an enemy in this cell, game over!
        elif cell.is_enemy():
            self.player.become_empty()
            self.set_game_over()
        # Otherwise, update the player location
        else:
            self.update_player_cell(cell)

    def update_player_cell(self, new_cell: Cell) -> None:
        """ Move the player to the new cell """
    
        # Empty the cell the player just moved away from
        self.player.become_empty()
        # Update the player to the new cell
        self.player = new_cell
        # Change the new cell to be the player type
        self.player.become_player()


    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
        """ Adds food to a random open spot on the board """

        # Find a row on the board
        row = random.randrange(0, Preferences.NUM_ROWS)
        # Find a col on the board
        col = random.randrange(0, Preferences.NUM_COLS)

        cell = self.board[row][col]
        # Only place food on a cell that's currently empty
        if cell.is_empty():
            cell.become_food()
            self.food.append(cell)
            # This cell is no longer empty, so update the count
            self.num_empty_cells -= 1

    def eat_food(self, cell: Cell) -> None:
        """ Behavior for when the player eats food """
        # The food is gone once eaten
        self.food.remove(cell)
        # Increase the player's score
        self.score += 1
        # The player's old cell will become empty (handled right after this
        # call, in update_player_cell), while this cell simply changes from
        # one occupied type (food) to another (player) - net one more
        # empty cell on the board.
        self.num_empty_cells += 1


    ##########################
    # Enemy Movement Methods #
    ##########################

    def add_enemy(self) -> None:
        """ Adds an enemy to the bottom right corner of the board """
        cell = self.board[Preferences.NUM_ROWS - 1][Preferences.NUM_COLS - 1]

        if cell.is_empty():
            # Nothing there - just place the enemy
            cell.become_enemy()
            self.enemies.append(cell)
            self.num_empty_cells -= 1
        elif cell.is_food():
            # The enemy takes over the food's spot; the food is destroyed
            self.food.remove(cell)
            cell.become_enemy()
            self.enemies.append(cell)
            # This cell was already non-empty (food), and stays non-empty
            # (enemy), so num_empty_cells does not change
        elif cell.is_player():
            # A seal appeared right where the player is standing - game over!
            self.set_game_over()
        elif cell.is_enemy():
            # There's already an enemy here; don't stack a second one
            pass

    def move_enemy_to_cell(self, enemy_cell: Cell, 
                           cell: Cell, idx: int) -> None:
        """ Moves the enemy cell to a new location.
            idx refpresents the index of that enemy in
             the enemies list. """
        if cell.is_player():
            # The enemy caught the player - game over!
            self.set_game_over()
        elif cell.is_food():
            # The enemy moves onto the food, destroying it
            self.food.remove(cell)
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell
        elif cell.is_enemy():
            # Blocked by another enemy - stay in place
            pass
        else:
            # The destination is empty - move the enemy there
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell

    def move_enemy_left(self, idx: int) -> None:
        """ Move the enemy at index idx left one cell """
        enemy_cell = self.enemies[idx]
        neighbor = self.get_west_neighbor(enemy_cell)
        if neighbor is not None:
            self.move_enemy_to_cell(enemy_cell, neighbor, idx)

    def move_enemy_right(self, idx: int) -> None:
        """ Move the enemy at index idx right one cell """
        enemy_cell = self.enemies[idx]
        neighbor = self.get_east_neighbor(enemy_cell)
        if neighbor is not None:
            self.move_enemy_to_cell(enemy_cell, neighbor, idx)

    def move_enemy_up(self, idx: int) -> None:
        """ Move the enemy at index idx up one cell """
        enemy_cell = self.enemies[idx]
        neighbor = self.get_north_neighbor(enemy_cell)
        if neighbor is not None:
            self.move_enemy_to_cell(enemy_cell, neighbor, idx)

    def move_enemy_down(self, idx: int) -> None:
        """ Move the enemy at index idx down one cell """
        enemy_cell = self.enemies[idx]
        neighbor = self.get_south_neighbor(enemy_cell)
        if neighbor is not None:
            self.move_enemy_to_cell(enemy_cell, neighbor, idx)



if __name__ == "__main__":
    gd = GameData()
    # You can modify the line below for testing!
    print(gd.get_west_neighbor(gd.player))