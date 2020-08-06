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
private:
    void preorder(TreeNode* root, int depth, vector<pair<long long, int>>& sum_count)
    {
        if (root == nullptr) return;
        if (depth >= sum_count.size()) sum_count.push_back({0,0});
        sum_count[depth].first += root->val;
        sum_count[depth].second ++;
        preorder(root->left, depth+1, sum_count);
        preorder(root->right, depth+1, sum_count);
    }
public:
    vector<double> averageOfLevels(TreeNode* root) {
        if (!root)
            return {};
        
        vector<pair<long long, int>> sum_count;
        vector<double> ans;
        
        preorder(root, 0, sum_count);
        
        for (const auto& p : sum_count)
        {
            ans.push_back(static_cast<double>(p.first)/p.second);
        }
        return ans;
    }
};