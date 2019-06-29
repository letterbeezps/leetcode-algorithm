/**
 * @param {string} s
 * @return {string}
 */

var longestPalindrome = function(s) {
    let max = '';
    for (let index = 0; index < s.length; index++) {
        for (let num = 0; num < 2; num++) {
            let left = index;
            let right = index + num;
            while (left >= 0 && s[left] === s[right]) {
                left--;
                right++;
            }
            if (right - left - 1 > max.length) {
                max = s.substring(left + 1, right);
            }
        }
        if (max.length / 2 >= s.length - index) break;
    }
    return max;
};
