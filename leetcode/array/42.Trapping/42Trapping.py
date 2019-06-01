class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        max = 0
        for i in range(l):
            if height[i] > height[max]:
                max = i  # find the hightest column of water
        
        water = 0
        peak = 0
        top = 0
        # approching the middle
        for i in range(max):  # 0 --> max
            if height[i] > peak:
                peak = height[i]
            else:
                water += peak - height[i]
                
        for i in range(l-1, max, -1):  # max <-- l
            if height[i] > top:
                top = height[i]
            else:
                water += top - height[i]
        
        return water