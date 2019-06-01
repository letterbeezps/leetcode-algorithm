class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return target
        nums.sort()
        delta = nums[0] + nums[1] + nums[2] - target
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums)-1
            while start < end:
                newdelta = nums[i] + nums[start] + nums[end] - target
                if newdelta == 0:
                    return target
                if abs(delta) > abs(newdelta):  # find the smallest delta
                    delta = newdelta
                if newdelta < 0:
                    start += 1
                else:
                    end -= 1
                    
        return target + delta