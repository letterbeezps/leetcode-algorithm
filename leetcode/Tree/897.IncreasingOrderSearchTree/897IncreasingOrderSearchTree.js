var increasingBST = function(root) {
    const s = [];
    const dummy = new TreeNode(null);
    let p = dummy;
    while (s.length > 0 || root) {
        if (root) {
            s.push(root);
            root = root.left;
        } else {
            const cur = s.pop();
            root = cur.right;
            cur.left = null;
            p.right = cur;
            p = p.right;
        }
    }
    return dummy.right;
};