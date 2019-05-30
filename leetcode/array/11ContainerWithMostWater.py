class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2 :
            return 0
        area = 0
        left, right = 0, len(height)-1
        while left < right:
            new_area = (right-left) * min(height[left],height[right])
            area = max(new_area, area)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1
        #end_while
        return area