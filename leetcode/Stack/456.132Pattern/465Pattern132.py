# first find the max ak, j < k and aj > ak
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ak = float('-inf')
        stack = []
        nums.reverse()
        
        for num in nums:
            if num < ak:
                return True
            while stack and stack[-1] < num:
                ak = max(ak, stack[-1])
                stack.pop()
                
            stack.append(num)
            
        return False