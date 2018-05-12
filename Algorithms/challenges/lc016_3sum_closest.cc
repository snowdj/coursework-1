#include <vector>
#include <algorithm>
#include <cstdlib>

using std::vector;


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
      std::sort(nums.begin(), nums.end());
      int res = nums[0] + nums[1] + nums[2];
      for (unsigned i = 0; i != nums.size() - 2; i++)
        {
          unsigned j = i + 1, k = nums.size() - 1;
          while (j < k)
            {
              int sum = nums[i] + nums[j] + nums[k];
              if (sum == target) return sum;
              if (std::abs(sum - target) < std::abs(res - target)) res = sum;
              (sum < target) ? j++ : k--;
            }
        }
      return res;
    }
};
