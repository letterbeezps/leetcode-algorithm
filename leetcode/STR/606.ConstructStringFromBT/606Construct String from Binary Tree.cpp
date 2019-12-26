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
    string tree2str(TreeNode* t) {
        if (t==nullptr) return "";
        const string s = std::to_string(t->val);
        const string l = tree2str(t->left);
        const string r = tree2str(t->right);
        
        if (t->left == nullptr && t->right==nullptr)
            return s;
        if (t->right == nullptr)
            return s + "(" + l +")";
        return s + "(" + l +")" + "(" + r + ")";
    }
};