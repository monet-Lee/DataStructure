import numpy as np 


def minPathSum_M_N(m):
    if (len(m) == 0) or (len(m[0]) == 0):
        return 0
    rows = len(m)
    cols = len(m[0])
    matdp = np.zeros((4,4))
    # print(matdp)
    matdp[0][0] = m[0][0]
    for i in range(1, rows):
        matdp[i][0] = matdp[i-1][0] + m[i][0]
    for j in range(1, cols):
        matdp[0][j] = matdp[0][j-1] + m[0][j]
    for i in range(1, rows):
        for j in range(1, cols):
            matdp[i][j] = min(matdp[i-1][j], matdp[i][j-1]) + m[i][j]
    return matdp[rows-1][cols-1]


def minPathSum_M(m):
    if (len(m)==0) or (len(m[0])==0):
        return 0
    rows = len(m)
    cols = len(m[0])
    arr = np.zeros(min(rows, cols))
    arr[0] = m[0][0]
    drctn = 1 if rows > cols else 0
    if drctn:
        # rows > cols 时，以 cols 大小作为数组长度，沿 x 方向遍历。
        # 第一行和第一列依旧特殊处理
        for i in range(1, cols):
            arr[i] = arr[i-1] + m[0][i]
        for j in range(1, cols):
            arr[0] = arr[0] + m[0][j]
            for i in range(1, rows):
                arr[j] = min(arr[j], arr[j-1]) + m[i][j]
        return arr[-1]
    else:
        for j in range(1, rows):
            arr[j] = arr[j-1] + m[j][0]
        for i in range(1, cols):
            arr[0] = arr[0] + m[0][i]
            for j in range(1, rows):
                arr[j] = min(arr[j-1], arr[j]) + m[j][i]
        return arr[-1]



if __name__ == "__main__":
    # mat = np.array([[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]])
    mat = np.array([[1, 3, 5, 9], [5, 0, 6, 1], [8, 8, 4, 0]])
    # flag = minPathSum_M_N(mat)
    flag = minPathSum_M(mat)
    print(flag)
