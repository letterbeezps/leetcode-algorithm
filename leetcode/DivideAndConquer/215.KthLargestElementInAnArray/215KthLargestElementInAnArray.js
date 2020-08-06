/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest$1 = function (nums, k) {
    if (!nums || nums.length === 0) {
        return 0;
    }
    function qs(nums, l, r) {
        if (l >= r) {
            return;
        }
        let x = nums[(l + r) >> 1];
        let i = l - 1;
        let j = r + 1;
        while (i < j) {
            i++;
            while (nums[i] < x) {
                i++;
            }
            j--;
            while (nums[j] > x) {
                j--;
            }
            if (i < j) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
            }
        }
        qs(nums, l, j);
        qs(nums, j + 1, r);
    }
    qs(nums, 0, nums.length - 1);
    return nums[nums.length - k];
};
