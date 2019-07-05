class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int p1=0, p2=0;
        int count=0, loop=(m+n)/2+1;
        int value=0, pre=0;
        while(true){
            value = 0;
            if(p1<m && p2<n){
                if(nums1[p1]<nums2[p2])
                    value = nums1[p1++];
                else
                    value = nums2[p2++];
            }else if(p1>=m && p2<n){
                value = nums2[p2++];
            }else if(p1<m && p2>=n){
                value = nums1[p1++];
            }else
                break;
            count++;
            if(count == loop){
                if((m+n)%2)
                    return value;
                else
                    return (pre+value)/2.0;
            }
            pre = value;
        }
        return 0;
    }
};    