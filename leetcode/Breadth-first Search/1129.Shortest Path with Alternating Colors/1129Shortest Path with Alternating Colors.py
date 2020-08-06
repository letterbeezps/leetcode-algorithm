class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g_red = collections.defaultdict(list)
        g_blue = collections.defaultdict(list)
        
        for u, v in red_edges:
            g_red[u].append(v)
        for u, v in blue_edges:
            g_blue[u].append(v)
            
        # （node color） start (0, 0) or (0, 1)
        # 表示到达该节点node经过哪一种颜色的边
        # 0：红， 1: 蓝
        ans = [-1] * n
        seen_r = set()
        seen_b = set()
        
        q = collections.deque()
        q.append((0, 0))
        q.append((0, 1)) # 到达节点0有两种可能
        
        seen_r.add(0)
        seen_b.add(0)
        
        steps = 0
        while q:
            size = len(q)
            while size:
                p, is_red = q[0]
                q.popleft()
                ans[p] = min(ans[p], steps) if ans[p] >= 0 else steps
                edges = g_red if is_red else g_blue
                seen = seen_r if is_red else seen_b  # 只是引用
                for nxt in edges[p]:
                    if nxt in seen: continue
                    seen.add(nxt) # 已经访问过的没必要再访问了
                    q.append((nxt, 1-is_red))
                size -= 1
            steps += 1
        return ans
                
                
                
                
                
                