import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        # 建立一个小顶堆 Transform a list into heap, in-place, in linear time
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums) # Pop and return the smallest item from the heap, maintaing the heap variant

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)  # pop the smallest and push the new val
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)