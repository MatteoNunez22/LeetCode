class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        reqMap = collections.defaultdict(list)
        
        for a, b in prerequisites:
            reqMap[a].append(b)
            
        visitSet = set()
            
        def complete(course):
            if course in visitSet:
                return False
            
            if not reqMap[course]:
                return True
            
            visitSet.add(course)
            for i, pre in enumerate(reqMap[course]):
                if not complete(pre):
                    return False
                    
            visitSet.remove(course)
            reqMap[course] = []
                    
            return True
        
        for i in range(numCourses):
            if not complete(i):
                return False
        
        return True