"""
Design a class implementing Chrome Top Ten domains feature, with two methods:
    hit(domain)
    printTopTen()
"""


# Solution 1
# Maintain an internal list of (domain, hits) and binary search and insert
# O(nlg(n)) for hit(), O(1) for printTopTen()

# Solution 2
# Maintain an internal heapq
# O(lg(n)) for hit(), O(lg(n)) for printTopTen()

# Solution 3
# Maintain two hash tables for 1-10 and 11-.
# O(1) for both methods
from collections import defaultdict


class TopTen:
    def __init__(self):
        self._others = defaultdict(int)
        self._topten = defaultdict(int)

    def hit(self, domain):
        if len(self._topten) < 10:
            self._topten[domain] += 1
            return
        self._others[domain] += 1
        tenth_domain = min(self._topten, key=self._topten.get)
        tenth_hits = self._topten[tenth_domain]
        if tenth_hits < self._others[domain]:
            self._others[tenth_domain] = tenth_hits
            self._topten[domain] = self._others.pop(domain)

    def printTopTen(self):
        for d, h in self._topten.items():
            print(d, h)
