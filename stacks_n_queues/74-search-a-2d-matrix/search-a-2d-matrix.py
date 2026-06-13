class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # n is the number of rows (length of the outer list)
        n = len(matrix)
        
        # m is the number of columns (length of the first row)
        m = len(matrix[0]) if n > 0 else 0
        """

        l = 0
        r = n
        while l<=r:
            mid = (l+r)//2
            if matrix[0][mid] == target:
                return True
                break
            if matrix[0][l] < target < matrix[0][mid]:
                r = mid - 1
            elif matrix[0][mid] < target < matrix[0][r]:
                l = mid + 1
            if l == r:
                k = l
        l1 = 0
        r1 = m
        while l1 <= r1:
            mid1 = (l1+r1)//2
            if matrix[k][mid1] == target:
                return True
            elif matrix[k][mid1] > target:
                r1 = mid1 - 1
            else:
                l1 = mid1 + 1
        return False
    """
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False



