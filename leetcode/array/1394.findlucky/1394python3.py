class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        count = [0] * 550
        
        for item in arr:
            count[item] += 1
            
        for i in range(500, 0, -1):
            if i == count[i]:
                return i
        return -1
        