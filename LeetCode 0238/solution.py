class Solution:
    def productExceptSelf(self, nums):
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0 for i in range(len(nums))]

        product = 1
        for num in nums:
            if num == 0:
                continue
            product *= num

        if zero_count == 1:
            answer = [0 for i in range(len(nums))]
            zero_index = nums.index(0)
            answer[zero_index] = product
            return answer 

        answer = []
        for num in nums:
            answer.append(product//num)
        
        return answer

# Test Cases

s = Solution()
print(s.productExceptSelf([0,2,3,4,6,8,9]))
print(s.productExceptSelf([0,1,2,4,5,7]))
print(s.productExceptSelf([0,1,2,0,5,7]))
print(s.productExceptSelf([5,1,2,1,5,7]))
print(s.productExceptSelf([-3, 3]))