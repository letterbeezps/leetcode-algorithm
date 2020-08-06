class newTrip:
    def __init__(self,val, key):
        self.val = val
        self.key = key
    def __lt__(self,other):
        if self.val == other.val:
            return self.key > other.key
        else:
            return self.val < other.val
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        count = collections.Counter(words)
        
        heap = []
        heapq.heapify(heap)
        for key, val in count.items():
            heapq.heappush(heap, newTrip(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).key)
        # print(ans)
        return ans[::-1]