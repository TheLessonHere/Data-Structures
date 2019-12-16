import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Increase the size counter by 1
        self.size += 1
        # Add item to the tail
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size < 1:
            return None
        # Decrease the size of the queue by 1
        self.size -= 1
        # Call method to remove item from the head
        return self.storage.remove_from_head()

    def len(self):
        return int(self.size)
