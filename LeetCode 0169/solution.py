class Solution:
    def majorityElement(self, nums):
        major_element = nums[0]
        qty = 1

        for i in range(1, len(nums)):

            if major_element == nums[i]:
                qty += 1
            elif qty == 0:
                major_element = nums[i]
                qty = 1
            else:
                qty -= 1
        
        return major_element

# Test Cases

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))