class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Set1 = set(nums1)
        Set2 = set(nums2)
        
        Set1 &= Set2
        
        return list(Set1)