"""
In an array of integers, we consider a pair of elements, (a, b), to be a valid pair if a ≤ b. Two valid pairs, (a, b) and (c, d), are considered to be different pairs if any of the following two conditions are true:
a ≠ c and b ≠ d
a ≠ d and b ≠ c
Given an array of integers and an integer value, k, we want to know the total number of valid (a, b) pairs in the array that satisfy a + k = b.
For example, the array [1, 1, 1, 2] has two different valid pairs: (1, 1) and (1, 2); note that the three possible instances of pair (1, 1) count as a single valid pair, as do the three possible instances of pair (1, 2). If k = 1, then this means we have a total of 1 valid pair as only pair (1, 2) satisfies a + k = b ⇒ 1 + 1 = 2.
Complete the function in the editor below. It has the following parameters:
Name	Type	Description
numbers	integer array	An array of n integers to check.
k	integer	A valid pair must satisfy a + k = b.
The function must return an integer denoting the count of valid (a, b) pairs in the numbers array that have a difference of k (i.e., where a + k = b).
Input Format
The first line contains an integer, n, denoting the number of elements in the numbers array.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing numbersi.
The last line contains an integer, k.
Constraints
2 ≤ n ≤ 2 × 105
0 ≤ numbersi ≤ 109, where 0 ≤ i < n
0 ≤ k ≤ 109
Output Format
Return an integer denoting the total number of valid pairs in the numbers array that have a difference of k.
Sample Case 0
Sample Input
6
1
1
2
2
3
3
1
Sample Output
2
Explanation
There two valid pairs in [1, 1, 2, 2, 3, 3] that have a difference of k = 1:
(1, 2)
(2, 3)
Thus, the function returns 2.
Sample Case 1
Sample Input
6
1
2
3
4
5
6
2
Sample Output
4
Explanation
There are four valid pairs in [1, 2, 3, 4, 5, 6] that have a difference of k = 2:
(1, 3)
(2, 4)
(3, 5)
(4, 6)
Thus, the function returns 4.
Sample Case 2
Sample Input
6
1
2
5
6
9
10
2
Sample Output
0
Explanation
No valid (a, b) pair exists in [1, 2, 5, 6, 9, 10] that satisfies b − a = k = 2, so the function returns 0.
"""


# 2-pointers, fast and slow.
def countPairs(numbers, k):
    n = len(numbers)
    nums = sorted(numbers)
    cnt = 0
    i, j = 0, 1
    while i < n:
        a = nums[i]
        while j < n and nums[j] < a + k:
            j += 1
        if j < n and nums[j] == a + k:
            cnt += 1
        while i < n and nums[i] == a:
            i += 1
    return cnt
