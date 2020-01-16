class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.cbegin(), wordDict.cend());
        
        return wordBreak(s, dict);
    }
    
    bool wordBreak(string s, const unordered_set<string>& dict)
    {
        if (mem_.count(s)) return mem_[s];
        
        if (dict.count(s)) return mem_[s] = true;
        
        for (int j=1; j<s.length(); j++)
        {
            const string left = s.substr(0,j);
            const string right = s.substr(j);
            if (dict.count(right) && wordBreak(left, dict))
                return mem_[s]=true;
        }
        return mem_[s]=false;
    }
    
private:
    unordered_map<string, bool> mem_;
};