class Solution:
    def summaryRanges(self, nums):
        sorted_list = []

        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]

        left_integer = nums[0]
        right_integer = nums[0]
        
        for i in range(1, len(nums)):

            if nums[i-1]+1 == nums[i]:
                right_integer = nums[i]
                continue

            if left_integer == right_integer:
                sub_range = str(left_integer)
            else:
                sub_range = str(left_integer) + "->" + str(right_integer)

            sorted_list.append(sub_range)

            left_integer = nums[i]
            right_integer = nums[i]
        
        if left_integer == right_integer:
            sub_range = str(left_integer)
        else:
            sub_range = str(left_integer) + "->" + str(right_integer)

        sorted_list.append(sub_range)

        return sorted_list
        

# Test Cases

s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))
print(s.summaryRanges([0,1,2,4,5,7]))