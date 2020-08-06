/**
 * @param {number[]} nums
 * @return {number}
 */

//  排序取中位数
var majorityElement$1 = (nums) => nums.sort()[Math.ceil(nums.length / 2) - 1];

/**
 * @param {number[]} nums
 * @return {number}
 */

// 遍历统计
var majorityElement$2 = (nums) => {
    //{ num: count, ... }
    const map = {};
    nums.forEach((num) => {
        map[num] ? (map[num] += 1) : (map[num] = 1);
    });

    for (const [key, value] of Object.entries(map)) {
        if (value > nums.length / 2) {
            return key;
        }
    }
};

// 由于这个过半的元素一定存在 也就是说它的出现次数比其他所有元素加起来都多
// 遍历到相同元素 count+1 否则count-1 count === 0 切换result 最后肯定会有目标元素result剩余
var majorityElement$3 = (nums) => {
    let count = 0;
    let result;
    for (let i = 0; i < nums.length; i++) {
        if (count === 0) {
            result = nums[i];
            count += 1;
        } else if (result !== nums[i]) {
            count -= 1;
        } else {
            count += 1;
        }
    }

    return result;
};
