class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(s) < len(target):
            return 0

        s_hash = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}
        for letter in s:
            s_hash[letter] += 1

        target_hash = {}
        for letter in target:
            if letter not in target_hash:
                target_hash[letter] = 0
            target_hash[letter] += 1

        # print(s_hash)
        # print(target_hash)
        copies_count = float("inf")
        for key in target_hash:
            copies_count = min(copies_count, s_hash[key]//target_hash[key])
        
        return copies_count


# Test Cases

s = Solution()
print(s.rearrangeCharacters("loonbalxballpoonballoo", "balloon"))
print(s.rearrangeCharacters("nlaebolko", "balloon"))