class Solution:
    def calculate(self, s: str) -> int:
        stack_op = []
        stack_num = []
        s += '+0'  # 处理边界问题
        
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] in '+-*/':
                stack_op.append(s[i])
            else:
                j = i
                while j<len(s) and '0'<=s[j]<='9':
                    j += 1
                stack_num.append(int(s[i:j]))
                i = j-1
                if stack_op:
                    if stack_op[-1] in '*/':
                        y, x = stack_num.pop(), stack_num.pop()
                        if stack_op[-1] == '*':
                            stack_num.append(x*y)
                        else:
                            stack_num.append(x//y)
                        stack_op.pop()
                    elif len(stack_op) >= 2:  #开头的预处理'+0'
                        z,y,x = stack_num.pop(),stack_num.pop(),stack_num.pop()
                        op2,op1 = stack_op.pop(), stack_op.pop()
                        if op1 == '+':
                            stack_num.append(x+y)
                        else:
                            stack_num.append(x-y)
                        stack_num.append(z)
                        stack_op.append(op2)
            i += 1
        #end_while
        stack_num.pop()
        return stack_num[-1]