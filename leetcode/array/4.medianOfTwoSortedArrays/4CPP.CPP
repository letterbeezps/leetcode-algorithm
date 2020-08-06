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

/////////////
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int total = nums1.size() + nums2.size();
        if (total % 2 == 0)
        {
            int left = findKthNumber(nums1, 0, nums2, 0, total / 2);
            int right = findKthNumber(nums1, 0, nums2, 0, total / 2 + 1);
            return (left + right) / 2.0;
        }
        else
        {
            return findKthNumber(nums1, 0, nums2, 0, total / 2 + 1);
        }
    }

    int findKthNumber(vector<int> &nums1, int i, vector<int> &nums2, int j, int k)
    {
        if (nums1.size() - i > nums2.size() - j) return findKthNumber(nums2, j, nums1, i, k);
        if (nums1.size() == i) return nums2[j + k - 1];
        if (k == 1) return min(nums1[i], nums2[j]);
        int si = min(i + k / 2, int(nums1.size())), sj = j + k / 2;
        if (nums1[si - 1] > nums2[sj - 1])
        {
            return findKthNumber(nums1, i, nums2, sj, k - k / 2);
        }
        else
        {
            return findKthNumber(nums1, si, nums2, j, k - (si - i));
        }
    }
};