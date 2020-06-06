class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n 
        q = collections.deque()

        dp[0] = nums[0]
        ans = nums[0]
        q.append(0) # 当前最大值的下标是 0
        for i in range(1, n):
            while q and i-q[0] > k:
                q.popleft()

            dp[i] = max(nums[i], dp[q[0]] + nums[i])
            ans = max(ans, dp[i])

            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        return ans