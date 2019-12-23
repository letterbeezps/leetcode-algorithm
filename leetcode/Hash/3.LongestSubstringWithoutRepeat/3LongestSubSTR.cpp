class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hash;
        int res = 0;
        for (int i=0,j=0;j<s.size();j++)
        {
            if (++hash[s[j]] > 1)
            {
                while (i<j)
                {
                    hash[s[i]]--;
                    i++;
                    if (hash[s[j]] == 1) break;
                }
            }
            res = max(res, j-i+1);
        }
        return res;
    }
};