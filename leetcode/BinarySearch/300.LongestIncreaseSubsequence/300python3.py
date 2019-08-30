class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            if num > stack[-1]:
                stack.append(num)
            else:
                i, j = 0, len(stack)-1
                while i<j:
                    mid = i + j >> 1
                    if stack[mid] >= num:
                        j = mid
                    else:
                        i = mid+1
                stack[j] = num
        return len(stack)
        