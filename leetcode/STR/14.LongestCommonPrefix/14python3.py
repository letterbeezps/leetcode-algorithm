class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        res = ''
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        return res