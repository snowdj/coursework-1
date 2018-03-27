"""
You are given two integers, l and r. Find the number of integers x such that l ≤ x ≤ r, and x is a Power Number.
A Power Number is defined as an integer that can be represented as sum of two powers, i.e.
x = ap + bq,
a, b, p and q are all integers, 
a, b ≥ 0, and
p, q > 1.
Complete the function countPowerNumbers which takes the following arguments :
Name	Type	Description
l	Positive integer	The lower range for finding power sum
r	Positive integer	The upper range for finding power sum
The above function should return the count of power numbers in the given range.

Constraints:
0 ≤ l ≤ r ≤ 5 ×106
Input Format:
The locked code stub in the editor reads the following input from stdin:
The first line contains the value of l. The next line contains the value of r.
Output Format:
Your function must return a single integer representing the required result. 
Sample Case 0
Sample Input
0
1
Sample Output
2
Explanation
0 and 1 both are Power Numbers.
0 = 02 + 02,
1 = 02 + 12.
Sample Case 1
Sample Input
25
30

Sample Output
5
Explanation
Except 30, all are Power Numbers.
25 = 52 + 02,
26 = 52  + 12,
27 = 33 + 02,
28 = 33 + 12,
29 = 52 + 22.
"""


# not finished
import math
def countPowerNumbers(l, r):
    pass


def dfs(x, larger_than):
    if x == 0:
        return True
    for N in range(2, int(math.log2(x+1))):
        for i in range(larger_than + 1, math.ceil(math.pow(x + 1, 1 / N))):
            if dfs(x - i ** N, i):
                print(x, i, N)
                return True
    return False
