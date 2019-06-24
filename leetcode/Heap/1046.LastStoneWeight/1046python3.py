import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        # 要构建大顶堆
        # python默认小顶堆
        self.data = [-x for x in stones]
        heapq.heapify(self.data)
        while len(self.data) > 1:
            y = -heapq.heappop(self.data)
            x = -heapq.heappop(self.data)
            if x == y:
                continue
            else:
                heapq.heappush(self.data, x-y)
        if self.data:
            return -self.data[0]
        else:
            return 0