###Solution1
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # 前缀和，求和运算符是 异或
        n = len(arr)
        ans = 0
        pre_xor = [0] * (n+1)
        for i in range(n):
            # pre_xor[i] = arr[0]^ ... ^ arr[i-1]
            pre_xor[i+1] = pre_xor[i] ^ arr[i]
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    a = pre_xor[j] ^ pre_xor[i]
                    b = pre_xor[k+1] ^ pre_xor[j]
                    if a==b:
                        ans += 1
        return ans

###Solution2
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # 前缀和，求和运算符是 异或
        n = len(arr)
        ans = 0
        pre_xor = [0] * (n+1)
        for i in range(n):
            # pre_xor[i] = arr[0]^ ... ^ arr[i-1]
            pre_xor[i+1] = pre_xor[i] ^ arr[i]
        for i in range(n):
            for k in range(i+1, n):
                if pre_xor[k+1] == pre_xor[i]:
                    ans += k-i
        return ans