class Solution:
    
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for char in S:
            if char.isalpha():
                res *= 2
                for i in range(len(res)):
                    if i < len(res)/2:
                        res[i] += char.lower()
                    else:
                        res[i] += char.upper()
            else:
                for j in range(len(res)):
                    res[j] += char
        
        return res
    
    
##############################
############for c++###########
##############################
'''
class Solution {
public:
    vector<string> res;
    vector<string> letterCasePermutation(string S) {
        dfs(S, 0);
        return res;
    }
    
    void dfs(string S, int u) {
        if (u == S.size()) {
            res.push_back(S);
            return;
        } 
        
        dfs(S, u+1);
        if (S[u] >= 'A') {
            S[u] ^= 32;
            dfs(S, u+1);
        }
    }
};
'''