class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        超时答案
        j = len(nums)-1
        step = 0
        while j:
            lastindex = 0
            for i in range(j+1):
                if nums[i] + i >= j:
                    lastindex = i
                    break
            #print(lastindex)
            step += 1
            j = lastindex
        return step
        '''
        '''
        分段跳跃，用f[]表示跳到指定元素所需的最小步数，那么f[]的形式应该是个011111222333444555
        相同的最小步数可以看作一层，然后使用bfs来算
        '''
        if len(nums) == 1:
            return 0
        l, r = 0, 0
        step = 0
        while l <= r:
            max_r = 0
            for i in range(l, r+1):
                max_r = max(max_r, i+nums[i])
            l, r = r + 1, max_r
            step += 1
            if r >= len(nums)-1:
                break
        #end_while
        return step
        
                    