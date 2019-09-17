var isMatch = function(s = 'abcdedfg', p = 'abcde.*') {
    // 初始化矩阵 dp[i][j]代表s的前i个字符和p的前j个字符是否匹配
    let dp = [];
    for (let i = 0; i <= s.length; i++) {
        dp[i] = [];
        for (let j = 0; j <= p.length; j++) {
            dp[i][j] = false;
        }
    }

    // 都是空字符串必定匹配
    dp[0][0] = true;

    //如果p[j-1]为*， 则空串s和p前j位是否匹配与空串s和p前j - 2位结果一致
    for (let j = 1; j <= p.length; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = !!dp[0][j - 2];
        }
    }
// 遍历整个字符串s 
// 对于每个i  遍历p
// 1. 如果s中第i个元素等于p中第j个字符 或者p中第j个字符等于`.`  则匹配性不变 
// 2.p中第j个字符等于* 分类讨论
//3.其他情况 则不匹配

    for (let i = 1; i <= s.length; i++) {
        for (let j = 1; j <= p.length; j++) {
            if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                if (dp[i][j - 2]) {
                    dp[i][j] = dp[i][j - 2];
                } else if (s[i - 1] == p[j - 2] || p[j - 2] == '.') {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = false;
                }
            } else {
                dp[i][j] = false;
            }
        }
    }
    return dp[s.length][p.length];
};

// 使用正则对象
var CHEET_isMatch = function(s, p) {
    const reg =  new RegExp(`^${p}$`);
    return reg.test(s)
};