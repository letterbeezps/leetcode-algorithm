/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const memo = {};
    for (let i = 0; i < nums.length; i++) {
        const another = target - nums[i];
        if (memo[another] !== undefined) {
            return [memo[another], i];
        }
        memo[nums[i]] = i;
    }
    return [];
};
