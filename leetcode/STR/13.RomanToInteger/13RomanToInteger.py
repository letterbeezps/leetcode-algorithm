'''
I V X L C D M
CD CM XC XL IX IV
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0
        if s.find('CM') != -1: res -= 200
        if s.find('CD') != -1: res -= 200
        if s.find('XC') != -1: res -= 20
        if s.find('XL') != -1: res -= 20
        if s.find('IX') != -1: res -= 2
        if s.find('IV') != -1: res -= 2
        for c in s:
            if c == 'M': res += 1000
            elif c == 'D': res += 500
            elif c == 'C': res += 100
            elif c == 'L': res += 50
            elif c == 'X': res += 10
            elif c == 'V': res += 5
            elif c == 'I': res += 1
        return res

############################################
#################### C + + #################
class Solution {
public:
    int romanToInt(string s) {
        int n = s.length(), ans = 0;
        unordered_map<char, int> words;
        words['I'] = 1; words['V'] = 5;
        words['X'] = 10; words['L'] = 50; 
        words['C'] = 100; words['D'] = 500;
        words['M'] = 1000;
        for (int i = 0; i < n; i++) {
            if (i != n - 1 && words[s[i + 1]] > words[s[i]]) {
                ans += words[s[i + 1]] - words[s[i]];
                i++;
            }
            else
                ans += words[s[i]];
        }
        return ans;
    }
};
 