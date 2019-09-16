class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 先构建好dandiaoxulie，在用哈希表把Next Greater存储下来
        nums2.reverse()
        stack = []
        dic = {}
        for num in nums2:
            dic[num] = -1
            
        for num in nums2:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            stack.append(num)
            
        res = []
        for n in nums1:
            res.append(dic[n])
        return res
        
                