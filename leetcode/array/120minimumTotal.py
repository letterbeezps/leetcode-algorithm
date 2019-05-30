# -*- coding: utf-8 -*-
def nimimumTotal(triangle):
    """
    type: triangle list[list[int]]
    rtyep: int
    2
    | \
    3  4
    | \| \
    6  5  7
    | \| \| \
    4  1  8  3
    """
    LenDp = len(triangle)  # 二维数组的长度，即一维数组的个数
    if LenDp == 0:
        return 0
    Dp = [0] * LenDp
    # print(LenDp)
    Dp[0] = triangle[0][0]
    for i in range(1, LenDp):
        j = i
        while j>=0:
            if j == 0:
                Dp[j] = Dp[j] + triangle[i][j]
            elif j == i:
                Dp[j] = Dp[j-1] + triangle[i][j]
            else:
                Dp[j] = triangle[i][j] + (Dp[j-1] if Dp[j-1] < Dp[j] else Dp[j])
                                         # min([Dp[j-1], Dp[j]])
            
            j = j-1

    print(Dp)
    print(sorted(Dp)[0])


if __name__ == '__main__':
    triangle = [[2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]]
    
    nimimumTotal(triangle)