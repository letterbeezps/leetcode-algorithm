class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import heapq
        heap = []
        for i, item in enumerate(mat):
            heap.append([sum(item), i])
        # heapq.heapify(heap)
        res = []
        for item in heapq.nsmallest(k, heap):
            res.append(item[1])
        return res