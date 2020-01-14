class Solution {
public:
    int minInsertions(string s) {
        const int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n));
        
        for (int l=2; l<=n; l++) //长度为0和1的时候，所需步数都是0
            for (int i=0, j=l-1; j<n; ++i, ++j)
                dp[i][j] = s[i]==s[j]? dp[i+1][j-1]: min(dp[i+1][j], dp[i][j-1]) + 1;
        return dp[0][n-1];
    }
};