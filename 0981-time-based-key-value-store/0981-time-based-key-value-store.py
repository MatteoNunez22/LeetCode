class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        self.timeMap[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        
        values = self.timeMap[key]
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            midStamp = values[mid][0]
            if midStamp <= timestamp:
                res = values[mid][-1]
                l = mid + 1
            else:
                r = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)