class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        IndexSum = 3000
        dic = {}
        for i, s1 in enumerate(list1):
            dic[s1] = i
            
        # print(dic)
        for i, s2 in enumerate(list2):
            if s2 in dic and dic[s2]+i <= IndexSum:
                if dic[s2]+i == IndexSum:
                    res.append(s2)
                else:
                    res = []
                    res.append(s2)
                IndexSum = dic[s2] + i
        return res
        