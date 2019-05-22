class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        # left表示正括号数目
        # right表示反括号数目
        def dfs(curr: str, res, n: int, left: int, right: int):
            if right == n:
                res.append(curr)
                return
            if left < n:
                dfs(curr+'(', res, n, left+1, right)
            if right < left:
                dfs(curr+')', res, n, left, right+1)
        
        dfs('', res, n, 0 ,0)
        return res