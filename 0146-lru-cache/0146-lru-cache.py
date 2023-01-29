class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def append(self, node):
        self.end.prev.next = node
        node.prev = self.end.prev
        self.end.prev = node
        node.next = self.end
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.append(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.append(self.map[key])
        
        if len(self.map) > self.capacity:
            self.map.pop(self.start.next.key)
            self.remove(self.start.next)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)