
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_length = len(ransomNote)
        magazine_length = len(magazine)

        if ransomNote_length > magazine_length:
            return False
        
        if ransomNote_length==1 and magazine_length==1:
            if ransomNote[0]==magazine[0]:
                return True
            else:
                return False
        
        ransomNote_hash = {chr(i):0 for i in range(ord("a"), ord("z")+1)}
        magazine_hash = {chr(i):0 for i in range(ord("a"), ord("z")+1)}

        for letter in ransomNote:
            ransomNote_hash[letter] += 1

        for letter in magazine:
            magazine_hash[letter] += 1

        for letter in ransomNote_hash:
            if ransomNote_hash[letter] == 0:
                continue
            if ransomNote_hash[letter] > magazine_hash[letter]:
                return False

        return True

# Test Cases

s = Solution()
print(s.canConstruct("abcd", 'ahcbgdc'))
print(s.canConstruct("abcd", 'ahcbgdc'))
print(s.canConstruct("a", 'b'))
print(s.canConstruct("aa", 'ab'))
print(s.canConstruct("aa", 'aab'))