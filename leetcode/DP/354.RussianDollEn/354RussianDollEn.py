''' 1
Binary Search
宽度为主键排序，宽度相同按长度逆序排序
这样就变成关于长度的最长上升子序列的问题
'''
class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        
        # 宽度为主键排序，宽度相同按长度逆序排序
        nums.sort(key=lambda s: [s[0], -s[1]])
        q = collections.deque()  # 用来记录符合条件的信封长度值
        
        for item in nums:
            y = item[1]  # take the second
            if not q:
                q.append(y)
            q_last = q.pop()
            q.append(q_last)
            if y > q_last:
                q.append(y)  # 宽度肯定符合条件（已经排序好了），判断长度
            else:
                l, r = 0, len(q) - 1
                while l < r:  # 二分法查找，找到第一个大于等于y的索引
                    mid = l+r >> 1
                    if q[mid] >= y:
                        r = mid
                    else:
                        l = mid + 1
                #end_while
                q[l] = y  # 在找到的位置用y替换
            #end_for
        return len(q)

''' 2 Time Limit
dynamic programming
'''
class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        nums.sort()
        L = len(nums)
        res = 0
        dp = [1] * L
        for i in range(L):
            for j in range(i):
                if nums[j][0] < nums[i][0] and nums[j][1] < nums[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res