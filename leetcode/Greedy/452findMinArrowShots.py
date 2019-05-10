'''
典型的时间调度问题，两个气球a b没有交集的时候就是 a.end < b.start
所以先按照end排序，（结束时间排序）
如果a.end > b.start 那么 a b属于同一个区间
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda s: s[1])
        
        res = 0
        r = -2147483648
        if len(points) and points[0][0] == r:
            res += 1
        for x in points:
            if x[0] > r:
                r = x[1]
                res += 1
        return res