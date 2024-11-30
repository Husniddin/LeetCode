class Solution:
    def mostFrequentEven(self, nums):
        nums_hash = {}

        for num in nums:
            if num%2 == 1:
                continue

            nums_hash[num] = nums_hash.get(num, 0) + 1

        max_frequency = 0
        most_frequent_el = float("inf")
 
        for num, frequency in nums_hash.items():
            if frequency > max_frequency:
                max_frequency = frequency
                most_frequent_el = num
            elif frequency == max_frequency and num < most_frequent_el:
                most_frequent_el = num
            
        return -1 if max_frequency == 0 else most_frequent_el


# Test Cases

s = Solution()
print(s.mostFrequentEven([0,1,2,2,4,4,1]))
print(s.mostFrequentEven([4,4,4,9,2,4]))
print(s.mostFrequentEven([29,47,21,41,13,37,25,7]))