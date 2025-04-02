class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if stack and brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return not stack