class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def Convert(version: str) -> str:
            v = version.split('.')
            return list(map(int, v))
        
        v1 = Convert(version1)
        v2 = Convert(version2)
        num1, num2 = 0, 0
        index1, index2 = 0, 0
        l1, l2 = len(v1), len(v2)
        while index1<l1 or index2<l2:
            if index1 < l1:
                num1 = v1[index1]
                index1 += 1
            if index2 < l2:
                num2 = v2[index2]
                index2 += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            num1, num2 = 0, 0
                
        return 0
        
 ##########solution 2##########
 class Solution:
        def compareVersion(self, version1: str, version2: str) -> int:
        
        def Convert(version: str) -> str:
            v = version.split('.')
            return list(map(int, v))
        
        v1 = Convert(version1)
        v2 = Convert(version2)
        while v1 and not v1[-1]:
            v1.pop()
        while v2 and not v2[-1]:
            v2.pop()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0       