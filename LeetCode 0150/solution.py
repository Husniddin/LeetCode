class Solution:
    def evalRPN(self, tokens):
        operators = ["+", "-", "*", "/"]
        integers = []
        for token in tokens:
            if token in operators:
                b, a = integers.pop(), integers.pop()
                if token == "+":
                    integers.append(a+b)
                elif token == "-":
                    integers.append(a-b)
                elif token == "*":
                    integers.append(a*b)
                elif token == "/":
                    integers.append(int(a/b))
            else:
                integers.append(int(token))

        return integers[0]
# Test Cases

s = Solution()
print(s.evalRPN(["4","-2","/","2","-3","-","-"]))
# print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(s.evalRPN(["4","13","5","/","+"]))
# print(s.evalRPN(["1"]))