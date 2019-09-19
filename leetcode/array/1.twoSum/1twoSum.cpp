class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            int t = target - nums[i];
            if (hash.count(t)) return vector<int>({hash[t], i});
            hash[nums[i]] = i;
        }
        return vector<int>();
    }
};