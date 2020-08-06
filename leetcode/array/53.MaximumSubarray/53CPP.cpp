class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> f(nums.size());
        f[0] = nums[0];
        for (int i=1; i<nums.size(); i++)
        {
            f[i] = max(nums[i]+f[i-1], nums[i]);
        }
        return *std::max_element(f.begin(), f.end());
    }
};