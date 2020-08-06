class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 划动窗口、单调队列
        max_q, min_q = collections.deque(), collections.deque()
        ans = 0
        l = 0
        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans
