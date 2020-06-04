/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */

//  从左下角 向右向上查找
var searchMatrix = function (matrix, target) {
    // matrix[上下][左右]
    let row = matrix.length - 1; // 行
    let column = 0; // 列
    while (row >= 0 && column <= matrix[0].length - 1) {
        if (matrix[row][column] == null) {
            return false;
        }
        if (target > matrix[row][column]) {
            column += 1;
        } else if (target < matrix[row][column]) {
            row -= 1;
        } else if (target === matrix[row][column]) {
            return true;
        }
    }
    return false;
};
