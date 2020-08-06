from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(type(count.get))
        res = heapq.nlargest(k, count.keys(), key=count.get)
        return res