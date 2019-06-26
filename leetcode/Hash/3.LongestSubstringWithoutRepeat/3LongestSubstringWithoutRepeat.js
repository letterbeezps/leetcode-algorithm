/**
 * @param {string} s
 * @return {number}
 */
// 将acc中不存在的值push进acc 计算并存储最大长度， 如果acc已存在当前元素则切除前面从0到重复元素部分
// 重新统计后面部分的长度
var lengthOfLongestSubstring = function(s) {
    let max = 0;
    [...s].reduce((acc, curr) => {
        if (!acc.includes(curr)) {
            acc.push(curr);
            max = max > acc.length ? max : acc.length;
        } else {
            acc.splice(0, acc.indexOf(curr) + 1);
            acc.push(curr);
        }
        return acc;
    }, []);
    return max;
};
