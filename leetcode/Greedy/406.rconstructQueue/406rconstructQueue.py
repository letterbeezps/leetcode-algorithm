'''
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
排序后，每个人的身高小于等于前面的身高
然后再根据k把排序后的序列插入到结果序列
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda s: [-s[0], s[1]])
        # [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        
        res = []
        for item in people:
            res.insert(0+item[1], item)
        return res