## 下界
### k头猪，0:没死，1:15分钟后死了 2:30分钟之后，3:45分钟之后， 4:60分钟之后
### 5^k种状态， 所以5^k >= n
### 设计方案，使得每种状态恰好对应每一个木桶，k位5进制数转换成10进制，对应每个木桶的标号

class Solution:
    def poorPigs(self, buckets: int, ToDie: int, ToTest: int) -> int:
        b = ToTest // ToDie + 1
        k, n = 0, 1
        while n < buckets:
            k += 1
            n *= b
        return k