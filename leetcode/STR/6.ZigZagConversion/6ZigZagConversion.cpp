class Solution {
public:
    string convert(string s, int numRows) {
        string res;
        if (numRows == 1) return s;
        
        for (int j=0; j<numRows; j++)
        {
            if (j==0 || j==numRows-1)
                for (int i = j;i<s.size(); i+=(numRows-1)*2)
                    res += s[i];
            
            else
            {
                for (int k = j, i=(numRows-1)*2-j;
                    i<s.size() || k<s.size();
                    i+=(numRows-1)*2, k+=(numRows-1)*2)
                {
                    if (k<s.size()) res+=s[k];
                    if (i<s.size()) res+=s[i];
                }
            }
        }
        return res;
    }
};