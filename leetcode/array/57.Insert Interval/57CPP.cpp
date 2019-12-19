class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        
        bool has_in = false;
        
        for (auto interval : intervals)
        {
            if (interval[0] > newInterval[1])
            {
                if (!has_in)
                {
                    res.push_back(newInterval);
                    has_in = true;
                }
                res.push_back(interval);
            }
            else if (interval[1] < newInterval[0])
            {
                res.push_back(interval);
            }
            else
            {
                newInterval[0] = min(newInterval[0], interval[0]);
                newInterval[1] = max(newInterval[1], interval[1]);
            }
        }
        if (!has_in) res.push_back(newInterval);
        return res;
    }
};