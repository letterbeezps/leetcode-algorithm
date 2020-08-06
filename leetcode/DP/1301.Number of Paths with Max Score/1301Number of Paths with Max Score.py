class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        modulo = 1e9 + 7
        n = len(board)
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        cc = [[0] * (n+1) for _ in range(n+1)]
        
        # board[n-1][n-1] = board[0][0] = '0'
        
        cc[n-1][n-1] = 1
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] != 'X':
                    m = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    if board[i][j] in ['E', 'S']:
                        dp[i][j] = m
                    else:
                        dp[i][j] = m+int(board[i][j])
                    if dp[i+1][j] == m:
                        cc[i][j] = (cc[i][j] + cc[i+1][j]) % modulo
                    if dp[i][j+1] == m:
                        cc[i][j] = (cc[i][j] + cc[i][j+1]) % modulo
                    if dp[i+1][j+1] == m:
                        cc[i][j] = (cc[i][j] + cc[i+1][j+1]) % modulo
        return [dp[0][0] if cc[0][0] else 0, int(cc[0][0])]