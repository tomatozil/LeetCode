# 2[ab]c
# 2[4[ab]c]
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i) -> (str, int):
            ret = ""
            while i < len(s):
                if s[i] == "]":
                    return ret, i+1
                else:
                    if not s[i].isdigit():
                        ret += s[i]
                        i += 1
                    else:
                        digit = ""
                        while i < len(s) and s[i].isdigit():
                            digit += s[i]
                            i += 1
                        sub, jump = decode(i+1) # [ 다음부터 줌
                        re = int(digit) # 숫자 추출
                        for r in range(re):
                            ret += sub
                        i = jump
            return ret, i       
        
        return decode(0)[0]
        
        # stack = []
        # for i in range(len(s)):
        #     if not s[i] == "]":
        #         stack.append(s[i])
        #     else:
        #         sub = ""
        #         while stack and stack[-1] != "[":
        #             top = stack.pop()
        #             sub = top + sub
        #         stack.pop() # "["" 빼기

        #         digit = ""
        #         while stack and stack[-1].isdigit():
        #             top = stack.pop()
        #             digit = top + digit
                
        #         re = int(digit) # 숫자 추출
        #         for r in range(re):
        #             stack.append(sub)
        
        # return ''.join(stack)
