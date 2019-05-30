class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Hash = collections.defaultdict(int)
        for x in nums:
            Hash[x] += 1
            if Hash[x] > 1:
                return True
        return False