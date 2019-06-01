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
    vector<int> get_val(vector<TreeNode*> level) {
        vector<int> res;
        for (auto &u : level) {
            res.push_back(u->val);
        }
        return res;
    }
    
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        vector<TreeNode*> level;
        level.push_back(root);
        res.push_back(get_val(level));
        while (true) {
            vector<TreeNode*> newlevel;
            for (auto &u : level) {
                if (u->left) newlevel.push_back(u->left);
                if (u->right) newlevel.push_back(u->right);
            }
            if (newlevel.size()) {
                res.push_back(get_val(newlevel));
                level = newlevel;
            }
            else break;
        }
        return res;
    }
};