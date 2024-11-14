class Solution:
    def maxArea(self, height):
        max_area = 0
        height_length = len(height)
        i = 0
        j = height_length - 1
        while i < j:
            # additional
            if i > 0 and height[i] < height[i-1]:
                i += 1
                continue
            if j < height_length - 1 and height[j] < height[j+1]:
                j -= 1
                continue
            #end additional

            max_area = max(max_area, (j - i)*min(height[i], height[j]))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

# Test Cases

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))