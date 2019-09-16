class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        dic = {}
        Set = set()
        for s, t in zip(S, T):
            if s not in dic:
                if t in Set:
                    return False
                dic[s] = t
                Set.add(t)
            if s in dic:
                if dic[s] != t:
                    return False
        #print
        return True