class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        keep, swap = [1001] * n, [1001] * n

        keep[0] = 0
        swap[0] = 1

        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1

            if B[i] > A[i-1] and A[i] > B[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)

        return min(keep[-1], swap[-1])