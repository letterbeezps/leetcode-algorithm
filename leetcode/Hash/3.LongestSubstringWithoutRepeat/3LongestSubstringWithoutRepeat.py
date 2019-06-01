'''
a->b->c->d->e->b->a->e
l              r
use left right two pointers
同时要记录l  ---   r中间的字符，表示已经访问，碰撞重复访问
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        find = collections.defaultdict(bool)
        
        maxn = 0
        left = right = 0
        while left<len(s) and right<len(s):
            if find[s[right]] == False:
                find[s[right]] = True
                right += 1
            else:
                maxn = max(maxn,right-left)
                while left < right and s[left] != s[right]:
                    find[s[left]] = False
                    left += 1
                left += 1
                right += 1
        #end_while
        maxn = max(maxn,right-left)
        return maxn