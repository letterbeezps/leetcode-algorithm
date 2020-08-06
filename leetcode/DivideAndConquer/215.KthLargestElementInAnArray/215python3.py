class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 10^8 o(n)
        def partition(a: List[int], left, right):
            pivot = a[left]
            i, j = left, right
            while i < j:
                while i < j and a[j] <= pivot:
                    j -= 1
                a[i] = a[j]

                while i < j and a[i] >= pivot:
                    i += 1
                a[j] = a[i]
            a[i] = pivot
            return i
        
        left, right = 0, len(nums)-1
        while True:
            pivot_index = partition(nums, left, right)
            print(nums)
            if pivot_index == k-1:
                return nums[k-1]
            elif pivot_index < k-1:
                left = pivot_index+1
            else:
                right = pivot_index-1