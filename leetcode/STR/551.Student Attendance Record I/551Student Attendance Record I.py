class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == 'A': 
                A += 1
            if c == 'L':
                if i+2 < n and s[i:i+3] == 'LLL':
                    return False
        return A < 2