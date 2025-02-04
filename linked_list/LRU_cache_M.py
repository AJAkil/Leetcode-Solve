class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.l = Node(0, 0) # dummy left node
        self.r = Node(0, 0) # dummy right node
        self.l.next = self.r
        self.r.prev = self.l
    
    def insert(self, node):
        prev_node = self.r.prev
        next_node = self.r

        # fix the pointers now
        node.next = next_node
        node.prev = prev_node

        # fix pointers for the prev and next node
        prev_node.next = node
        next_node.prev = node
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key]) # remove from the linked list first
            self.insert(self.cache[key]) # add to the MRU, at the end just before the right pointed node

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # case: if key is in cache
        if key in self.cache:
            # remove from where it is in the doubly linked list
            self.remove(self.cache[key])

        # create a new node
        self.cache[key] = Node(key, value)
        # place it in MRU
        self.insert(self.cache[key])

        # eviction
        if len(self.cache) > self.cap:
            # evict the LRU node
            lru = self.l.next
            self.remove(lru) # remvoe it from the linked list
            del self.cache[lru.key]  # also delete it from the key as well.

        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)