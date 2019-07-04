'''
(()()))()
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not len(s):
            return 0
        maxn, leftmost = 0, -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # 存储的是每个左括号的下标
            else:
                if len(stack) == 0:  # 当前是右括号，而且没有与之对应的左括号，那么该右括号之前的字符串不会继续参与计算最长合法子串了
                    leftmost = i
                else:
                    stack.pop()  # 当前是右括号 且有与之对应的左括号
                    '''
                    if len(stack) == 0:
                        maxn = max(maxn, i-leftmost)
                    else:
                        maxn = max(maxn, i-stack[-1])
                    '''
                    maxn = max(maxn, i-leftmost) if not len(stack) else max(maxn, i-stack[-1])
        #end_for
        return maxn