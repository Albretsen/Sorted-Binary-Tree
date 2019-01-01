# What is a binary tree?
# In computer science, a binary tree is a tree data structure in which each node has at most two children, which are
# referred to as the left child and the right child. A sorted binary tree (which this is) will add lower or equal
# values to the left node, and higher values to the right node. If the top node is 4, and we want to add a node with
# the value 8, we place this node to the top nodes right. If the top node already had a right node, we compare the
# value of 8 to the top nodes right node.

# To add a node, create an instance of the Tree class, and run the add_node function on it.
# It only requires on argument, which is an instance of a node class. ( tree = Tree(Node()) )
# Nodes require one value to be instantiated. ( Node(3) or Node(734) etc )

# Use the traverse algorithm on the trees rootnode to print out every number in the tree from
# smallest to highest.

# Example at bottom of page

# Import only used for assigning random values to node! It is not necessary for this algorithm to work.
import random


class Tree:
    rootNode = None

    def __init__(self, node):
        self.rootNode = node

    # Adds a node to the correct position in the tree
    def add_node(self, node):
        if node.value <= self.rootNode.value:
            if self.rootNode.leftNode is None:
                self.rootNode.leftNode = node
            else:
                self.rootNode.leftNode.add_node(node)
        else:
            if self.rootNode.rightNode is None:
                self.rootNode.rightNode = node
            else:
                self.rootNode.rightNode.add_node(node)


class Node:

    value = 0
    leftNode = None
    rightNode = None

    def __init__(self, value):
        self.value = value

    # Adds node as neighbor or runs the function on neighbor according to new nodes value
    def add_node(self, node):
        if node.value <= self.value:
            if self.leftNode is None:
                self.leftNode = node
            else:
                self.leftNode.add_node(node)
        else:
            if self.rightNode is None:
                self.rightNode = node
            else:
                self.rightNode.add_node(node)

    # Recursive algorithms that prints every number from bottom left node to bottom right node.
    # It works like this:
    # Checks if this nodes left node exists
    # If it exists, run the function on that node
    # That node checks if it has a left node
    # If it doesn't, it will print out it's value
    # It will then check for a right node. If right node exists, run function on that node.
    # If not, the recursion will "jump a step back" and continue where it left of, which means it will print the value
    # at whatever node it left of from.
    def traverse(self):
        if self.leftNode is not None:
            self.leftNode.traverse()
        print(self.value)
        if self.rightNode is not None:
            self.rightNode.traverse()


# EXAMPLE
# Creates a tree with a root node
tree = Tree(Node(random.randint(0, 10)))
# Adds 10 random nodes to the tree
for i in range(10):
    tree.add_node(Node(random.randint(0, 10)))

# Prints out every number in the tree from lowest to highest
tree.rootNode.traverse()
