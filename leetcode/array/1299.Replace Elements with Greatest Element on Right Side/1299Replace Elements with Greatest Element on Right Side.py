class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n, m = len(arr), -1
        for i in range(n-1, -1, -1):
            t = arr[i]
            arr[i] = m
            m = max(m, t)
        return arr