class Solution:
    def twoSum(self, nums, target):
        passed_nums = {}

        for i in range(0, len(nums)):

            y = target - nums[i]

            if y in passed_nums:
                return [passed_nums[y], i]
            
            passed_nums[nums[i]] = i

# Test Cases

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))