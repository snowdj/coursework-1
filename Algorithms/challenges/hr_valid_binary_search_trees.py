"""
A binary tree is a multi-node data structure where each node has, at most, two child nodes and one stored value. It may either be:
An empty tree, where the root is null.
A tree with a non-null root node that contains a value and two subtrees, left and right, which are also binary trees.
 
A binary tree is a binary search tree (BST) if all the non-null nodes exhibit two properties:
Each node's left subtree contains only values that are lower than its own stored value.
Each node's right subtree contains only values that are higher than its own stored value.
 
A pre-order traversal is a tree traversal method where the current node is visited first, then the left subtree, and then the right subtree. The following pseudocode parses a tree into a list using pre-order traversal:
If the root is null, output the null list.
For a non-null node:
Make a list, left, by pre-order traversing the left subtree.
Make a list, right, by pre-order traversing the right subtree.
Output the stored value of the non-null node, append left to it, then append right to the result.
For more detail, see the diagram in the Explanation section below.
 
Given q queries where each query consists of a list of numbers, determine if the sequence of numbers describes the pre-order traversal of a binary search tree (BST). For each query, print YES on a new line if its list describes a valid pre-order traversal of a BST; otherwise, print NO.
 
Input Format
The first line contains an integer, q, denoting the number of queries.
The 2·q subsequent lines describe each query over two lines:
The first line contains an integer, n, denoting the number of nodes in the tree.
The second line contains a list of n distinct space-separated integers in the inclusive range [1, n] describing a pre-order traversal of a binary tree.
 
Constraints
1 ≤ q ≤ 10
1 ≤ n ≤ 100
 
Output Format
For each query, print YES on a new line if the query describes the pre-order traversal of a valid BST; otherwise, print NO instead.
 
Sample Input
5
3
1 3 2
3
2 1 3
6
3 2 1 5 4 6
4
1 3 4 2
5
3 4 5 1 2
 
Sample Output
YES
YES
YES
NO
NO
"""


for _ in range(int(input())):
    n = int(input())
    tree = list(map(int, input().split()))

    def dfs(tree):
        if not tree:
            return True
        n = len(tree)
        root = tree[0]
        i = 1
        left, right = [], []
        while i < n and tree[i]<root:
            left.append(tree[i])
            i += 1
        while i < n and tree[i]>root:
            right.append(tree[i])
            i += 1
        return i == n and dfs(left) and dfs(right)
    res = dfs(tree)
    print({True: 'YES', False: 'NO'}[res])
