"""
a priori OA

nxn matrix
-1: wall
>=0: path
1: a diamond on the path

Walk from (0, 0) to (n-1, n-1) and come back. Find max number of diamonds you can pick up.
"""


def pickdiamond(mat):
    n = len(mat)

    # From (0, 0) to (n-1, n-1)
    dp = [0] * n
    path = [[0] * n for i in range(n)]  # 0: come from above  1: come from left
    for i in range(n):
        for j in range(n):
            #pdb.set_trace()
            if (i == 0 and j > 0 and mat[i][j-1] == -1) or\
               (j == 0 and i > 0 and mat[i-1][j] == -1) or\
               (i > 0 and j > 0 and mat[i][j-1] == -1 and mat[i-1][j] == -1):
                mat[i][j] = -1
            if mat[i][j] == -1:
                path[i][j] = -1
                continue
            if j > 0 and (i == 0 or dp[j-1] > dp[j]):
                path[i][j] = 1
            dp[j] = (mat[i][j] == 1) + max(dp[j], j > 0 and dp[j-1] or 0)
    # Remove diamonds along the best path
    i, j = n-1, n-1
    while i != 0 or j != 0:
        if mat[i][j] == 1:
            mat[i][j] = 0
        if path[i][j] == 0:
            i -= 1
        else:
            j -= 1
    diamonds = dp[n-1]

    # From (n-1, n-1) back to (0, 0)
    dp = [0] * n
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if (i == n-1 and j < n-1 and mat[i][j+1] == -1) or\
               (j == n-1 and i < n-1 and mat[i+1][j] == -1) or\
               (i < n-1 and j < n-1 and mat[i][j+1] == -1 and mat[i+1][j] == -1):
                mat[i][j] = -1
            if mat[i][j] == -1:
                continue
            dp[j] = (mat[i][j] == 1) + max(dp[j], j < n-1 and dp[j+1] or 0)
    diamonds += dp[0]

    return diamonds
