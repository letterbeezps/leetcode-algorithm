class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visit = [[0] * col for i in range(row)]
        
        def dfs(x: int, y: int, u: int):
            if u == len(word):
                return True
            visit[x][y] = 1
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
            for i in range(4):
                a,b = x + dx[i], y + dy[i]
                if 0<=a<row and 0<=b<col and 1-visit[a][b] and board[a][b] == word[u]:
                    if dfs(a,b,u+1):
                        return True
            #end_for
            visit[x][y] = 0
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        #end_for
        return False

################################
#############  C++  ############

class Solution {
public:
    
    int n,m;
    vector<vector<char>> board;
    vector<vector<bool>> st;
    string word;
    
    bool exist(vector<vector<char>>& _board, string _word) {
        board = _board, word = _word;
        
        n = board.size(), m = board[0].size();
        st = vector<vector<bool>> (n, vector<bool>(m, false));
        
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
            {
                if (board[i][j] == word[0])
                {
                    if (dfs(i, j, 1))
                        return true;
                }
            }
        return false;
    }
    
    bool dfs(int x, int y, int u)
    {
        st[x][y] = true;
        if (u==word.size()) return true;
        int dx[4]={-1,0,1,0}, dy[4]={0,1,0,-1};
        for (int i=0; i<4; i++)
        {
            int a = x + dx[i], b = y + dy[i];
            if (a>=0 && a<n && b>=0 && b<m && !st[a][b] && board[a][b]==word[u])
            {
                if (dfs(a,b,u+1)) return true;
            }
        }
        st[x][y] = false;
        
        return false;
    }
};