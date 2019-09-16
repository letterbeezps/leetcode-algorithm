/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */

var verticalTraversal = function(root) {
    if (!root) return [];
    let posNodeList = [];
    let current = [[0, 0, root]];
    while (current.length > 0) {
        const [x, y, node] = current.shift();
        if (node.val == 6 || node.val == 5) {
        }

        posNodeList.push([x, y, node]);
        if (node.left) {
            current.push([x - 1, y - 1, node.left]);
        }
        if (node.right) {
            current.push([x + 1, y - 1, node.right]);
        }
    }
    const compare = (a, b) => {
        if (a[0] === b[0]) {
            if (a[1] === b[1]) {
                return a[2].val - b[2].val;
            }
            return b[1] - a[1];
        }
        return a[0] - b[0];
    };

    posNodeList = posNodeList.sort(compare);
    const result = [];
    posNodeList.reduce((acc, cur, index) => {
        if (index === 0) {
            result.push([cur[2].val]);
            return cur;
        }
        if (acc[0] === cur[0]) {
            result[result.length - 1].push(cur[2].val);
            return cur;
        } else {
            result.push([cur[2].val]);
            return cur;
        }
    }, []);
    return result;
};
