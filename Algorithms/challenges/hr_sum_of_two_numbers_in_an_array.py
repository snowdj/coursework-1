"""
Complete the function numberOfPairs that has 2 parameters- an array of integers a, and an integer k. The function must return an integer denoting the number of distinct pairs, (ai, aj) where i ≠ j, in a such that ai + aj = k.
 
Note: Pairs (ai, aj) and (aj, ai) are considered to be the same because they are both composed of the same 2 elements; however, while i ≠ j, the value of ai may be equal to aj. In addition, two pairs (ai, aj) and (ak, am) are considered to be the same if (ai ≡ ak and aj ≡ am) or (ai ≡ am and aj ≡ ak), meaning that both pairs are composed of different elements but the same integer values. See Explanation for more detail.
 
Constraints
1 ≤ n ≤ 5 × 105
0 ≤ a[i] ≤ 109
0 ≤ k ≤ 5 × 109
 
Input Format
The locked stub code assembles the following inputs from stdin and passes them to your function:
The first line contains an integer, n, denoting the size of a. Each of the n subsequent lines describes an element in a. The next line contains an integer, k.
 
Output Format
Your function must return the number of pairs of unique/distinct pairs in a having a sum equal to k.
 
Sample Input 1
6
1
3
46
1
3
9
47
 
Sample Output 1
1
 
Sample Input 2
7
6
6
3
9
3
5
1
12
 
Sample Output 2
2
 
Explanation
Sample Case 1:
a = [1, 3, 46, 1, 3, 9], k = 47
There are 4 pairs of unique elements where ai + aj = k:
(a0 = 1, a2 = 46)
(a2 = 46, a0 = 1)
(a2 = 46, a3 = 1)
(a3 = 1, a2 = 46)
In the list above, pairs 1 and 2 are equivalent, as are pairs 3 and 4 (because they both use the same i and j). In addition, all four pairs contain the same values. Thus, we only have 1 distinct pair, (1, 46), so our function returns 1.
 
Sample Case 2:
a = [6, 6, 3, 9, 3, 5, 1], k = 12
There are 5 unique pairs where ai + aj = k:
(a0 = 6, a1 = 6)
(a1 = 6, a0 = 6)
(a2 = 3, a3 = 9)
(a3 = 9, a2 = 3)
(a3 = 9, a4 = 3)
(a4 = 3, a3 = 9)
In the list above, pair 1 ≡ pair 2, pair 3 ≡ pair 4, and pair 5 ≡ pair 6 (because they all use the same i and j). In addition, pairs 3 through 6 all contain the same values. Thus, we only have 2 distinct pairs, (6, 6) and (3, 9), so our function returns 2.
"""


# 2-sum problem extended to non-unique combinations.
def numberOfPairs(a, k):
    tbl = {}
    res = set()
    for i, x in enumerate(a):
        y = k - x
        if y in tbl:
            res.add((x, y) if x <= y else (y, x))
        tbl[x] = i
    return len(res)
