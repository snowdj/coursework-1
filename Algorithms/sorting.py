"""
Sorting algorithms and data structures
"""


import numpy as np
from random import randrange


def check_sort(s):
    """
    Check if sorting result is correct.
    """
    print("Sorting Result:\n", s)
    error = False
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            print("Error at {0}: {1} >= {2}".format(i, s[i-1], s[i]))
            error = True
    if not error:
        print("Sorting Correct!")


def insertion_sort(s):
    """
    Insertion-Sort algorithm in CRLS 3ed.
    """
    for j in range(1, len(s)):
        key = s[j]
        # Insert S[j] into the sorted sequence s[1..j-1]
        i = j - 1
        while i >= 0 and s[i] > key:
            s[i+1] = s[i]
            i -= 1
        s[i+1] = key


def merge_sort_inplace(s):
    """
    Inplace merge sort.
    Here inplace does not mean constant additional memory.
    Actually merge sort uses O(n) additional memory space.
    Modified from Code Fragment 12.2 and 12.3, DSAP page 543,544.

    :s: Python list.

    Note: This function does not work for numpy array input as np.array slice
          is still a reference, not a copy. It is needed to use np.copy to
          create subarrays s1 and s2.
    """

    # trivial case
    n = len(s)
    if n < 2:
        return

    # divide
    mid = n // 2
    s1 = s[:mid]  # slicing creates new list using new storage.
    s2 = s[mid:]

    # print("s1: ", s1)
    # print("s2: ", s2)

    # conquer
    merge_sort_inplace(s1)
    merge_sort_inplace(s2)

    # combine
    i = 0
    j = 0
    n1 = mid
    n2 = n - mid
    while (i+j) < n:
        if j == n2 or (i < n1 and s1[i] <= s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
    return


def merge_sort(s):
    """
    Merge sort returns new list.
    Modified from Code Fragment 12.2 and 12.3, DSAP page 543,544.

    :s: Python list.

    Note: This function does not work for numpy array input as np.array slice
          is still a reference, not a copy. It is needed to use np.copy to
          create subarrays s1 and s2.
    """

    # trivial case
    n = len(s)
    if n < 2:
        return s

    # divide
    mid = n // 2

    # conquer
    s1 = merge_sort(s[:mid])  # passing in slice creates new list (new storage)
    s2 = merge_sort(s[mid:])

    # combine
    i = 0
    j = 0
    n1 = mid
    n2 = n - mid
    while (i+j) < n:
        if j == n2 or (i < n1 and s1[i] <= s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

    return s


def merge_iter(src, dest, segment_start, subarray_size):
    """
    Merge the two subarrays in a segment of src into the corresponding
    positions in dest. Iterative (non-recursion) merging.
    Modified from Code Fragment 12.4, DSAP page 549.
    """

    s1_end = segment_start + subarray_size
    s2_end = min(segment_start + 2 * subarray_size, len(src))

    i, j, k = segment_start, s1_end, segment_start

    while i < s1_end and j < s2_end:
        if src[i] < src[j]:
            dest[k] = src[i]
            i += 1
        else:
            dest[k] = src[j]
            j += 1
        k += 1

    if i < s1_end:  # subarray 2 sorted earlier than subarray 1
        dest[k:s2_end] = src[i:s1_end]
    elif j < s2_end:  # subarray 1 sorted earlier than subarray 2
        dest[k:s2_end] = src[j:s2_end]


def merge_sort_iter(s):
    """
    Sort list S using merge-sort algorithm.
    Iterative (non-recursion) merging. Perform merge-sort bottom-up
    by going up tree level by level.
    Modified from Code Fragment 12.4, DSAP page 549.
    """

    n = len(s)
    logn = int(np.ceil(np.log2(n)))

    src, dest = s, [None] * n  # Create a temp list dest of same length of s.
    for subarray_size in (2**level for level in range(logn)):
        segment_size = 2 * subarray_size
        for segment_start in range(0, n, segment_size):
            merge_iter(src, dest, segment_start, subarray_size)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n]


def quicksort(s, randomized=True):
    """
    My quicksort implementation.
    """

    # trivial case
    if len(s) < 2:
        return s

    # Randomize. Exchange a random element with the last one.
    if randomized:
        rand_i = randrange(len(s))
        s[rand_i], s[-1] = s[-1], s[rand_i]

    # divide
    pivot = s[-1]
    i = -1  # boundary of two partitions. Last element of subarray <= pivot.
    for j in range(len(s)):  # scanner j. No need to increase j explicitly.
        if s[j] <= pivot:  # including pivot itself
            i += 1
            s[i], s[j] = s[j], s[i]
    # pivot is at i after partitioning.

    # conquer
    s1 = quicksort(s[:i])
    s2 = quicksort(s[i+1:])

    # combine
    return s1 + [pivot] + s2


def quicksort_inplace(s, start=None, end=None, randomized=True):
    """
    My inplace quicksort on s[start:end].
    To sort s inplace, the whole s list has to be passed in, instead of
    list slice; otherwise, Python creates a copy for the list slice, and
    then the original list would not be changed.

    :param start: Index of the first element. If None, start = 0.
    :param end:   Index of the end. If None, end = len(s).
    """

    if start is None:
        start = 0
    if end is None:
        end = len(s)

    # trivial case
    if (end - start) < 2:
        return

    # Randomize. Exchange a random element with the last one.
    if randomized:
        rand_i = randrange(start, end)
        s[rand_i], s[end-1] = s[end-1], s[rand_i]

    # divide
    pivot = s[end-1]
    i = start-1  # i is partition boundary, the last one of subarray <= pivot.
    for j in range(start, end):  # scanner j. No need to increase j explicitly.
        if s[j] <= pivot:  # including pivot itself
            i += 1
            s[i], s[j] = s[j], s[i]
    # pivot is at i after partitioning.

    # conquer
    quicksort_inplace(s, start, i)
    quicksort_inplace(s, i+1, end)

    # No need to combine for tail recursion
    return


def counting_sort(s):
    """
    Counting-Sort algorithm in CRLS 3ed.
    """

    if not all((isinstance(x, int) or isinstance(x, np.int64))
               and x >= 0 for x in s):
        print("All elements must be non-negative integers for counting sort.")
        return

    # Find the range of integer elements:
    k = max(s)

    # Initialize C and B arrays
    counting = [0] * (k+1)
    result = [None] * len(s)

    # Counting. counting array contains the number of element equal to index.
    for elts in s:
        counting[elts] += 1
    print("Counting Array: ", counting)

    # Accumulate counting array contains the number of elements <= index.
    for i in range(1, k+1):
        counting[i] += counting[i-1]
    print("Accumulated Counting Array: ", counting)

    # Insert elements into appropriate positions based on accumulated counting.
    for elts in s:
        result[counting[elts] - 1] = elts
        counting[elts] -= 1

    return result


def radix_sort_oneside(s, base=10):
    """
    Radix-Sort algorithm.
    This implementation uses bucket sort for each digit, instead of counting
    sort as in CRLS 3ed. The bucket-sort assumes inputs in [0, base-1], and
    each digit is appended to the corresponding bucket, so no need to do
    insertion sort, as in the Bucket-Sort in CRLS 3ed, which assumes inputs
    are real numbers in [0, 1).
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Radix_sort

    This function works for either non-negative list, or pure negative list,
    but not for mixed list. For a list of mixed negative and non-negative
    integers, run this function separately on negative and non-negative
    elements, and then combine the results.
    """

    assert all(isinstance(x, (int, np.int64)) for x in s),\
        "All elements of input must be integers for radix sort."

    assert all(x >= 0 for x in s) or all(x < 0 for x in s),\
        ("All elements of input must all non-negative,"
         " or pure negative integers.")

    longest_elets = max(abs(max(s)), abs(min(s)))
    maxlen = len(np.base_repr(longest_elets, base))

    for k in range(maxlen):  # loop over digits from least to most significant
        # List of lists, length of base, e.g. 10 for base decimals
        buckets = [[] for i in range(base)]

        # Loop over all elements, and place each element in corresponding bin
        # according to the current digit.
        for elts in s:
            current_digit = elts // base**k  # shift right for 1 digit
            index = current_digit % base  # extract the last digit
            buckets[index].append(elts)

        # Flat out buckets to a list
        s = [e for bucket in buckets for e in bucket]

    return s


def radix_sort(s, base=10):
    """
    This function separates s into pure negative and non-negative parts, and
    call radix_sort_oneside() for each. Return the combined results.
    """

    assert all(isinstance(x, (int, np.int64)) for x in s),\
        "All elements must be integers for radix sort."

    ns = [e for e in s if e < 0]
    ps = [e for e in s if e >= 0]

    if not ps:
        return radix_sort_oneside(ns, base)
    elif not ns:
        return radix_sort_oneside(ps, base)
    else:
        return radix_sort_oneside(ns, base) + radix_sort_oneside(ps, base)


def bucket_sort(s):
    """
    Bucket-Sort algorithm in CRLS 3ed, page 201.
    This function takes real numbers in [0,1).
    """

    assert all(0 <= x < 1 for x in s), "Bucket-Sort assumes numbers in [0, 1)."

    n = len(s)
    buckets = [[] for i in range(n)]

    for elts in s:
        index = int(np.floor(n * elts))
        buckets[index].append(elts)

    for b in buckets:
        insertion_sort(b)

    return [x for b in buckets for x in b]


def randomized_select(s, i, start=None, end=None):
    """
    Randomized-Select algorithm, CRLS 3ed, page 216.

    :param s: Input list.
    :param i: [1, len(s)]. Order statistic, or the i-th smallest element.
    :returns: The i-th smallest element.
    :rtype: A number, the same as original.

    """
    if start is None:
        start = 0
    if end is None:
        end = len(s)

    assert 1 <= i <= (end-start), "Parameter i is out of input range."

    # Randomized pivot
    rand_i = randrange(start, end)
    s[end-1], s[rand_i] = s[rand_i], s[end-1]

    # Divide (partition)
    pivot = s[end-1]
    # print("start = {}, end = {}, pivot = {}, ".format(start,end,pivot))
    # print("Unpartitioned s: ", s)
    q = start-1
    for j in range(start, end):
        if s[j] <= pivot:  # including exchange pivot.
            q += 1
            s[q], s[j] = s[j], s[q]
    # pivot is at q after partitioning.

    k = q - start + 1  # s[q] is the k-th order statistic.
    # print("Partitioned s: ", s)
    # print("q = {}, s[q] = {}, k = {}".format(q, s[q], k))
    if k == i:
        return s[q]
    elif i < k:
        return randomized_select(s, i, start, q)
    else:
        return randomized_select(s, i-k, q+1, end)


def randomized_select_iter(s, i):
    """
    Iterative version of Randomized-Select, CRLS 3ed, page 216.

    :param s: Input list.
    :param i: [1, len(s)]. Order statistic, or the i-th smallest element.

    """
    while s:  # loop as long as s is not empty
        # Randomized pivot
        rand_i = randrange(len(s))
        s[-1], s[rand_i] = s[rand_i], s[-1]

        # Divide (partition)
        pivot = s[-1]
        print("pivot = {}, ".format(pivot))
        print("Unpartitioned s: ", s)
        q = -1
        for j in range(len(s)):
            if s[j] <= pivot:  # including exchange pivot.
                q += 1
                s[q], s[j] = s[j], s[q]
                # pivot is at q after partitioning.

        k = q + 1  # s[q] is the k-th order statistic.
        print("Partitioned s: ", s)
        print("q = {}, s[q] = {}, k = {}".format(q, s[q], k))
        if k == i:
            return s[q]
        elif i < k:
            s = s[:q]
        else:
            s = s[q+1:]
            i = i - k
