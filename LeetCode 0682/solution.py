class Solution:
    def calPoints(self, operations):

        record = []

        for operation in operations:
            if operation == "+":
                record.append(record[-1] + record[-2])
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "C":
                record.pop()
            else:
                record.append(int(operation))

        return sum(record)

# Test Cases

s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))