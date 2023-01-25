class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        l, r = 0, m * n - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            mid_row, mid_col = mid // n, mid % n
            if target < matrix[mid_row][mid_col]:
                r = mid - 1
            elif target > matrix[mid_row][mid_col]:
                l = mid + 1
            else:
                return True
            
        return False