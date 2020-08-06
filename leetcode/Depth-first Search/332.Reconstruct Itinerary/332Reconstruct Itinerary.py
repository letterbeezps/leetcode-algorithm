class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 有向图的遍历，有多种遍历结果
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])  # 构成有向图
        for item in graph.items():
            item[1].sort()                      # 对每个起始节点能到达的子节点进行排序
        kStart = 'JFK'
        
        route_ = []
        def visit(src: str):
            dests = graph[src]
            while dests:
                dest = dests.pop(0)
                visit(dest)
            route_.append(src)
            
        visit(kStart)
        route_.reverse()
        return route_