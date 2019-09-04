from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        set1, set2 = set(count1.keys()), set(count2.keys())
        
        set1 &= set2
        
        res = []
        for x in set1:
            
            for i in range(min(count1[x], count2[x])):
                res.append(x)
        return res