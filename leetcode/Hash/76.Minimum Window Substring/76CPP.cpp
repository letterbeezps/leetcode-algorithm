class Solution {
public:
    string minWindow(string s, string t) {
        string res;
        unordered_map<char, int> S,T;
        for (auto c : t) T[c] ++;
        int total = T.size();
        int satisfy = 0;
        for (int i = 0, j=0; i<s.size(); i++)
        {
            S[s[i]] ++;
            if (S[s[i]] == T[s[i]]) satisfy ++;
            while (S[s[j]] > T[s[j]]) 
            {   
                S[s[j++]] --;
            }
                
            if (satisfy == total && (res.empty() || i-j+1 < res.size()))
                res = s.substr(j,i-j+1);
        }
        return res;
    }
};