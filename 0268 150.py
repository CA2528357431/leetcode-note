class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isnumeric() or x[0]=="-" and x[1:].isnumeric():
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x=="+":
                    stack.append(a+b)
                elif x=="-":
                    stack.append(a-b)
                elif x=="*":
                    stack.append(a*b)
                else:
                    if a*b>=0:
                        stack.append(abs(a)//abs(b))
                    else:
                        stack.append(abs(a)//abs(b)*-1)
                        # 注意除法。。。
        return stack[0]