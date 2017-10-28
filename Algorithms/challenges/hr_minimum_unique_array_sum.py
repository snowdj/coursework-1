"""
Given an array, arr, we want it to make it unique by incrementing any duplicate elements in arr such that the sum of arrunique's elements is minimal. In other words, if two or more elements in arr are not unique, we must increase the value of the duplicate element(s) to some other number(s) such that arr consists of unique elements that sum to a number that is as small as possible. For example, if arr = [3, 2, 1, 2, 7], then arrunique = [3, 2, 1, 4, 7] and its elements sum to a minimal value of 3 + 2 + 1 + 4 + 7 = 17.
 
Complete the getMinimumUniqueSum function in the editor below. It has one parameter: an array of n integers, arr. The function must return an integer denoting the sum of arrunique's elements.
 
Input Format
The first line contains an integer, n, denoting size of array arr.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing element i in array arr.
 
Constraints
1 ≤ n ≤ 2000
1 ≤ arri ≤ 3000
 
Output Format
The function must return an integer denoting the sum of arrunique's elements.
 
Sample Input 0
3
1
2
2
Sample Output 0
6
 
Explanation 0
arr = [1, 2, 2]
arr0 is unique, but arr1 and arr2 are duplicate elements. We increase the value of arr2 by 1 (the minimum amount we can increase the value by so that each element is unique) to get arrunique = [1, 2, 3]. We then return the sum of these elements, which is 1 + 2 + 3 = 6.
 
Sample Input 1
3
1
2
3
 
Sample Output 1
6
 
Explanation 1
arr = [1, 2, 3]
Each number in arr is unique, so we do not need to modify any of its elements (i.e., arr ≡ arrunique). We return the sum of all elements in the array, which is 1 + 2 + 3 = 6.
 
Sample Input 2
4
2
2
4
5
 
Sample Output 2
14
 
Explanation 2
arr = [2, 2, 4, 5]
Because arr0 and arr1 are both duplicates, we must increase one of the two elements in such a way that they are two unique elements having a minimal sum. When we do this, we get arrunique = [2, 3, 4, 5]. We then return the sum of these elements, which is 2 + 3 + 4 + 5 = 14.
"""


# Be careful with the duplicates that have >2 numbers, e.g., 1,2,2,2,3,3,3,7
def getMinimumUniqueSum(arr):
    a = sorted(arr)
    total = a[0]
    for i in range(1, len(a)):
        if a[i-1] >= a[i]:
            a[i] = a[i-1] + 1
        total += a[i]
    return total
