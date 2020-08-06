class UniFind{
public:
    vector<int> father;
    UniFind(int num) {
        for (int i = 0; i < num; i++)
            father.push_back(i);
    }
    int getFather(int n){
        if (father[n] != n)
            father[n] = getFather(father[n]);
        return father[n];
    }
    void Union(int a, int b){
        int fa = getFather(a);
        int fb = getFather(b);
        if (fa != fb)
            father[fb] = fa;
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int N = M.size();
        UniFind UF(N);
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (M[i][j]) {
                    UF.Union(i, j);
                }
            }
        } // for
        int res = 0;
        for (int i=0; i<N; i++){
            if(UF.getFather(i) == i)
                res ++;
        }
        return res;
    }
};

////////////////////Graph/////////
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        if (M.empty()) return 0;
        int n = M.size();
        vector<int> visited(n, 0);
        int ans = 0;
        for (int i=0; i<n; i++)
        {
            if (visited[i]) continue;
            dfs(M, i, n, visited);
            ++ans;
        }
        return ans;
    }
private:
    void dfs(const vector<vector<int>>& M, int cur, int n, vector<int>& visited)
    {
        if (visited[cur]) return;
        visited[cur] = 1;
        for (int i=0; i<n; i++)
            if (M[cur][i] && !visited[i])
                dfs(M, i, n, visited);
    }
};