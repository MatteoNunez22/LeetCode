class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        order = {}
        for i in range(len(source)):
            if source[i] in order:
                order[source[i]].append(i)
            else:
                order[source[i]] = [i]
            
        def getNextIndex(array, value):
            for num in array:
                if num > value:
                    return num
            else:
                return -1
          
        idx = -1
        count = 1
        for j in range(len(target)):
            if target[j] not in source:
                return -1
            nextIdx = getNextIndex(order[target[j]], idx)
            if not nextIdx == -1:
                idx = nextIdx
            else:
                count += 1
                idx = order[target[j]][0]
            
        return count
            
            
            