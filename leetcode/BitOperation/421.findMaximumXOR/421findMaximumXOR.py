'''
构造前缀树
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nodes = [[0,0]] # 用来存储每一个节点，每个节点有两个儿子0 和 1
                        # 先存储根节点
        for x in nums:
            p = 0  # p指向节点的下标
            for i in range(30, -1, -1):
                t = x >> i & 1  # t 取值 {0,1}
                if not nodes[p][t]:
                    nodes.append([0,0])
                    nodes[p][t] = len(nodes)-1  # 指向刚刚插入的节点
                p = nodes[p][t]
        #end_for 将所有的数以二进制形式插入前缀树
        
        res = 0
        for x in nums:
            p, xorv = 0, 0
            for i in range(30, -1, -1):
                t = x >> i & 1
                if nodes[p][1-t]:
                    p = nodes[p][1-t]
                    xorv += 1 << i
                else:
                    p = nodes[p][t]
            #end_for
            res = max(res, xorv)
        #end_for
        return res



##########################
############C++###########
##########################
class Solution {
public:
    struct Node {
        int son[2];
    };
    
    vector<Node> nodes;
    
    int findMaximumXOR(vector<int>& nums) {
        nodes.push_back(Node({0, 0}));
        
        for (auto x : nums)
        {
            int p = 0;
            for (int i=30; i>=0; i--)
            {
                int t = x >> i & 1;
                if(!nodes[p].son[t])
                {
                    nodes.push_back(Node({0, 0}));
                    nodes[p].son[t] = nodes.size() - 1;
                }
                p = nodes[p].son[t];
            }
        }
        
        int res = 0;
        for (auto x : nums) 
        {
            int p=0, xorv = 0;
            for (int i=30; i>=0; i--)
            {
                int t = x >> i & 1;
                if (nodes[p].son[!t])
                {
                    p = nodes[p].son[!t];
                    xorv += 1 << i;
                }
                else
                {
                    p = nodes[p].son[t];
                }
            }
            res = max(xorv, res);
        }
        return res;
    }
};