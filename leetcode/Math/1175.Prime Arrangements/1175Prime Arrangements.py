class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        if n<3:
            return 1
        def fact(n):
            if n==1:
                return 1
            else:
                return n*fact(n-1)
        def isPrime(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        def Prime(n):
            count = 0
            for i in range(2, n+1):
                if isPrime(i):
                    count += 1
            return count
        
        a = Prime(n)
        b = n - a
        return (fact(a)*fact(b)%1000000007+1000000007)%1000000007