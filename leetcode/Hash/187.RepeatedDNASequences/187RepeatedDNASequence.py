class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        Hash = collections.defaultdict(int)
        res = []
        i = 0
        while i + 10 <= len(s):
            
            substr = s[i:i+10]
            Hash[substr] += 1
            if Hash[substr] == 2:
                res.append(substr)
            
            i += 1
            
        return res