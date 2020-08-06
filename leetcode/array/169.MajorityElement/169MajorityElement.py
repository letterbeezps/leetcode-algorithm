class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 普通方案，先排序，再取中间值。nlogn
        candidate, count = None, 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count > 0:
                count -= 1
            else:
                candidate, count = num, 1
        return candidate