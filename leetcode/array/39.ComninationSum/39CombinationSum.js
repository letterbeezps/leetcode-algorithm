/*
 * @lc app=leetcode.cn id=39 lang=javascript
 *
 * [39] 组合总和
 */
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 * 典型的回溯法
 *  ✔ Accepted
  ✔ 168/168 cases passed (76 ms)
  ✔ Your runtime beats 100 % of javascript submissions
  ✔ Your memory usage beats 72.81 % of javascript submissions (36.7 MB)
 */
var combinationSum = function(candidates, target) {
    var res = [];
    var path = [];
    rept(candidates, target, 0, path, res);
    function rept(candidates, target, it, path, res) {
        if (target < 0) return;
        if (target === 0) {
            path = path.slice();
            res.push(path);
            return;
        }
        for (var i = it; i < candidates.length; i++) {
            path.push(candidates[i]);
            rept(candidates, target - candidates[i], i, path, res);
            path.pop();
        }
    }
    return res;
};
