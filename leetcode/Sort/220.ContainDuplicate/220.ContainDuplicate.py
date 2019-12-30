class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or k < 1 or t < 0:
            return False
        
        n = len(nums)
        l = 0
        d = {nums[0] // max(1, t): nums[0]}
        for r in range(1, n):
            if r - l == k + 1:
                d.pop(nums[l] // max(1, t))  # slide window
                l += 1
            tmp = nums[r] // max(1, t)
            
            for key in {tmp-1, tmp, tmp+1}:
                if key in d and abs(d.get(key) - nums[r]) <= t:
                    return True
                
            d[tmp] = nums[r]
            
        return False