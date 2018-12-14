# -*- coding: utf-8 -*-
s = []
t = []

# 这是一道动态规划题
def numDictinct(s ,t):
    ls = len(s)
    lt = len(t) 
    # 定义一个二维数组
    dp = [[0]*(ls+1) for i in range(lt+1)]
    for j in range(ls+1):
        dp[0][j] = 1
    # 再动态规划中，每一步都要进行一次选择，但选择通常依赖子问题的解
    # 这也是动态规划与贪心算法的不同之处
    for i in range(1, lt+1):
        for j in range(1, ls+1):
            if s[j-1] == t[i-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    print(dp)
    print(dp[lt][ls])


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    numDictinct(s, t)