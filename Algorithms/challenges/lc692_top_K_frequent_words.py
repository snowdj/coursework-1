"""
Time: O(nlg(k)) for heap, O(n) worst O(nlg(n)) for bucket sorting.
Space: O(n)


Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
import collections
import heapq


# heap O(nlg(n))
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        most = collections.Counter(words).most_common(len(words))  # heap size is n
        freqtbl = collections.OrderedDict()
        for w, f in most:
            freqtbl.setdefault(f, []).append(w)
        for wlist in freqtbl.values():
            wlist.sort()
        return sum(freqtbl.values(), [])[:k]


# max heap O(nlg(k))
class Solution2:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        def heappush_max(heap, item):
            heap.append(item)
            heapq._siftdown_max(pq, 0, len(heap)-1)

        cnt = [(-f, w) for w, f in collections.Counter(words).items()]  # O(n)
        pq = []
        for entry in cnt:  # O(nlg(k))
            heappush_max(pq, entry)
            if len(pq) > k:
                heapq._heappop_max(pq)
        res = [heapq._heappop_max(pq)[1] for _ in range(k)]  # O(klg(k))
        return res[::-1]


# bucket sort O(n)
class Solution3:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = collections.Counter(words)
        bucket = [[] for _ in range(len(words)+1)]
        for w, f in cnt.items():
            bucket[f].append(w)
        res = []
        for wlist in reversed(bucket):
            wlist.sort()  # O(nlg(n)) in the worst case. Improve with Trie or min heap of size k.
            res += wlist
            if len(res) >= k:
                return res[:k]
