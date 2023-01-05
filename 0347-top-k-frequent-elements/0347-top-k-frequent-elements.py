class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
           
        print(count)
        maxheap = []
        heapq.heapify(maxheap)
        for n, c in count.items():
            heapq.heappush(maxheap, (-c,n))
            
        answer = []
        for i in range(k):
            pop = heapq.heappop(maxheap)
            print(pop)
            answer.append(pop[1])
        
        return answer
    
        