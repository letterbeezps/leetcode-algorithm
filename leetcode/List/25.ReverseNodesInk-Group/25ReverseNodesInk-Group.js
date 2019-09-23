/*
 * @lc app=leetcode.cn id=25 lang=javascript
 *
 * [25] K 个一组翻转链表
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    var temp = head;
    for (var i = 1; i < k && temp !== null; i++) {
        temp = temp.next;
    }
    if (temp == null) return head;
    var t2 = temp.next;
    temp.next = null;
    var newHead = reverseList(head);
    var newTemp = reverseKGroup(t2, k);

    head.next = newTemp;
    return newHead;
};

function reverseList(head) {
    if (head == null || head.next == null) return head;
    var res = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return res;
}
