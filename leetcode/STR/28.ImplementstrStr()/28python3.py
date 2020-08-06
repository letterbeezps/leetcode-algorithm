'''
直接用轮子了，
详细的可以翻阅KMP算法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        

######Solution2 KMP#############
'''
直接用轮子了，
详细的可以翻阅KMP算法
'''
class Solution:
    def strStr(self, s1: str, s2: str) -> int:
        nextn = [0] * len(s2)
        
        return self.kmp(s1, s2, nextn)
        # print(nextn)
    
    def kmp(self, s1: str, s2: str, nextn: list) -> int:
        if not s2:
            return 0
        # 求s1中s2第一次出现的位置
        i, j = 0, 0
        k, ans = -1, 0
        nextn[0] = -1
        lens2 = len(s2)
        while j < lens2:
            while k != -1 and s2[j] != s2[k]:
                k = nextn[k]
            j += 1
            k += 1
            if j < lens2 and k < lens2:
                if s2[j] != s2[k]:
                    nextn[j] = k
                else:
                    nextn[j] = nextn[k]
        # end_while
        
        j = 0
        while i < len(s1):
            if j != -1 and j == lens2:
                return i - j
            while j != -1 and s1[i] != s2[j]:
                j = nextn[j]
                
            i += 1
            j += 1
        #end_while
        if j == lens2:
            return i - j
        else:
            return -1