class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:    
        def dfs(n, count = 1):
            if '0' not in str(n) and '0' not in str(count):
                return n    
            n -= 1
            count +=1 
            return dfs(n, count)
        
        num = dfs(n-1)
        return [n - num, num]