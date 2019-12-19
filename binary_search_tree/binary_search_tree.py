import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Store value of the current tree node, this is going to change with each tree
        # node so we can't just use self
        current_tree = self
        # Declare higher scope variable to hold the value of the next tree node after
        # we check if the value is smaller or larger
        next_tree = None
        if current_tree.value >= value:
            # Sends it left if the value is smaller
            next_tree = current_tree.left
        else:
            # Sends it right if it's larger
            next_tree = current_tree.right
        # While there are still more trees...
        while next_tree is not None:
            # Perform a similar action to the initial one above
            # The value of the current tree is set to the next tree
            current_tree = next_tree
            # Then check if the value is smaller or larger than the new current tree
            if current_tree.value >= value:
                # Sends it left if the value is smaller
                next_tree = current_tree.left
            else:
                # Sends it right if it's larger
                next_tree = current_tree.right
                # Loop breaks once it has gone through every value and hits the right depth location

        # Create a new tree node out of the value using the class constructor
        new_tree = BinarySearchTree(value)
        # And then place it on the correct side of the current tree
        if current_tree.value >= value:
            current_tree.left = new_tree
        else:
            current_tree.right = new_tree

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if the value of the current tree node is equal to the target value
        if self.value == target:
            # If so, return true
            return True
        # If not, we go through a similar process as the while loop in the insert method
        # Store value of the current tree node so that we can mutate it
        current_tree = self
        # Declare higher scope variable to hold the value of the next tree after
        # we check if the value is smaller or larger
        next_tree = None
        if current_tree.value >= target:
            # Goes left if the value is smaller
            next_tree = current_tree.left
        else:
            # Goes right if it's larger
            next_tree = current_tree.right
        # While there are still more trees to check...
        while next_tree is not None:
            # The value of the current tree is set to the next tree
            current_tree = next_tree
            # We check if the new current tree value is equal to the target value
            if current_tree.value == target:
                # If it is return true
                return True
            # If not, go to the next tree node
            elif current_tree.value > target:
                next_tree = current_tree.left
            else:
                next_tree = current_tree.right
        # Loop breaks when it has checked every value, if it didn't exist it returns False
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Declare some higher scope variables to store/keep track of values for
        # 1: The max value
        # 2: The current/starting tree node that we're checking and
        # 3: The next tree node we have to check (always going to be to the right)
        current_max = self.value
        current_tree = self
        next_tree = self.right
        # While there are still tree nodes to check...
        while next_tree is not None:
            # Move to the next tree
            current_tree = next_tree
            # If that tree's value is greater than our current max value...
            if current_tree.value > current_max:
                # Set our current max to the new value
                current_max = current_tree.value
            # Continue to the next tree to the right
            next_tree = current_tree.right
        # Return our current max value once we hit the end of the tree
        return current_max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Call the callback function on the current/starting tree value
        cb(self.value)
        # Recursively iterate over each branch to the left and right,
        # calling the callback for each tree node value
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
