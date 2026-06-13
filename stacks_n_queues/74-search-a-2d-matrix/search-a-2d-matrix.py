class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        low = 0
        high = (n * m) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map the 1D index back to 2D row and column
            mid_element = matrix[mid // m][mid % m]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
        
       