class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        hash = collections.defaultdict(int)
        for a in A:
            for b in B:
                hash[a+b] += 1
        for c in C:
            for d in D:
                res += hash[-c-d]
        return res