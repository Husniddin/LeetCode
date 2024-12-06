class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x!=0 and x%10==0):
            return False

        original_x = x
        reversed_x = 0

        while x > 0:
            delta = x % 10
            reversed_x = reversed_x * 10 + delta
            x = x // 10

        return reversed_x == original_x

# Test Cases

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(151616516))
print(s.isPalindrome(15))