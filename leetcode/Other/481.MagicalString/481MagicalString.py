class Solution:
    def magicalString(self, n: int) -> int:
        s = '122'
        k = 1
        for i in range(2, n):
            for j in range(int(s[i])):
                s += str(k)
            
            k = 3 - k
        res = 0
        for x in s[:n]:
            res += x == '1'
        return res
        