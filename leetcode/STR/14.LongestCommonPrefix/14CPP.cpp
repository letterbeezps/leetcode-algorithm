class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string res;
        string &first = strs[0];
        for (int i=0; ;i++)
        {
            bool flag = false;
            
            for (auto &now : strs)
                if (i>=first.size() || i>=now.size() || first[i]!=now[i])
                {
                    flag = true;
                    break;
                }
            if (flag) break;
            res += first[i];
        }
        
        return res;
    }
};