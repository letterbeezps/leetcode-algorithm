class Solution {
public:
    string longestPalindrome(string s) {
        int len = 0;
        string ans;
        for (int k = 0; k < s.size(); k++)
        {
            int i = k, j = k+1;
            while (i >=0 && j < s.size() && s[i]==s[j]) i--, j++;
            if (j-i-1 > len)
            {
                len = j-i-1;
                ans = s.substr(i+1, len);
            }
            i = k-1, j = k+1;
            while (i >=0 && j < s.size() && s[i]==s[j]) i--, j++;
            if (j-i-1 > len)
            {
                len = j-i-1;
                ans = s.substr(i+1, len);
            }
        }
        return ans;
    }
};