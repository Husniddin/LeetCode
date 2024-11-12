class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}
        t_hash = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}

        for letter in s:
            s_hash[letter] += 1
        for letter in t:
            t_hash[letter] += 1

        for key in s_hash:
            if s_hash[key] == 0:
                continue
            if s_hash[key] != t_hash[key]:
                return False
        return True
        

# Test Cases

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))