class Solution:
    def missingNumber(self, nums):
        i = 0
        j = len(nums) - 1
        while i <= j:
            if i not in nums:
                return i
            if j not in nums:
                return j
            i += 1
            j -= 1
        
        return len(nums)

# Test Cases

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))