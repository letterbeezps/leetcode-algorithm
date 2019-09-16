class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  #[[int]]
        
        if len(nums) < 4:
            return res
        l = len(nums)
        dic = collections.defaultdict(list)
        nums.sort()
        
        for i, a in enumerate(nums):
            for j in range(i+1, l):
                b = nums[j]
                dic[a+b].append([i,j])
        
        
        for i, c in enumerate(nums):
            for j in range(i+1, l):
                d = nums[j]
                key = target - c - d
                if key not in dic:
                    continue
                
                vector = dic[key]
                for item in vector:
                    if i <= item[1]:
                        continue  # 有重复
                    res_item = [nums[item[0]], nums[item[1]], c, d]
                    res_item.sort()
                    res.append(res_item)
        
        return list(set([tuple(t) for t in res]))