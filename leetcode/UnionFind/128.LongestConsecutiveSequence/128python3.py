import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, L = 0, len(nums)
        used = collections.defaultdict(int)
        for x in nums:
            used[x] = 1    # 1代表未访问
        for x in nums:
            if used[x] == 2:   #2 代表以访问
                continue
            elif used[x] == 1:
                used[x] = 2
                left, right = x-1, x+1
                while used[left] == 1:
                    used[left] = 2
                    left -= 1
                while used[right] == 1:
                    used[right] = 2
                    right += 1
                res = max(res, right-left-1)
        return res


#############Time Limit Exceed##################
########## it worked at C plus plus ############
import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, L = 0, len(nums)
        used = collections.defaultdict(bool)
        for x in nums:
            if used[x]:
                continue
            used[x] = True
            left, right = x-1, x+1
            while left in used:
                used[left] = True
                left -= 1
            while right in used:
                used[right] = True
                right += 1
            res = max(res, right-left-1)
        return res