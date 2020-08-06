'''tricks:n = size of array
if there is no duplicate elements, nums is a permutation of [i in range(n)]
so, you can make ervery element as a index, and there is no collision
but with duplicates, collision indicate duplicate element
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        for x in nums:
            index = abs(x)
            if nums[index-1] < 0:
                res.append(index)
            else:
                nums[index-1] = -nums[index-1]
        return res
        