"""

5 3
1 2 100
2 5 100
3 4 100
 
Sample Output 0
200
 
Explanation 0
We perform the following sequence of m = 3 operations on list = {0, 0, 0, 0, 0}:
Add k = 100 to every element in the inclusive range [1, 2], resulting in list = {100, 100, 0, 0, 0}.
Add k = 100 to every element in the inclusive range [2, 5], resulting in list = {100, 200, 100, 100, 100}.
Add k = 100 to every element in the inclusive range [3, 4], resulting in list = {100, 200, 200, 200, 100}.
We then print the maximum value in the final list, 200, as our answer.
 
Sample Input 1
4 3
2 3 603
1 1 286
4 4 882
 
Sample Output 1
882
 
Explanation 1
We perform the following sequence of m = 3 operations on list = {0, 0, 0, 0}:
Add k = 603 to every element in the inclusive range [2, 3], resulting in list = {0, 603, 603, 0}.
Add k = 286 to every element in the inclusive range [1, 1], resulting in list = {286, 603, 603, 0}.
Add k = 882 to every element in the inclusive range [4, 4], resulting in list = {286, 603, 603, 882}.
We then print the maximum value in the final list, 882, as our answer.
"""


# Same as leetcode
from itertools import accumulate
n, m = map(int, input().split())
nums = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    nums[a-1] += k
    nums[b] -= k
print(max(accumulate(nums[:-1])))
