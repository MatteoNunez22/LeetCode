class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1       
        print(count)
        
        # Approach 1: O(klogN)
        # maxheap = []
        # heapq.heapify(maxheap)
        # for n, c in count.items():
        #     heapq.heappush(maxheap, (-c,n))
        # answer = []
        # for i in range(k):
        #     pop = heapq.heappop(maxheap)
        #     print(pop)
        #     answer.append(pop[1])
        # return answer
    
        # Approach 2: O(N)
        bucket = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            bucket[c].append(n)
        print(bucket)
        
        answer = []
        for n_list in bucket[::-1]:
            if n_list:
                for n in n_list:
                    answer.append(n)
                    if len(answer) == k:
                        return answer
        return answer
    
        