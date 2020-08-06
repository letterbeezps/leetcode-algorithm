'''
一个最长的回文串可以有 2n+1个字符
XXXXxxxxx ? xxxxxXXXX 这样的结构
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = Counter(s)
        for val in counter.values():
            res += val // 2 * 2
            if res % 2 == 0 and val % 2 == 1:
                res += 1
                
        return res