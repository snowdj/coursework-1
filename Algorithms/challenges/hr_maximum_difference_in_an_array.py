"""
The maximum difference between elements in some array, a, is defined as the largest difference between any a[i] and a[j] where i < j and a[i] < a[j]. For example, if a = [4, 1, 2, 3], the maximum difference would be a[3] − a[1] = 3 − 1 = 2 because this is the largest difference between any two elements satisfying the aforementioned criteria.
 
Complete the maxDifference function in the editor below. It has 1 parameter: an array of integers, a. It must return an integer denoting the maximum difference between any pair of elements in a; if no such number exists (e.g., if a is in descending order and all a[j] < a[i]), return −1 instead.
 
Input Format
Locked stub code in the editor reads the following input from stdin and passes it to the function:
The first line contains a single integer, n, denoting the number of elements in array a.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains a single integer describing element a[i].
 
Constraints
1 ≤ n ≤ 2 × 105
−106 ≤ a[i] ≤ 106 ∀ i ∈ [0, n − 1]
 
Output Format
The function must return an integer denoting the maximum difference in a. This is printed to stdout by locked stub code in the editor.
 
Sample Input 0
7
2
3
10
2
4
8
1
 
Sample Output 0
8
 
Explanation 0
n = 7, a = [2, 3, 10, 2, 4, 8, 1]
As a[2] = 10 is largest element in the array, we must find the smallest a[i] where 0 ≤ i < 2. This ends up being 2 at index i = 0.
We then calculate the difference between the two elements: a[2] − a[0] = 10 − 2 = 8, and return the result (8).
 
Note: While the largest difference between any two numbers in this array is 9 (between a[2] = 10 and a[6] = 1), this cannot be the maximum difference because the element having the smaller value (a[6]) must be of a lesser index than the element having the higher value (a[2]). As j = 2 is not less than i = 6, these elements cannot be used to calculate the maximum difference.
 
Sample Input 1
6
7
9
5
6
3
2
 
Sample Output 1
2
 
Explanation 1
n = 6, a = [7, 9, 5, 6, 3, 2]
The maximum difference returned by the function is a[1] − a[0] = 9 − 7 = 2, because 2 is the largest difference between any a[i] and a[j] satisfying the conditions that a[i] < a[j] and i < j.
"""


# Maximum Subarray problem. Same as lc053 and lc121.
# Note: output -1 instead of 0 for the case all numbers are the same, or descending array.
def maxDifference(a):
    ad = [a[i]-a[i-1] for i in range(1, len(a))]
    if all(x == 0 for x in ad):  # for corner case Test 13/14
        return -1
    max_here = max_sofar = -1
    for x in ad:
        max_here = max(x, max_here+x)
        max_sofar = max(max_sofar, max_here)
    return max_sofar
