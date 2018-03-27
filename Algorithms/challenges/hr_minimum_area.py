"""
You are given n points in 2D plane, with integers coordinates, (x[0], y[0]), (x[1], y[1]), (x[2], y[2]), ..., (x[n - 1], y[n - 1]). Here x[i] is the x-coordinate of the ith point and y[i] is the y-coordinate of the ith point.
Your task is to draw a square by choosing any four points (may or may not from the set of n given points), such that the following three constraints are satisfied:
The x-coordinates and y-coordinates of the points should be integers only.
The sides of the square should be parallel to coordinate axis.
At least k of the given n points should lie strictly inside the square drawn. By strictly inside, we mean that any point on the sides of the square is not considered to be inside the square.
Complete the function minArea, in the editor below which has the following parameters:
Name	Type	Description
x	Integer array	An array of n integers denoting the x coordinates of the n points.
y	Integer array	An array of n integers denoting the y coordinates of the n points.
k	Positive integer	A positive integer representing the minimum number of points that should lie inside the square.
The function should return the minimum possible area of the square satisfying all the three constraints.
Input Format
The locked code in the editor reads the input and passes to the function.
The first line of the input is an integer, n, the total number of points.
Each of the next n subsequent lines contains an integer x[i] denoting the x-coordinate of the ith point.
The next line is the value of integer n.
Each of the next n subsequent lines contains an integer y[i] denoting the y-coordinate of the ith point.
The last line of the input contains the value of the integer, k.

Constraints
2 ≤ n ≤ 100
-109 ≤ x[i], y[i] ≤ 109, where 0 ≤ i ≤ n - 1
1 ≤ k ≤ n
 
Output Format
The locked code in the editor prints the return value of the function.
The function should return the possible minimum area of the square satisfying all the three constraints.
Sample Case 0
Sample Input
2
0
2
2
0
4
2
Sample Output
36
 
Explanation
The given points are:
(0, 0)
(2, 4)
Now we can choose following four points:
(-1, -1)
(-1, 5)
(5, 5)
(5, -1)
Thus we draw a square of side six, satisfying the three constraints given in the problem statement and the area of the square is possible minimum.
 

 
So, the function returns 36, as the area of the square is side x side (6 x 6 = 36).
 
Sample Case 1
Sample Input
2
0
3
2
0
7
2
 
Sample Output
81
 
Explanation
The given points are:
(0, 0)
(2, 7)
Now we can choose following four points:
(-1, -1)
(-1, 8)
(8, 8)
(8, -1)
Thus we draw a square of side nine, satisfying the three constraints given in the problem statement and the area of the square is possible minimum. So the function returns 81 (9 x 9).
"""


from itertools import combinations


# O(k * n^k)
def minArea(x, y, k):
    n = len(x)
    min_edge = float('inf')
    for comb in combinations(range(n), k):
        points = [(x[i], y[i]) for i in comb]
        points_x, points_y = zip(*points)
        edge = max(max(points_x) - min(points_x),
                   max(points_y) - min(points_y)) + 2
        min_edge = min(min_edge, edge)
    return min_edge ** 2


# O(n)  6/10 cases passed.
def minArea2(x, y, k):
    n = len(x)
    min_edge = float('inf')
    px = sorted(zip(x, y))
    py = sorted(zip(y, x))
    for i in range(n-k+1):
        min_edge = min(min_edge, max(abs(px[i+k-1][0] - px[i][0]), abs(px[i+k-1][1] - px[i][1])))        
    for i in range(n-k+1):
        min_edge = min(min_edge, max(abs(py[i+k-1][0] - py[i][0]), abs(py[i+k-1][1] - py[i][1]))) 
    return (min_edge + 2) ** 2


# O(n^3)
https://stackoverflow.com/questions/30951045/square-with-minimum-area-enclosing-k-points-among-given-n-points
https://ideone.com/139C7A
