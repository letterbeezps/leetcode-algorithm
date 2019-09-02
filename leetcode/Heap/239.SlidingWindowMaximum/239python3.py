class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        
        j = 0
        for i, num in enumerate(nums):
            
            while dq and nums[dq[0]] <= num:
                dq.popleft()
            dq.appendleft(i)
            
            if i-j+1 > k:
                
                if dq[-1] <= j:
                    dq.pop()
                j += 1
            
            if i-j+1 == k:
                res.append(nums[dq[-1]])
        return res
                