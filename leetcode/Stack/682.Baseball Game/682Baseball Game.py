class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for op in ops:
            if op == '+':
                s.append(s[-1] + s[-2])
            elif op == 'C':
                s.pop()
            elif op == 'D':
                s.append(s[-1]*2)
            else:
                s.append(int(op))
        return sum(s)