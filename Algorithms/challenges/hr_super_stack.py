"""
Implement a simple stack that accepts the following commands and performs the operations associated with them:
push k: Push integer k onto the top of the stack.
pop: Pop the top element from the stack. It is guaranteed that this will not be called on an empty stack.
inc e k: Add k to each of the bottom e elements of the stack.
 
Complete the superStack function in the editor below. It has one parameter: an array of n strings, operations. The function must create an empty stack and perform each of the n operations in order and, after performing each operation, print the value of the stack's top element on a new line; if the stack is empty, print EMPTY instead.
 
Input Format
Locked stub code in the editor reads the following input from stdin and passes it to the function:
The first line contains an integer, n, denoting the number of operations to perform on the stack.
Each line i of the n subsequent lines contains a space-separated string describing operationsi.
 
Constraints
1 ≤ n ≤ 2 × 105
-109 ≤ k ≤ 109
1 ≤ e ≤ |S|, where |S| is the size of the stack at the time of the operation.
It is guaranteed that pop is never called on an empty stack.
 
Output Format
After performing each operation, print the value of the stack's top element on a new line; if the stack is empty, print EMPTY instead.
 
Sample Input 0
12
push 4
pop
push 3
push 5
push 2
inc 3 1
pop
push 1
inc 2 2
push 4
pop
pop
 
Sample Output 0
4
EMPTY
3
5
2
3
6
1
1
4
1
8
 
Explanation 0
The diagram below depicts the stack after each operation:

After each operation, we print the value denoted by Current Top on a new line.
 
In other words, we have an empty stack, S, we express as an array where the leftmost element is the bottom of the stack and the rightmost element is its top. We perform the following sequence of n = 12 operations as given in the operations array:
push 4: Push 4 onto the top of the stack, so S = [4]. We then print the top element, 4, on a new line.
pop: Pop the top element from the stack, so S = []. Because the stack is now empty, we print EMPTY on a new line.
push 3: Push 3 onto the top of the stack, so S = [3]. We then print the top element, 3, on a new line.
push 5: Push 5 onto the top of the stack, so S = [3, 5]. We then print the top element, 5, on a new line.
push 2: Push 2 onto the top of the stack, so S = [3, 5, 2]. We then print the top element, 2, on a new line.
inc 3 1: Add k = 1 to bottom e = 3 elements of the stack, so S = [4, 6, 3]. We then print the top element, 3, on a new line.
pop: Pop the top element from the stack, so S = [4, 6]. We then print the top element, 6, on a new line.
push 1: Push 1 onto the top of the stack, so S = [4, 6, 1]. We then print the top element, 1, on a new line.
inc 2 2: Add k = 2 to bottom e = 2 elements of the stack, so S = [6, 8, 1]. The top element is 1, so we print 1 after this operation.
push 4: Push 4 onto the top of the stack, so S = [6, 8, 1, 4]. We then print the top element, 4, on a new line.
pop: Pop the top element from the stack, so S = [6, 8, 1]. We then print the top element, 1, on a new line.
pop: Pop the top element from the stack, so S = [6, 8]. We then print the top element, 8, on a new line.
"""


def superStack(operations):
    stk = []
    for opstr in operations:
        op = opstr.split()
        if op[0] == 'push':
            stk.append([int(op[-1]), 0])
        elif op[0] == 'pop':
            last = stk.pop()
            if stk:
                stk[-1][1] += last[1]
        else:  # inc e k
            stk[int(op[1])-1][1] += int(op[2])
        print(sum(stk[-1]) if stk else "EMPTY")
