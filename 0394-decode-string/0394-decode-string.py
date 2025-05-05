# 2[ab]c
# 2[4[ab]c]
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not s[i] == "]":
                stack.append(s[i])
            else:
                sub = ""
                top = stack.pop()
                while top != "[":
                    sub = top + sub
                    top = stack.pop()
                
                digit = ""
                while stack and stack[-1].isdigit():
                    top = stack.pop()
                    digit = top + digit
                
                re = int(digit) # 숫자 추출
                for r in range(re):
                    stack.append(sub)
        
        return ''.join(stack)
