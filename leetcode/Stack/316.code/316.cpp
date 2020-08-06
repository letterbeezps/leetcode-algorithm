class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n = s.size();
        vector<int> c(26, 0), visit(26, 0);
        // 假设 ans 是当前i个字符得到的最小结果
        string ans;
        for (int i = 0; i<n; i++)
            ++c[s[i]-'a']; // 统计每个字符的个数

        for (int i=0; i<n; i++)
        {
            --c[s[i]-'a'];
            if (visit[s[i] - 'a']) continue;
            while (ans.size() && s[i] < ans.back() && c[ans.back()-'a'])
                visit[ans.back()-'a'] = 0, ans.pop_back();
            ans.push_back(s[i]);
            visit[s[i]-'a'] = 1;
        }
        return ans;
    }
};