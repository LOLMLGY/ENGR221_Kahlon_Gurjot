"""
Author: Gurjot Kahlon
Last updated: November 16, 2026
Description: Defines the root tree to build the tree. Every node has a name, type(school, program, or faculty)
some optional data, a pararnet and list of children along with support for removing or adding children, leaf checks, 
depth/height, and name searching.
"""

from enum import Enum


class TreeNode:
    def __init__(self, name, node_type, data=None):
        self.name = name
        self.node_type = node_type
        self.data = data
        self.parent = None
        self.children = []


    def add_child(self, child) -> None:
        """ Adds the given node as a child of this node and sets the
            child's parent attribute to this node. """
        self.children.append(child)
        child.parent = self


    def remove_child(self, child) -> None:
        """ Removes the given node from this node's children, if present,
            and clears the removed child's parent attribute. Does nothing
            if the node is not a child of this node. """
        if child in self.children:
            self.children.remove(child)
            child.parent = None


    def is_leaf(self) -> bool:
        """ Returns True if this node has no children, False otherwise. """
        return len(self.children) == 0


    def depth(self) -> int:
        """ Returns the depth of this node: the number of edges on the path
            from the root down to this node (the root has depth 0). """
        depth = 0
        current = self
        # Walk up the parent links until we reach the root
        while current.parent is not None:
            depth += 1
            current = current.parent
        return depth


    def height(self) -> int:
        """ Returns the height of this node: the number of edges on the
            longest path from this node down to a leaf (a leaf has
            height 0). """
        # Base case: a leaf has height 0
        if self.is_leaf():
            return 0
        # Recursive case: 1 + height of the tallest child subtree
        return 1 + max(child.height() for child in self.children)


    def find(self, name):
        """ Searches this node and its descendants (pre-order, depth-first)
            for a node with the given name. Returns the matching TreeNode,
            or None if no node has that name. """
        # Check this node first
        if self.name == name:
            return self
        # Otherwise search each child's subtree
        for child in self.children:
            result = child.find(name)
            if result is not None:
                return result
        return None


    def print_tree(self, indent=0):
        """ Prints the tree with indentation. """
        print("    " * indent + str(self))

        for child in self.children:
            child.print_tree(indent + 1)


    def __str__(self):
        """ A node is displayed as its name """
        return self.name
    

    class NodeType(Enum):
        SCHOOL = "School"
        PROGAM = "Program"
        FACULTY = "Faculty"

        @classmethod
        def init_from_str(cls, node_type):
            return cls[node_type.strip().upper()]

if __name__ == "__main__":
    root = TreeNode("Engineering", TreeNode.NodeType.SCHOOL)

    comp_e = TreeNode("CompE", TreeNode.NodeType.PROGAM)
    root.add_child(comp_e)

    ee = TreeNode("EE", TreeNode.NodeType.PROGAM)
    root.add_child(ee)

    kubota = TreeNode("Kubota", TreeNode.NodeType.FACULTY)
    comp_e.add_child(kubota)

    qin = TreeNode("Qin", TreeNode.NodeType.FACULTY)
    comp_e.add_child(qin)

    root.print_tree()