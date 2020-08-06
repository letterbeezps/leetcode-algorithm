class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m+1))
        ans = []

        for cur in queries:
            ret = 0
            # 数据量不大，直接暴力吧
            for i in range(m):
                if P[i] == cur:
                    ret = i
                    break
            ans.append(ret)

            for i in range(ret, 0, -1):
                P[i] = P[i-1]
            P[0] = cur
        return ans