/**
 * @param {number[]} nums
 * @return {boolean}
 */
// Runtime: 52 ms, faster than 99.40% of JavaScript online submissions for Non-decreasing Array.
// Memory Usage: 36.4 MB, less than 100.00% of JavaScript online submissions for Non-decreasing Array.

var checkPossibility = function(nums) {
    let result = 0;
    nums.reduce((acc, cur, index) => {
        if (acc > cur) {
            result++;
            //当前值前面的元素已经形成长度大于1的非减序列 且 当前值且当前值小于上上一个值 则修改当前值为acc
            if (index - 2 >= 0 && cur < nums[index - 2]) {
                return acc;
            } else {
                return cur;
            }
        } else {
            return cur;
        }
    });
    return result < 2;
};
