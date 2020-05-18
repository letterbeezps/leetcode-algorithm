class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> s;
        int l = 0;
        int ans = 0;
        for (int r = 0; r < nums.size(); ++r)
        {
            s.insert(nums[r]);
            while (*rbegin(s) - *begin(s) > limit)
                s.erase(s.equal_range(nums[l++]).first);
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};