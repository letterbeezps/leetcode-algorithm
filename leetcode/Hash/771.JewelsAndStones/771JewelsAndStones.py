class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Hash = collections.defaultdict(bool)
        res = 0
        for x in J:
            Hash[x] = True
        for x in S:
            if Hash[x]:
                res += 1
        return res