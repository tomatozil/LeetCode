class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def is_sign(char) -> bool:
            sign = ['+', '-', '*', '/']
            if char in sign:
                return True
            return False

        def cal(n1, n2, op):
            if op == '+':
                return n1+n2
            elif op == '-':
                return n1-n2
            elif op == '*':
                return n1*n2
            else:
                return int(n1/n2)
        
        for s in tokens:
            if is_sign(s) and len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                ret = cal(n2, n1, s)
                stack.append(ret)
            else:
                stack.append(int(s))
        
        return stack.pop()