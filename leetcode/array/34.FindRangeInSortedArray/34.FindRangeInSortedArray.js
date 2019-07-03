/**
 * 
✔ Accepted
  ✔ 88/88 cases passed (84 ms)
  ✔ Your runtime beats 84.08 % of javascript submissions
  ✔ Your memory usage beats 35.88 % of javascript submissions (35.1 MB)
 */

var searchRange = function(nums, target) {
    var mid = Math.floor(nums.length / 2);
    if (nums[0] > target || nums[nums.length - 1] < target) return [-1, -1];

    // 判断往那边
    var count = 0;
    var l = mid;
    var r = mid;
    if (target > nums[mid]) {
        count = 1;
    } else if (target < nums[mid]) {
        count = -1;
    }

    while (nums[mid] != target) {
        mid += count;
        l = mid;
        r = mid;
        if (mid > nums.length - 1 || mid < 0) {
            return [-1, -1];
        }
    }
    while (nums[mid] == nums[mid + 1]) {
        mid++;
        r = mid;
    }
    while (nums[mid - 1] == nums[mid]) {
        mid--;
        l = mid;
    }
    return [l, r];
};
