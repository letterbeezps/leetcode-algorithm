class Solution:
    def isValid(self, s: str) -> bool:
        mark = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                mark.append(s[i])
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(mark) == 0:
                    return False
                cur = mark.pop()
                if cur == '(' and s[i] != ')':
                    return False
                if cur == '{' and s[i] != '}':
                    return False
                if cur == '[' and s[i] != ']':
                    return False
        if len(mark) == 0:
            return True
        return False