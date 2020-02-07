class Solution:
    def calc(self, v, arr):
        s = 0
        for x in arr:
            s += min(v, x)
        return s
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l, r = 0, max(arr)
        
        while l<r:
            mid = l+r >> 1
            if self.calc(mid, arr) < target:
                l = mid+1
            else:
                r = mid
        # 这里求出的 mid 是满足合大于等于target的最小值
        # 不是合最接近target的mid
        if abs(self.calc(l-1, arr)-target) <= abs(self.calc(l, arr)-target):
            return l-1
        return l
        