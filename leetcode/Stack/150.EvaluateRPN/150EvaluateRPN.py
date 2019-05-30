class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []
        for x in tokens:
            if x == '+' or x == '-' or x == '*' or x == '/':
                a = Stack.pop()
                b = Stack.pop()
                if x == '+':
                    Stack.append(a+b)
                elif x == '-':
                    Stack.append(b-a)
                elif x == '*':
                    Stack.append(a*b)
                else:
                    '''
                    除法繁琐的根源在于python对于除法的处理
                    如果是C++可以直接 (b /a)
                    '''
                    if a < 0 and b < 0:
                        Stack.append((abs(b) // abs(a)))
                    elif a < 0 or b < 0:
                        Stack.append(-(abs(b) // abs(a)))
                    else:
                        Stack.append(b // a)
                #print(Stack)
            else:
                Stack.append(int(x))
                #print(Stack)
        #end_for
        return Stack.pop()