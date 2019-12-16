class Solution {
public:
    static bool cmp(vector<int> a, vector<int> b) {
        return a[0] < b[0];
    }
    
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        if (intervals.empty()) return res;
        sort(intervals.begin(), intervals.end());
        int st = intervals[0][0], ed = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++)
        {
            if (ed < intervals[i][0])
            {
                res.push_back({st, ed});
                st = intervals[i][0], ed = intervals[i][1];
            }
            else
                ed = max(ed, intervals[i][1]);
        }
        res.push_back({st, ed});
        return res;
    }
};