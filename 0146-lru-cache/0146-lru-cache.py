class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.map = {}
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.keys.remove(key)
            self.keys.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.keys.remove(key)
        elif len(self.keys) == self.capacity:
            self.map.pop(self.keys[0])
            self.keys.remove(self.keys[0])
        self.keys.append(key)
        self.map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)