class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0

        balloon_hash = {"b": 1, "a": 1, "l":2, "o": 2, "n": 1}

        text_hash = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}

        for letter in text:
            text_hash[letter] += 1

        instance_count = float("inf")
        for key in balloon_hash:
            instance_count = min(instance_count, text_hash[key]//balloon_hash[key])

        return instance_count


# Test Cases

s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoonballoo"))
print(s.maxNumberOfBalloons("nlaebolko"))