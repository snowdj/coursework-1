#!/usr/bin/env python
"""
Implementations of classic sequential container data structures:
Stacks, queues, double-ended queues, linked lists, priority queues, heaps.

For practical implementations or use cases:
  1. Python List is good to use as a stack.

  2. Stack, Linked Stack, Queue, Linked Queue and Double-Ended Queue (Deque)
     Use collections.deque, which is implemented as doubly linked array blocks.
     Source code:
       https://hg.python.org/cpython/file/3.6/Modules/_collectionsmodule.c

  3. Priority Queue and Binary Heap
     Use heapq module.
     Use a tuple (priority, object), or implement __cmp__ in your custom object.
       Ref: http://stackoverflow.com/questions/407734/a-generic-priority-queue-for-python  # noqa
     heapq doc section 8.5.2 explains how to implement adaptable PQ.
       https://docs.python.org/3.6/library/heapq.html
"""


from random import sample


class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass


class Underflow(Exception):
    """Error attempting to delete an element from an empty container.
    """
    pass


class Overflow(Exception):
    """Error attempting to insert an element to a full container.
    """
    pass


class Stack(object):
    """Array based stack with a specified capacity.
       Modified from DSAP code fragment 6.2. See the last paragraph, page 234.

    """
    def __init__(self, max_len):
        """Create an empty stack.
        """
        super(Stack, self).__init__()
        self.max_len = max_len
        self._data = [None] * max_len
        self._top = -1  # Top index, and current stack size

    def __len__(self):
        """Return the number of elements, or current size of stack.
        """
        return self._top + 1 if self._top >= 0 else 0

    def __str__(self):
        return str(self._data)

    @property
    def is_empty(self):
        """Return True if the stack is empty.
        """
        return self._top < 0

    @property
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.

        Note:
        Here S.top is different than CLRS 3ed, which is the same as self._top.
        """
        if self.is_empty:
            raise Empty('Stack is empty.')
        return self._data[self._top]

    def push(self, e):
        """
        Add element e to the top of the stack.
        Raise Overflow exception if the stack is full.
        """
        if self._top + 1 == self.max_len:
            raise Overflow('Stack overflow.')
        self._top += 1
        self._data[self._top] = e

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Underflow exception is the stack is empty.
        """
        if self.is_empty:
            raise Underflow('Stack underflow.')
        self._top -= 1
        return self._data[self._top + 1]


class Queue:
    """
    FIFO queue implementation using a Python list as underlying storage.
    DSAP code fragment 6.6, page 243.
    """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Create an empty queue.
        """
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def first(self):
        """
        Return, but do not remove the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """

        if self.is_empty:
            raise Empty('Queue is empty.')
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue, i.e. FIFO.
        Raise Empty exception if the queue is empty.
        """

        if self.is_empty:
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        # shrink the underlying array to half size, when the number of
        # elements falls below its capacity.
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of queue.
        :param e: New element.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self).

        :param cap: New capacity.

        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class LinkedStack:
    """
    LIFO stack implementation using a singly linked list for storage.
    DSAP code fragment 7.5, 7.6.
    """

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked list.
        """
        __slots__ = ('element', 'nxt')

        def __init__(self, element, next_node):
            self.element = element
            self.nxt = next_node

    def __init__(self):
        """Create an empty stack.
        """

        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack.
        """
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack.
        """
        self._head = self._Node(e, self._head)
        self._size += 1

    @property
    def top(self):
        """Return, but do not remove, the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty:
            raise Empty("Stack is empty.")
        return self._head.element

    def pop(self):
        """Remove and return the element from stack top, i.e. LIFO.
        Raise Empty exception if stack is empty.
        """
        if self.is_empty:
            raise Empty("Stack is empty.")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        return answer


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage.
       DSAP code fragment 7.7, 7.8.
    """

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked list.
        """
        __slots__ = ('element', 'nxt')

        def __init__(self, element, next_node):
            self.element = element
            self.nxt = next_node

    def __init__(self):
        """Create an empty queue.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue.
        """
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def first(self):
        """Return but do not remove the element at the front of the queue.
        """
        if self.is_empty:
            raise Empty("Queue is empty.")
        return self._head.element

    def dequeue(self):
        """Remove and return the first element of the queue, i.e. FIFO.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty:
            raise Empty("Queue is empty.")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty:
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue.
        """
        new_element = self._Node(e, None)
        if self.is_empty:
            self._head = new_element
        else:
            self._tail.nxt = new_element
        self._tail = new_element
        self._size += 1


class CircularQueue:
    """Queue implementation using circularly linked list for storage.
       DSAP code fragment 7.9, 7.10.
    """

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = ('element', 'nxt')

        def __init__(self, element, next_node):
            self.element = element
            self.nxt = next_node

    def __init__(self):
        """Create an empty queue.
        """
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def first(self):
        """Return, but do not remove, the first element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty:
            raise Empty("Queue is empty.")
        head = self._tail.nxt
        return head.element

    def dequeue(self):
        """Remove and return the first element of the queue, i.e. FIFO.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty:
            raise Empty("Queue is empty.")
        old_head = self._tail.nxt
        if self._size == 1:
            self._tail.nxt = None
        else:
            self._tail.nxt = old_head.nxt
        self._size -= 1
        return old_head.element

    def enqueue(self, e):
        """Add an element to the back of the queue.
        """
        if self.is_empty:
            new_node = self._Node(e, None)
            self._tail = new_node
            self._tail.nxt = new_node
        else:
            new_node = self._Node(e, self._tail.nxt)
            self._tail.nxt = new_node
            self._tail = new_node
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue.
        """
        if self._size > 0:
            self._tail = self._tail.nxt


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation.
    """

    class _Node:
        """Lightweight nonpublic class for storing a doubly linked node.
        """
        __slots__ = ('element', 'prev', 'nxt')

        def __init__(self, element, prev_node, next_node):
            self.element = element
            self.prev = prev_node
            self.nxt = next_node

    def __init__(self):
        """Create an empty list.
        """
        # Sentinels
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.nxt = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes, and return new node.
        """
        new_node = self._Node(e, predecessor, successor)
        predecessor.nxt = new_node
        successor.prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Delete non-sentinel node and return its element.
        """

        predecessor = node.prev
        successor = node.nxt
        predecessor.nxt = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        # node cannot be deleted in function, but only deprecated.
        node.prev = node.nxt = node.element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list.
    """

    def first(self):
        """Return, but do not remove the element at the front of the deque.
        """
        if self.is_empty:
            raise Empty("Deque is empty.")
        return self._header.nxt.element

    def last(self):
        """Return, but do not remove the element at the end of the deque.
        """
        if self.is_empty:
            raise Empty("Deque is empty.")
        return self._trailer.prev.element

    def insert_first(self, e):
        """Add an element to the front of the deque.
        """
        self._insert_between(e, self._header, self._header.nxt)

    def insert_last(self, e):
        """Add an element to the back of the deque.
        """
        self._insert_between(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty:
            raise Empty("Deque is empty.")
        return self._delete_node(self._header.nxt)

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        """
        if self.is_empty:
            raise Empty("Deque is empty.")
        return self._delete_node(self._trailer.prev)


def test_stack():
    stk = Stack(20)
    print("Empty stack:", stk)
    print("Is empty? {}. Max len: {}. Current len: {}".format(
        stk.is_empty, stk.max_len, len(stk)))

    s = sample(range(101), 12)
    print("Push: ", s)
    for e in s:
        stk.push(e)
        print("Pushed: {}, Current top: {}".format(e, stk.top))
    print("Stack: ", stk)

    for _ in range(5):
        print("Popped: {}, Current top: {}".format(stk.pop(), stk.top))
    print("Stack: ", stk)


if __name__ == '__main__':
    test_stack()
