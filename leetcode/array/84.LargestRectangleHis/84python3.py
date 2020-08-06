

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left, right = [0]*n, [n+1]*n
        # for left
        stack = [] # heights_value, heights_index
        for i in range(n):
            
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1][1]
            stack.append([heights[i], i+1])
        #print(left)
        
        # for right
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1][1]
            stack.append([heights[i], i+1])
        #print(right)
        
        minn = 0
        for i in range(n):
            temp = heights[i] * (right[i]-left[i]-1)
            minn = max(temp, minn)
        return minn
            
        
        
        