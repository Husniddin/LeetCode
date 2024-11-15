class Solution:
    def isValid(self, strs: str) -> bool:
        correct = True
        parentheses = {'(':')', '{':'}', '[':']'}
        stack = []

        for s in strs:
            if s in parentheses:
                stack.append(s)
            elif len(stack) == 0:
                correct = False
            else:
                last_item = stack.pop()
                if parentheses[last_item] != s:
                    correct = False
                    break

        if len(stack) > 0:
            correct = False

        return correct

# Test Cases

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))