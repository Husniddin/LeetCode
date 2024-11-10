class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '' or (s == '' and t == ''):
            return True

        if t == '':
            return False

        j = 0

        for letter in t:
            if s[j] == letter:
                j += 1
            
            if j == len(s):
                return True
        
        return False

# Test Cases

s = Solution()
print(s.isSubsequence("abcd", 'ahcbgdc'))