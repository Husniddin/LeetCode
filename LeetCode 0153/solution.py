class Solution:
    def findMin(self, nums):
        
        i = 0
        j = len(nums) - 1
        nums_min = nums[0]
        while i <= j:
            middle = (i + j)//2
            if nums[middle] < nums_min:
                nums_min = nums[middle]
                j = middle - 1
            else:
                i = middle + 1
        
        return nums_min
# Test Cases

s = Solution()
print(s.findMin([4,5,6,7,8,9,1,2,3]))