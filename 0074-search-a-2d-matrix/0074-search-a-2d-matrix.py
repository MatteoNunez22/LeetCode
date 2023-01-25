class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # l, r = 0, m * n - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     mid_row, mid_col = mid // n, mid % n
        #     if target < matrix[mid_row][mid_col]:
        #         r = mid - 1
        #     elif target > matrix[mid_row][mid_col]:
        #         l = mid + 1
        #     else:
        #         return True
        # return False
        
        m, n = len(matrix), len(matrix[0])
        
        l_row, r_row = 0, m - 1
        while l_row <= r_row:
            mid_row = l_row + (r_row - l_row) // 2
            if target < matrix[mid_row][0]:
                r_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                l_row = mid_row + 1
            else:
                break
        
        if l_row > r_row:
            return False
        
        l_col, r_col = 0, n - 1
        while l_col <= r_col:
            mid_col = l_col + (r_col - l_col) // 2
            if target < matrix[mid_row][mid_col]:
                r_col = mid_col - 1
            elif target > matrix[mid_row][mid_col]:
                l_col = mid_col + 1
            else:
                return True
        
        return False