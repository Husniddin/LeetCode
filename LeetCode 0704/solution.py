class Solution:
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1

        while i <= j:
            middle = (i + j) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                i = middle + 1
            else:
                j = middle - 1
        
        return -1

# Test Cases

s = Solution()
print(s.search([-1,0,3,5,9,12,13,14,15,16,17,18,19,20], 9))
print(s.search([-1,0,3,5,9,12,13,14,15,16,17,18,19,20], 21))