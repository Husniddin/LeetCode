class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
        
        return s
        

# Test Cases

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))