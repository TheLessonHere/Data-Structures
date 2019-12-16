import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Increase the size counter by 1
        self.size += 1
        # Add item to the head
        self.storage.add_to_head(value)

    def pop(self):
        if self.size < 1:
            return None
        # Decrease the size of the queue by 1
        self.size -= 1
        # Call method to remove item from the head
        return self.storage.remove_from_head()

    def len(self):
        return int(self.size)
