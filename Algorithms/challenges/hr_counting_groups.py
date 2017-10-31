"""
A 2D array, m, is an n × n matrix where each cell contains either the value 0 or the value 1. Any two cells (x1, y1) and (x2, y2) in m fall into the same group if |x1 − x2| + |y1 − y2| = 1 and both cells contain the value 1.
 
Complete the countGroups function in your editor. It has 2 parameters:
An n × n 2D array of integers, m, where the value of each element mi,j (where 0 ≤ i,j < n) is a binary integer (i.e., a 0 or 1).
An array of q integers, t, where the value of each element tk (where 0 ≤ k < q) is a group size for which you must find the number of groups in m.
 
Your function must go through each of the q integers in array t and, for each tk (where 0 ≤ k < q), find the number of groups in m having size tk. It must then add the result to index k of a q-element array of integers to be returned by the function (we'll call this array ret).
 
After finding the result for each element in t, your function must return the ret array. Recall from the above paragraph that this is a q-element array of integers where each element k (0 ≤ k < q) denotes the number of groups of size tk in array m.
 
Input Format
The locked stub code in your editor reads the following input from stdin and passes it to your function:
The first two lines both contain an integer, n, denoting the number of rows in array m.
The second line contains an integer, n, denoting the number of columns in array m.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains n space-separated binary integers describing the respective elements of row i in m.
The next line contains an integer, q, denoting the number of test cases.
Each line k of the q subsequent lines (where 0 ≤ k < q) contains an integer describing element k in array t.
 
Constraints
1 ≤ n ≤ 103
1 ≤ q ≤ n
1 ≤ tk ≤ n2
 
Output Format
Your function must return an array of integers where each element k denotes the number of groups of size tk present in array m. This is printed to stdout by the locked stub code in your editor.
 
Sample Input 1
10
10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 1 1 1
1 1 0 0 1 0 0 1 1 1
1 0 1 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
5
1
10
20
2
6
 
Sample Output 1
2
2
1
1
1
 
Sample Input 2
5
5
1 0 1 1 0
0 1 0 0 1
1 0 1 1 0
1 0 1 1 0
0 1 0 0 1
5
1
2
3
4
5
 
Sample Output 2
5
2
0
1
0
 
Explanation 
Sample Case 1:
t0 = 1: m has two groups of this size, so index 0 in our return array should contain the value 2.
t1 = 10: m has two groups of this size, so index 1 in our return array should contain the value 2.
t2 = 20: m has one group of this size, so index 2 in our return array should contain the value 1.
t3 = 2: m has one group of this size, so index 3 in our return array should contain the value 1.
t4 = 6: m has one group of this size, so index 4 in our return array should contain the value 1.
 
Sample Case 2:
t0 = 1: m has five groups of this size, so index 0 in our return array should contain the value 5.
t1 = 2: m has two groups of this size, so index 1 in our return array should contain the value 2.
t2 = 3: m has zero groups of this size, so index 2 in our return array should contain the value 0.
t3 = 4: m has one group of this size, so index 3 in our return array should contain the value 1.
t4 = 5: m has zero groups of this size, so index 4 in our return array should contain the value 0.
"""


from collections import defaultdict


def countGroups(m, t):
    M, N = len(m), len(m[0])
    cnt = defaultdict(int)
    visited = [[False] * N for _ in range(M)]

    def dfs(r, c):
        visited[r][c] = True
        ret = 1
        for i, j in zip((r, r, r-1, r+1), (c-1, c+1, c, c)):
            if not (i < 0 or i == M or j < 0 or j == N
                    or m[i][j] == 0 or visited[i][j]):
                ret += dfs(i, j)
        return ret

    for r in range(M):
        for c in range(N):
            if m[r][c] == 1 and not visited[r][c]:
                group_size = dfs(r, c)
                cnt[group_size] += 1
    return [cnt[tk] for tk in t]
