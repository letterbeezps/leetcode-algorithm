class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 贪心，区间覆盖
        '''
        把每一个区间按照起点排序，同时维护一下当前能到达的end的最大值
        选择新区间时：
            区间起点小于等于当前end
            该区间的newend尽可能大，
            用newend代替原来的end实现向前覆盖
        '''
        p = [] # [[start, end]]
        for i in range(n+1):
            p.append([max(0, i-ranges[i]), min(n, i+ranges[i])])
        p.sort()
        
        i, end, ans = 0, 0, 0
        while i <= n and end < n:
            next_end = 0
            while i <= n and p[i][0] <= end:
                next_end = max(next_end, p[i][1])
                
                i += 1
            if next_end == end:
                return -1
            ans += 1
            end = next_end
        return ans
        