class Solution {
public:
    string reverseWords(string s) {
        int i=0, k=0;
        s += ' ';
        while (k < s.size() && s[k] == ' ') k ++;
        while (k < s.size())
        {
            if (s[k] != ' ')
                s[i++] = s[k++];
            else
            {
                s[i++] = ' ';
                while (k < s.size() && s[k] == ' ') k ++;
            }
        }
        if (!i)
        {
            s = "";
            return s;
        }
        s.erase(s.begin()+i-1, s.end());
        
        for (int i = 0; i< s.size(); i++)
        {
            // reverse every word
            int j = i;
            while (j < s.size() && s[j] != ' ') j ++;
            reverse(s.begin()+i, s.begin()+j);
            i = j;
        }
       
        // reverse all string
        reverse(s.begin(), s.end());
        
        return s;
    }
};