var search = function(nums, target) {
    if (nums.length == 0) return -1;
    if (nums.length == 1) return nums[0] == target ? 0 : -1;
    var l = 0;
    var r = nums.length - 1;
    while (l < r) {
        if (nums[l] == target) {
            return l;
        } else if (nums[r] == target) {
            return r;
        }

        if (nums[l] > target) {
            while (nums[r] == nums[r - 1]) {
                r--;
            }
            if (nums[r] < target) {
                return -1;
            } else if (nums[r] > target) {
                r--;
            } else if (nums[r] == target) {
                return r;
            }
        } else if (nums[l] < target) {
            // 跳过数组一样的
            while (nums[l] == nums[l + 1]) {
                l++;
            }

            if (nums[l] < nums[l + 1]) {
                l++;
            } else {
                return -1;
            }
        } else if (nums[l] < nums[r]) {
            return -1;
        }
    }
    return -1;
};
