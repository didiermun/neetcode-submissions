class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #dummies
        self.left = Node()
        self.right = Node()

        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

    def insert(self, node):
        node_prev = self.right.prev

        node.prev = node_prev
        node_prev.next = node

        self.right.prev = node
        node.next = self.right


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        found = self.cache[key]

        self.remove(found)
        self.insert(found)

        return found.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            found = self.cache[key]
            self.remove(found)

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
