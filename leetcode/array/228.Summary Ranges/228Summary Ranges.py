class Solution:
    
    def RangetoStr(self, st, ed):
        if st == ed:
            return str(st)
        else:
            return str(st)+'->'+str(ed)
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        st, ed = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > ed+1:
                res.append(self.RangetoStr(st,ed))
                st = ed = nums[i]
            else:
                ed += 1
        
        res.append(self.RangetoStr(st,ed))
        return res
        