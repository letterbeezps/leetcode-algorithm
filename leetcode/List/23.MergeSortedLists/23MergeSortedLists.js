/**
 * 
 ✔ Accepted
  ✔ 131/131 cases passed (128 ms)
  ✔ Your runtime beats 87.83 % of javascript submissions
  ✔ Your memory usage beats 11.28 % of javascript submissions (46.4 MB)
 */
// 可以优化一点空间

var mergeCore = function(a, b) {
    var l = a,
        r = b;
    var res = [];
    while (l && r) {
        if (l.val < r.val) {
            res.push(l.val);
            l = l.next;
        } else {
            res.push(r.val);
            r = r.next;
        }
    }
    while (l) {
        res.push(l.val);
        l = l.next;
    }
    while (r) {
        res.push(r.val);
        r = r.next;
    }

    var node = new ListNode(null);
    var _node = node;
    for (var i = 0; i < res.length; i++) {
        _node.next = new ListNode(res[i]);
        _node = _node.next;
    }
    return node.next;
};
var mergeKLists = function(lists) {
    if (lists.length === 0) return '';
    if (lists.length === 1) {
        return lists[0];
    }
    var res = [];
    for (var i = 0; i < lists.length; i = i + 2) {
        res.push(mergeCore(lists[i], lists[i + 1]));
    }
    if (i < lists.length) {
        res.push(lists[lists.length - 1]);
    }
    return mergeKLists(res.slice(0));
};
