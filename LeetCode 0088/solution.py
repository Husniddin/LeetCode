class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        j = m + n - 1

        while i2 > -1:
            if i1 > -1 and nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1

            j -= 1
        # return nums1

# Test Cases

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))
print(s.merge([2,0], 1, [1], 1))
print(s.merge([2,0,0,0,0,0,0], 1, [1, 1, 1, 1, 1, 1], 6))