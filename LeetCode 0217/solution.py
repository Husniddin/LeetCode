class Solution:
    def containsDuplicate(self, nums):
        nums_length = len(nums)

        if nums_length==1:
            return False

        nums_hash = {}
        i, j = 0, nums_length-1

        while i <= j:

            if i!=j and nums[i]==nums[j]:
                return True
            if nums[i] in nums_hash:
                return True
            if nums[j] in nums_hash:
                return True

            nums_hash[nums[i]] = 1
            nums_hash[nums[j]] = 1

            i += 1
            j -= 1

        return False

# Test Cases

s = Solution()
print(s.containsDuplicate([0,2,3,4,6,8,9]))
print(s.containsDuplicate([0,1,2,4,5,7]))