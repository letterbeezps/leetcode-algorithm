/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2) {
    let carry = 0;
    let result = new ListNode(0);
    let currentResult,
        currentNode = result;
    while (l1 || l2 || carry) {
        if (!l2) {
            l2 = new ListNode(0);
        }
        if (!l1) {
            l1 = new ListNode(0);
        }
        currentResult = carry + l1.val + l2.val;
        if (currentResult / 10 >= 1) {
            carry = 1;
            currentNode.next = new ListNode(currentResult % 10);
        } else {
            currentNode.next = new ListNode(currentResult);
            carry = 0;
        }
        currentNode = currentNode.next;
        l1 = l1.next;
        l2 = l2.next;
    }

    return result.next;
};
