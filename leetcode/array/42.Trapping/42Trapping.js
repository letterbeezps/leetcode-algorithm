/*
 * @lc app=leetcode.cn id=42 lang=javascript
 *
 * [42] 接雨水
 */
/**
 * @param {number[]} height
 * @return {number}
 * 
 * 双指针算法，一般暴力法，如果2个指针之间存在一定的线性关系，都可以使用双指针优化
 * ✔ Accepted
  ✔ 315/315 cases passed (68 ms)
  ✔ Your runtime beats 100 % of javascript submissions
  ✔ Your memory usage beats 74.32 % of javascript submissions (34.9 MB)
 */
var trap = function(height) {
    var left = 0,
        right = height.length - 1;
    var ans = 0;
    var left_max = 0,
        right_max = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            height[left] >= left_max
                ? (left_max = height[left])
                : (ans += left_max - height[left]);
            ++left;
        } else {
            height[right] >= right_max
                ? (right_max = height[right])
                : (ans += right_max - height[right]);
            --right;
        }
    }
    return ans;
};
