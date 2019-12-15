class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() < 5)  // 特别小的时候，直接遍历
        {
            for (int i = 0; i<nums.size(); i++)
                if (nums[i]==target)
                    return i;
            return -1;
        }
        int left = 0, right=nums.size()-1;
        
        if (nums[0] > nums.back()) // 第一个数比最后一个数大，那么一定有两个部分
        {
            int l = 0, r = nums.size()-1;
            while (l<r)
            {
                int mid = l+r+1 >> 1;
                if (nums[mid] >= nums[0])
                    l = mid;
                else r = mid-1;
            }
            if (target >= nums[0]) left = 0, right=l;
            else left = l+1, right=nums.size()-1;
        }
        
        while (left < right)
        {
            int mid = left + right >> 1;
            if (nums[mid]<target) left = mid+1;
            else right=mid;
        }
        if (target == nums[left])
            return left;
        else
            return -1;
    }
};