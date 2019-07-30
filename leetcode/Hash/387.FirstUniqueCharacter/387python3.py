class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = collections.Counter(s)
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1