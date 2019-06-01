class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda s: s[0]-s[1])
        n = len(costs)
        res = 0
        for i in range(n):
            if i < n//2:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res