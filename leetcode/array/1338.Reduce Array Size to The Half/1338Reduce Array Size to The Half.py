class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        Len = Len_ = len(arr)
        res = 0
        counter = collections.Counter(arr)
        temp = sorted(counter.items(), key=lambda x : x[1], reverse=True)
        for k, v in temp:
            Len -= v
            res += 1
            if Len <= Len_ // 2:
                break
        return res