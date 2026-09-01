from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move accessed item to the end (MRU)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and mark as MRU
            self.cache.move_to_end(key)
        self.cache[key] = value

        # Evict the first item (LRU) if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

"""
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #left- Least recent used
        #right- Most recent used
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    #normal delete
    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    #insert node at right()
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.nxt = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #remove key and insert in right(as most recently used)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #if node in cache remove it to inset at mru
        if key in self.cache:
            self.remove(self.node)
        #insert into hashmap
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #evict LRU key
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

"""


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)