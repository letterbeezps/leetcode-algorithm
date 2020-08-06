class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        # 图论题目，找连通分量
        graph = collections.defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        idx = []
        temp = []
        def dfs(cur: int):
            if cur in visited:
                return
            visited.add(cur)
            idx.append(cur)
            temp.append(s[cur])
            for nxt in graph[cur]:
                dfs(nxt)
                
        for i in range(len(s)):
            if i in visited:
                continue
            idx.clear()
            temp.clear()
            dfs(i)
            idx.sort()
            temp.sort()
            for k in range(len(idx)):
                s[idx[k]] = temp[k]
        return ''.join(s)
            