class Solution:
    def twoSum(self, numbers, target):

        numbers_hash = {}
        for i in range(len(numbers)):
            index1 = target - numbers[i]
            if index1 in numbers_hash:
                return [numbers_hash[index1]+1, i+1]
             
            numbers_hash[numbers[i]] = i
        

# Test Cases

s = Solution()
print(s.twoSum([7,1,5,3,6,4], 10))