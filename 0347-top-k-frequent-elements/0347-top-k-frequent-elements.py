class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        tuples = [(k,v) for k,v in count.items()]
        tuples.sort(key=lambda x: x[1])
        return [k for k,v in tuples][-k:]
        