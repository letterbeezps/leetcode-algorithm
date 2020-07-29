/**
 * @param {number[][]} dungeon
 * @return {number}
 */
// 有时间我再把正向的搞搞
// var calculateMinimumHP = function (dungeon) {
//     const dp = Array.from({ length: dungeon.length }, () =>
//         Array.from({ length: dungeon[0].length }, () => ({}))
//     );
//     //  正向
//     // dp[i][j] 当前点所需生命 向右 向下取较大值
//     // 当前值取决于后续的负值
//     // 到当前格  一共 加了多少 减了多少命 自带了多少命 上一步生命 当前格生命
//     //  + -> -
//     // 0 ->
//     // 上一步生命
//     // - -> +

//     //  - -> - 直接减
//     //  + -> + 直接加

//     for (let i = 0; i < dungeon.length; i++) {}
// };

// 反向操作
var calculateMinimumHP$1 = function (dungeon) {
    const row = dungeon.length;
    const col = dungeon[0].length;
    const dp = Array.from({ length: row + 1 }, () =>
        Array.from({ length: col + 1 }, () => Infinity)
    );
    dp[row][col - 1] = 1;

    for (let r = row - 1; r >= 0; r--) {
        for (let c = col - 1; c >= 0; c--) {
            const minPath =
                Math.min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c];
            dp[r][c] = Math.max(1, minPath);
        }
    }
    return dp[0][0];
};
