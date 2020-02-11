class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cnt, num = 1, arr[0]
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                cnt += 1
            else:
                if cnt * 4 > n:
                    return num
                cnt = 1
                num = arr[i]
        return num
                