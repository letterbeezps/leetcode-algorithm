/*
 * @Date: 2020-06-10 13:17:49
 * @LastEditors: 周泽泽
 * @LastEditTime: 2020-06-10 13:37:06
 * @FilePath: /leetcode-algorithm/leetcode/array/26.removeDuplicate/26removeDuplicate.js
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let len = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) {
            len += 1;
            nums[len - 1] = nums[i];
        }
    }
    return len;
};
