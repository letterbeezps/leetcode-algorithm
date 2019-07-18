###########solution 1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(heap)
            
            for factor in [2,3,5]:
                if val*factor not in visited:
                    heapq.heappush(heap, val*factor)
                    visited.add(val*factor)
        
        
        return val

##################solution 2
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i2=i3=i5=0
        next2, next3, next5 = 2, 3, 5
        cur = 1
        
        for i in range(1, n):
            cur = min(next2, next3, next5)
            res.append(cur)
            if cur == next2:
                i2 += 1
                next2 = res[i2] * 2
            if cur == next3:
                i3 += 1
                next3 = res[i3] * 3
            if cur == next5:
                i5 += 1
                next5 = res[i5] * 5
                
        return cur