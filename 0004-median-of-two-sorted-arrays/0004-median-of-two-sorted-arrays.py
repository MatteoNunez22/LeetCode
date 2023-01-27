class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2  
        else:
            A, B = nums2, nums1
            
        total = len(A) + len(B)
        half = total // 2
            
        l, r = 0, len(A) - 1
        
        while True:
            midA = l + (r - l) // 2
            midB = half - midA - 2
            
            leftA = A[midA] if midA >= 0 else float("-infinity")
            leftB = B[midB] if midB >= 0 else float("-infinity")
            rightA = A[midA+1] if midA+1 < len(A) else float("infinity")
            rightB = B[midB+1] if midB+1 < len(B) else float("infinity")
            
            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1
                