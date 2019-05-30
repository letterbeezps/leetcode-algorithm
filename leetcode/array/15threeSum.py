class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        result = []
        L_num = len(nums)
        if L_num < 3:
            return result
        num = sorted(nums)
        for i in range(L_num-2):
            if num[i] > 0: # 太牛批了，这个
                break
            j = i + 1
            if i > 0 and num[i] == num[i-1]:
                continue  # 这一步是为了排除重复的结果
            k = L_num - 1
            while j < k:
                if num[i] + num[j] + num[k] < target:
                    j = j + 1
                    while num[j] == num[j-1] and j < k:
                        j = j + 1
                elif num[i] + num[j] + num[k] > target:
                    k = k - 1
                    while num[k] == num[k+1] and j < k:
                        k = k - 1
                else:
                    print([num[i], num[j], num[k]])
                    result.append([num[i], num[j], num[k]])  # 将所得结果加到结果集中
                    j = j + 1
                    k = k - 1
                    while num[j] == num[j-1] and num[k] == num[k+1] and j < k:
                        j = j + 1
            # end while
        # end for
        return result