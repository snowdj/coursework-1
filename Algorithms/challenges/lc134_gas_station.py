"""
Time: O(n)
Space: O(1)

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1

        start = 0
        bal = 0
        total = 0
        for i in range(len(gas)):
            bal += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if bal < 0:
                start = i+1
                bal = 0
        return start if total >= 0 else -1
