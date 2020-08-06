class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans = 0;
        for (int x : nums)
        {
            if ((int)(floor(log10(x))) % 2 == 1)
                ans ++;
        }
        return ans;
    }
};