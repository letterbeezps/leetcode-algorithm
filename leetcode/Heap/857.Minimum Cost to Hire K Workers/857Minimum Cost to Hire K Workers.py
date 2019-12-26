'''
q'[0], q'[1],..., q'[k-1]
q'[0]*x, q'[1]*x,..., q'[k-1]*x

res = (q'[0] + q'[1] + ,..., + q'[k-1])*x

q[0]*x >= w[0] ==> x_0 >= w[0]/q[0]
x_i >= w[i]/q[i]

先把所有工人按照x_i排序
枚举 x = x_i 此时所有满足0,...,i的工人，再从这些工人里找到quality最小的k个工人，对每个x_i都有一个最优解
再集合所有x_i的最优解
# 找到最大的x_i，当确定x的时候，找到所有x[j] <= x的工人
'''

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        import heapq
        
        n = len(quality)
        workers = []  # [[]]
        for i in range(n):
            workers.append([wage[i]/quality[i], quality[i]])  # x_i = wage[i]/quality[i]
        workers.sort()
        
        heap = [] 
        heapq.heapify(heap) # 这是小根堆，我们需要大根堆
        res = 1e9
        sumn = 0
        
        for worker in workers:
            heapq.heappush(heap, -worker[1])
            sumn += worker[1]
            if len(heap) > K:
                sumn += heapq.heappop(heap)  # 堆里的数是负数，实则是减法
            if len(heap) == K:
                res = min(res, sumn*worker[0])
                
        return res
        
            