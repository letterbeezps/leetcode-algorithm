'''
["ate","eat","tea"]它们的排序结果都是'aet'
可以用来构建一个字典结构
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if not strs:
            return res
        HashMap = collections.defaultdict(list) # list[str]
        for x in strs:
            NewStr = ''.join(sorted(x))
            HashMap[NewStr].append(x)
        for x in HashMap.values():
            res.append(x)
        return res