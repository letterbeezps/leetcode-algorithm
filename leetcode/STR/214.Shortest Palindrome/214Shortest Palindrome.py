# 本质是一个kmp问题
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_1 = s
        s = s + '#' + s[::-1] + '*'
        length = len(s)
        nextn = [0] * length
        i,j = 0, 0
        k = -1
        nextn[0] = -1
        while j<length:
            while k != -1 and s[j] != s[k]:
                k = nextn[k]
            k += 1
            j += 1
            if j < length and k < length:
                if s[j] != s[k]:
                    nextn[j] = k
                else:
                    nextn[j] = nextn[k]
        return s_1[nextn[-1]:][::-1]+s_1