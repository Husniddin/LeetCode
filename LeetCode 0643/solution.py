class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        i = 0
        j = 0
        max_sub_arr = float("-inf")
        sum_arr = 0
        while j < n:
            sum_arr += nums[j]

            if (j - i + 1) == k:
                max_sub_arr = max(max_sub_arr, sum_arr)
                sum_arr -= nums[i]
                i += 1

            j += 1

        return max_sub_arr/k

# Test Cases

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([1,12], 2))