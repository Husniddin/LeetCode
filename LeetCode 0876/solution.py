class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_hash = {}

        for jewel in jewels:
            jewels_hash[jewel] = 1
        
        jewels_count = 0

        for stone in stones:
            if stone in jewels_hash:
                jewels_count += 1

        return jewels_count

# Test Cases

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones(["z", "ZZ"]))