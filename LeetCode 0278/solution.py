# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion():
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n

        while i < j:
            middle = (i + j)//2

            if isBadVersion(middle):
                j = middle
            else:
                i = middle + 1
        
        return i

# Test Cases