class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        res = []

        el_1 = 1
        qty_1 = 0

        el_2 = 2
        qty_2 = 0

        for num in nums:
            if el_1 == num:
                qty_1 += 1
            elif el_2 == num:
                qty_2 += 1
            elif qty_1 == 0:
                el_1 = num
                qty_1 = 1
            elif qty_2 == 0:
                el_2 = num
                qty_2 = 1
            else:
                qty_1 -= 1
                qty_2 -= 1

        qty_1, qty_2 = 0, 0

        for num in nums:
            if el_1 == num:
                qty_1 += 1
            if el_2 == num:
                qty_2 += 1

        if qty_1 > n/3:
            res.append(el_1)
        if qty_2 > n/3:
            res.append(el_2)
        
        return res
# Test Cases

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,2,3,4,5,6,7,8,9]))