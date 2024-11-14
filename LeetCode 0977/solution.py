class Solution:
    def sortedSquares(self, nums):
        squares = []
        i = 0
        j = len(nums)-1
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                squares.append(nums[j]**2)
                j -= 1
            else:
                squares.append(nums[i]**2)
                i += 1
        
        squares.reverse()

        return squares

# Test Cases

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))