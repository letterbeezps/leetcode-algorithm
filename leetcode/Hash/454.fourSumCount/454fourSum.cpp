class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> hash;
        int res = 0;
        for (auto a : A)
            for (auto b : B)
                hash[a + b]++;
        for (auto c : C)
            for (auto d : D)
                res += hash[-c-d];
        return res;
    }
};