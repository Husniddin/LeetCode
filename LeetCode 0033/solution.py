class Solution:
    def search(self, nums, target):

        min_item = self.findMin(nums)

        if min_item[1] <= target and target <= nums[-1]:
            i = min_item[0]
            j = len(nums) - 1
        else:
            i = 0
            j = min_item[0]

        while i <= j:
            middle = (i + j)//2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                i = middle + 1
            else:
                j = middle - 1
    
        return -1

    def findMin(self, nums):
        
        i = 0
        j = len(nums) - 1
        nums_min = nums[0]
        index = 0
        while i <= j:
            middle = (i + j)//2
            if nums[middle] < nums_min:
                nums_min = nums[middle]
                index = middle
                j = middle - 1
            else:
                i = middle + 1
        
        return [index, nums_min]

# Test Cases

s = Solution()
print(s.search([5,1,3], 5))
print(s.search([4,5,6,7,0,1,2], 0))