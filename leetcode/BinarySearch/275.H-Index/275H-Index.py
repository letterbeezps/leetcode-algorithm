class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l<r:
            mid = l+r+1 >> 1
            if citations[n-mid] >= mid:
                l = mid
            else:
                r = mid-1
        return l
        
        