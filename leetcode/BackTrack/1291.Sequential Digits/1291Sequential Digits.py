class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        
        def solve(num):
            # print(ans)
            if num > high:
                return
            if low <= num:
                ans.append(num)
            if num%10 < 9:
                solve(num*10 + num%10+1)
        
        for i in range(1, 10):
            solve(i)
        ans.sort()
        return ans
        
    
        