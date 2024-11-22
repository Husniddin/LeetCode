class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        j = num

        while i <= j:
            m = (i + j)//2
            m_square = m * m

            if m_square == num:
                return True
            elif m_square > num:
                j = m - 1
            else:
                i = m + 1
        
        return False

# Test Cases

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))