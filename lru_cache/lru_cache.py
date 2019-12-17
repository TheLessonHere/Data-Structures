from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Max # of nodes
        self.limit = limit
        # Current # of nodes
        self.size = 0
        # DLL that holds the key-value entries
        self.list = DoublyLinkedList()
        # Storage dictionary
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Return None if the list has no elements
        if not self.list.head and not self.list.tail:
            return None
        # Check if the key is in the list
        # Start at the head of the list
        current_key = self.list.head
        in_list = False
        # If we find the matching key, return in_list == true, otherwise go to the next item
        while current_key and in_list == False:
            if current_key.value == key:
                in_list = True
            else:
                current_key = current_key.next
        # If the key is in the list, move it to most recently used and return the value from storage
        if in_list:
            self.list.move_to_front(current_key)

            for i in self.storage:
                if i == key:
                    return self.storage[i]
        # Otherwise, return None
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Check if the given key is in the list
        key_in_list = self.get(key)
        # If it is, overwrite the value if necessary
        if key_in_list:
            for i in self.storage:
                if i == key:
                    self.storage[i] = value
        # If it isn't...
        if key_in_list == None:
            # Check if the cache is at its limit
            if self.size == self.limit:
                # If it is, remove the item from the tail of the list
                tail = self.list.remove_from_tail()
                print(tail)
                # And remove the item from our cache storage
                self.storage.pop(tail)
            # Then, add the new key to the head of the list or MRU
            self.list.add_to_head(key)
            # Update cache storage with the new key value pair
            self.storage.update({key: value})
            # Update the cache size
            self.size = self.list.length
