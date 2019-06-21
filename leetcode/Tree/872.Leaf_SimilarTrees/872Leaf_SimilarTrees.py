class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1 = self.findLeafList(root1, list());
        list2 = self.findLeafList(root2, list());
        return list1==list2
    
    def findLeafList(self, node: TreeNode, listNode: list) -> list:
        if (node.right == None and node.left == None): 
            listNode.extend([node.val])
        if node.left != None: listNode = self.findLeafList(node.left, listNode);
        if node.right != None: listNode = self.findLeafList(node.right, listNode);
        return listNode;

###################################
##########222222222222#############