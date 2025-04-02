from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        s_q = deque(s)
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        while s_q:
            b = s_q.popleft()
            if b in list(brackets):
                stack.append(b)
            else:
                if not stack: return False
                open_bracket = stack.pop()
                if b != brackets[open_bracket]:
                    return False
        
        if stack:
            return False
        return True