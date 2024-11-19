class Solution:
    def plusOne(self, digits):

        decimal = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                decimal = 1
            else:
                digits[i] += 1
                decimal = 0
                return digits
        
        if decimal:
            digits.insert(0, 1)

        return digits

# Test Cases

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([9]))