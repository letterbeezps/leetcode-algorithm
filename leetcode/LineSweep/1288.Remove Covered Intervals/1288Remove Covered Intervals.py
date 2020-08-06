class Solution:
    def removeCoveredIntervals(self, items: List[List[int]]) -> int:
        # 区间合并
        items.sort(key = lambda x: [x[0], -x[1]])
        # items.sort()
        
        r = -1
        ans = len(items)
        for item in items:
            if item[1] <= r:
                ans -= 1
            else:
                r = item[1]
        return ans
        