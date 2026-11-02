"""
Name: YOUR NAME HERE
Date last updated: November 1, 2026
Description: Draws a Koch snowflake fractal using Python's turtle graphics.
    Each edge of the snowflake is drawn with a "curve" method, implemented
    two ways: recursively (draw_curve_recursive) and non-recursively with a
    stack of turtle commands (draw_curve_stack). compare_snowflake() measures
    the time and memory used by each approach.
"""

import turtle
import time 
from memory_profiler import memory_usage

class KochSnowflake:
    def __init__(self, init_length=500, init_depth=3):
        """ Store the length of the starting triangle's edges and the
            number of recursive layers (depth) to draw """
        # Initialize the turtle
        self.t = None  

        # Length of one edge at 0 depth
        self.init_length = init_length  
        # Number of "layers" to draw
        self.init_depth = init_depth    
    

    def init_turtle(self):
        """ Initialize the turtle and move it to the 
            appropriate location on the screen """
        
        t = turtle.Turtle() # Initialize the turtle
        t.speed(8) # Increase the turtle's speed
        # Move the turtle to the upper left corner
        t.teleport(-200, -200)
        self.t = t


    ######################
    # Draw curve methods #
    ######################

    def draw_curve_recursive(self):
        """ The 'entry point' into the recursive curve method """
        self.draw_curve_recursive_helper(self.init_length, self.init_depth)


    def draw_curve_recursive_helper(self, length, depth):
        """ Recursively draw one side of the Koch snowflake.

            Parameters:
                length: the length of this side if it were a straight line
                depth: the number of layers of bumps still to add; at
                       depth 0 the side is just a straight line

            At depth > 0 the side is replaced by four curves, each one third
            as long and one depth shallower, joined by turns that form an
            outward-pointing equilateral triangle in the middle. """

        # Raise an error if depth is negative
        if depth < 0:
            raise ValueError("Depth cannot be negative")

        # Base case
        elif depth == 0:
            self.t.forward(length)

        # Recursive case
        else:
            third = length / 3

            self.draw_curve_recursive_helper(third, depth - 1)
            self.t.right(60)   # turn outward to start the bump
            self.draw_curve_recursive_helper(third, depth - 1)
            self.t.left(120)   # turn back inward to finish the bump
            self.draw_curve_recursive_helper(third, depth - 1)
            self.t.right(60)   # realign with the original direction
            self.draw_curve_recursive_helper(third, depth - 1)


    def draw_curve_stack(self):
        """ Draw one side of the Koch snowflake without recursion.

            A stack holds the turtle's pending commands, which are tuples:
                ("add_curve", length, depth): draw a curve of this size
                ("turn_left", angle): turn the turtle left by angle degrees
                ("turn_right", angle): turn the turtle right by angle degrees
            Because a stack is last-in, first-out, the commands for one
            expansion are pushed in reverse order so that they are popped
            (and so executed) in the correct order. """

        commands = [("add_curve", self.init_length, self.init_depth)]

        while commands:
            command = commands.pop()
            name = command[0]

            if name == "turn_left":
                self.t.left(command[1])

            elif name == "turn_right":
                self.t.right(command[1])

            elif name == "add_curve":
                length, depth = command[1], command[2]

                if depth < 0:
                    raise ValueError("Depth cannot be negative")

                # Base case: draw a straight line
                elif depth == 0:
                    self.t.forward(length)

                # Expand the curve into four smaller curves and three turns.
                # Pushed in reverse so they are executed in this order:
                #   curve, right 60, curve, left 120, curve, right 60, curve
                else:
                    third = length / 3
                    commands.append(("add_curve", third, depth - 1))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", third, depth - 1))
                    commands.append(("turn_left", 120))
                    commands.append(("add_curve", third, depth - 1))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", third, depth - 1))


    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self):
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_recursive()
            self.t.left(120)
            
        turtle.clearscreen()


    def draw_snowflake_stack(self):
        """ Draw the three edges of the Koch snowflake using the 
            non-recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_stack()
            self.t.left(120)

        turtle.clearscreen()


    #########################@#
    # Compare the approaches! #
    ##########################@

    def compare_snowflake(self):
        """ Compare how much time and memory the recursive and non-recursive 
            implementations of drawing the Koch Snowflake used """
        
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # End the timer
        time_end = time.perf_counter()

        # Find the total time taken
        time_taken = time_end - time_start 
        # Find the total memory used
        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used


if __name__ == "__main__":
    s = KochSnowflake(500, 3)
    s.draw_snowflake_stack()
    # s.draw_snowflake_recursive()
    # s.compare_snowflake()

