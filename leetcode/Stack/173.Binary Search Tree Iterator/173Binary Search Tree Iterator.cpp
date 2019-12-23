/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//非递归中序遍历
class BSTIterator {
public:
    stack<TreeNode *> stk;
    BSTIterator(TreeNode* root) {
        while (root)
        {
            stk.push(root);
            root = root->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        //动态遍历下一个节点
        auto t = stk.top();
        stk.pop();
        for (auto p = t->right; p; p=p->left)
        {
            stk.push(p);
        }
        return t->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stk.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */