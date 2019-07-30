class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        the operate 'n-1' will elimiate the most rightside '1'
        """
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count