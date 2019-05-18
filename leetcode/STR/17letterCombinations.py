class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        '''
        简单的dfs分析
        '''
        def dfs(digits: str, d: int, cur: str):
            if d == len(digits):
                res.append(cur)
                return
            
            cur_num = int(digits[d])
            for x in digit[cur_num]:
                dfs(digits, d+1, cur+x)
                
        if digits == '':
            return res
        dfs(digits, 0, '')
        return res