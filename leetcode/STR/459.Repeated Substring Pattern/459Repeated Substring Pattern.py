'''
s = n*a, n>=2
s+s = a + (n-1)*a + (n-1)*a + a
s+s = a + (2n-2)*a + a
2n-2 >= n, n>=2
s+s[1:-1] must contain s if s = n*a, n>=2
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1