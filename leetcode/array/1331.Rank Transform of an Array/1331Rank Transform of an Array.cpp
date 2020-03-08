class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n=arr.size();
        vector<int> a(arr.begin(), arr.end());
        
        sort(a.begin(), a.end());
        
        a.resize(unique(a.begin(), a.end()) - a.begin());
        
        for (int i=0; i<n; i++)
        {
            arr[i] = lower_bound(a.begin(), a.end(), arr[i]) - a.begin() + 1;
        }
        return arr;
    }
};