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
    unordered_map<string, int> hash;
    vector<TreeNode*> ans;
    
    string dfs(TreeNode *u){
        if (!u) return "NULL";
        string left = dfs(u->left);
        string right = dfs(u->right);
        string s = to_string(u->val) + ',' + left + ',' + right;
        if (++hash[s] == 2) ans.push_back(u);
        return s;
    }
    
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        dfs(root);
        return ans;
    }
};