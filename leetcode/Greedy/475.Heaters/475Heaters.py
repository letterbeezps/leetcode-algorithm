'''
houses  : 
每一个房子的最下半径取决于离他左右两个相邻的热点
所以要先找到该 房子 右边第一个 热点，
如果找不到，那么该房子的 r 就取决于自己最左边的热点
如果第一个热点位置就在该房子的右边，就取决于该房子最右边的热点
其它情况：左右两边最近的热点
heaters :
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        houses.sort()
        heaters.sort()
        r, j, temp = 0, 0, 0
        for i in range(len(houses)):
            if abs(houses[i]-heaters[j]) > r:
                while j < n and heaters[j] < houses[i]:
                    j += 1
                if j == n:
                    temp = houses[i] - heaters[j-1]
                    j -= 1
                elif j == 0:
                    temp = heaters[j] - houses[i]
                elif heaters[j] > houses[i]:
                    temp = min(heaters[j]-houses[i], houses[i]-heaters[j-1])
                r = temp if temp > r else r
                #end_if
        return r