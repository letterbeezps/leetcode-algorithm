class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        dx = {'U': -1, 'D': 1, 'L': 0, 'R':0}
        dy = {'U': 0, 'D': 0, 'L': -1, 'R':1}
        for c in moves:
            x += dx[c]
            y += dy[c]
        return x == 0 and y == 0
        
        