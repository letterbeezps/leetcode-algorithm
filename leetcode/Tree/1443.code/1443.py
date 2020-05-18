class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        # create graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        seen = [0] * n
        def dfs(cur):
            seen[cur] = 1 # visited cur
            total = 0
            for child in graph[cur]:
                if seen[child]:
                    continue
                cost = dfs(child)
                if cost > 0 or hasApple[child]:
                    total += 2 + cost
            return total
        return dfs(0)