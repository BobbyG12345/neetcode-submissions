class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # 1️⃣ 二分找行
        top, bottom = 0, m - 1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break  # target 在这一行
        
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        
        # 2️⃣ 在这一行二分查找
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False