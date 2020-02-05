class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k:
            return False
        nums.sort()
        
        counter = collections.Counter(nums)
        
        for x in nums:
            if (counter[x] > 0):
                for j in range(x, x+k):
                    if counter[j] == 0:
                        return False
                    counter[j] -= 1
        return True