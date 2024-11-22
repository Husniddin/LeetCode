class Solution:
    def searchMatrix(self, matrix, target):
        m_target = None
        i = 0
        j = len(matrix) - 1
        while i <= j:
            middle = (i+j)//2

            if matrix[middle][0] <= target and target <= matrix[middle][-1]:
                m_target = matrix[middle]
                break
            elif matrix[middle][-1] < target:
                i = middle + 1
            else:
                j = middle - 1
        
        if m_target is None:
            return False
        
        i = 0
        j = len(m_target) - 1
        while i <= j:
            middle = (i+j)//2
            if m_target[middle] == target:
                return True
            elif m_target[middle] < target:
                i = middle + 1
            else:
                j = middle - 1
        
        return False

# Test Cases

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))