class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        toMax = 1
        aux = [[1, 1] for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            maxlength, count = 1, 1
            for j in range(i):
                l, c = aux[j]
                if nums[j] < nums[i]:
                    if l+1 == maxlength:
                        count += c
                    elif l+1 > maxlength:
                        maxlength = l+1
                        count = c
                        
            toMax = max(toMax, maxlength)
            aux[i] = [maxlength, count]
        ans = 0
        for a in aux:
            if a[0] == toMax:
                ans += a[1]
        return ans