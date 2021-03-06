"""
Time: O(n)
Space: O(n)

Suppose Andy and Doris want to choose a restaurant for dinner, and they both
have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index
sum. If there is a choice tie between answers, output all of them with no order
requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is
"Shogun" with index sum 1 (0+1).
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {r: i for i, r in enumerate(list1)}
        isum_max = len(list1) + len(list2)
        isum_min = isum_max
        ret = []
        for i, r in enumerate(list2):
            isum = i + d1.get(r, isum_max)
            if isum < isum_min:
                ret = [r]
                isum_min = isum
            elif isum == isum_min:
                ret.append(r)
        return ret
