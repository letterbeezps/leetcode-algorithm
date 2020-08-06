class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for x in range(left, right+1):
            t = x
            valid = True
             
            while t and valid:
                r = t % 10
                if not r or x % r:
                    valid = False
                t //= 10
            if valid:
                ans.append(x)
        return ans
                
        