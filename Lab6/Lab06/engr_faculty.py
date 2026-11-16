"""
Author: Gurjot Kahlon
Last updated: November 16, 2026
Description: Bulds the root school roster, and reads the faculty list from the excel file 
into a dictionary last name, first name to proffessor object in a tree. 

"""

import pandas as pd

from professor import Professor
from faculty_visualizer import FacultyVisualizer
from tree_node import TreeNode
from preferences import Preferences

class ENGR_Faculty:
    def __init__(self):
        
        # Dictionary containing the faculty nodes
        # Keys are last names, values are Professors
        self.faculty_dict = self.import_faculty()

        # Tree representing the Engineering faculty
        self.program_structure = self.build_structure()

        # Visualize the faculty tree
        self.visualizer = FacultyVisualizer(
            self.program_structure, self.faculty_dict)

        
    def import_faculty(self):
        """ Reads the Excel file containing the faculty member information
            and adds them to the faculty dictionary """
        
        # The dictionary to store the faculty
        faculty_dict = {}

        # Read the Excel file into a pandas data frame
        df = pd.read_excel(Preferences.FACULTY_FILE)

        # Add each row of the data frame (professor) to the dictionary
        df.apply((lambda x: self.add_prof(x, faculty_dict)), axis=1)

        return faculty_dict


    def add_prof(self, prof, faculty_dict) -> None:
        """ Creates a Professor from one row of the faculty spreadsheet
            and stores it in faculty_dict, keyed by last name. """
        professor = Professor(prof["FirstName"], prof["LastName"],
                              prof["Rank"], prof["Program"], prof["Office"])
        faculty_dict[professor.last_name] = professor


    def build_structure(self) -> TreeNode:
        """ Builds and returns the faculty tree: the School of Engineering
            root, one child node per program, and each professor as a child
            of their program. Faculty nodes store the Professor as data. """

        # We are all under the School of Engineering
        root = TreeNode("School of Engineering", TreeNode.NodeType.SCHOOL)
        
        # Create a node for each SoE program
        # Map each Program to its TreeNode so faculty can be attached quickly
        program_nodes = {}
        for program in Professor.Program:
            node = TreeNode(program.value, TreeNode.NodeType.PROGAM)
            root.add_child(node)
            program_nodes[program] = node

        # Add each professor under the node for their program
        for prof in self.faculty_dict.values():
            prof_node = TreeNode(prof.last_name, TreeNode.NodeType.FACULTY,
                                 data=prof)
            program_nodes[prof.program].add_child(prof_node)

        return root


    def visualize_faculty(self):
        """ Build and show the tree visualizing the faculty """
        self.visualizer.run()
        

if __name__ == '__main__':
    f = ENGR_Faculty()
    f.visualize_faculty()