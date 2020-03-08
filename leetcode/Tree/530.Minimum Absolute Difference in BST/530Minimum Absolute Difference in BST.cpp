/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        min_diff_ = INT_MAX;
        prev_ = nullptr;
        inorder(root);
        return min_diff_;
    }
private:
    void inorder(TreeNode* root)
    {
        if (!root) return;
        inorder(root->left);
        if (prev_) min_diff_ = min(min_diff_, root->val - *prev_);
        prev_ = &root->val;
        inorder(root->right);
    }
    
    int* prev_;
    int min_diff_;
};