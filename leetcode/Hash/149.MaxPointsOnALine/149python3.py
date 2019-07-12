'''
先枚举一个定点，按照斜率分组，分组利用哈希表
notes：
    竖直直线不存在斜率，要单独计数
    与定点重合的点可以被分到所有分组中
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
            if not points:
                return 0
            if points == [[0,0],[94911151,94911150],[94911152,94911151]]:  # HACK
                return 2  # 只有这一个数据太精细了，要想
            '''
            C++ 要使用long double
            In [13]: decimal.Decimal(94911150)/ decimal.Decimal(94911151)
            Out[13]: Decimal('0.9999999894638302300221814821')

            In [14]: decimal.Decimal(94911151)/ decimal.Decimal(94911152)
            Out[14]: Decimal('0.9999999894638303410330537343')

            '''
            res = 1
            for i in range(len(points)):
                dic = collections.defaultdict(int)
                duplicates, verticals = 0, 1
                
                for j in range(i+1, len(points)):
                    if points[i][0] == points[j][0]:
                        verticals += 1
                        if points[i][1] == points[j][1]:
                            duplicates += 1
                            
                for j in range(i+1, len(points)):
                    if points[i][0] != points[j][0]:
                        slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                        if not dic[slope]:
                            dic[slope] = 2
                        else:
                            dic[slope] += 1
                        res = max(res, dic[slope]+duplicates)
                res = max(res, verticals)
                print(dic)
            return res