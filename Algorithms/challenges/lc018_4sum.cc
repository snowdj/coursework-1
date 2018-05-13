/*
Time: O(n^3)
Space: O(1)

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/

#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
      vector<vector<int>> res;
      unsigned n = nums.size();
      if (n < 4) return res;
      sort(nums.begin(), nums.end());

      for (unsigned i = 0; i != n - 3; i++)
        {
          if (i > 0 && nums[i] == nums[i-1]) continue;  // skip repetitions
          if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;  // too big
          if (nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;  // too small
          
          for (unsigned j = i+1; j != n - 2; j++)
            {
              if (j > i+1 && nums[j] == nums[j-1]) continue;  // skip repetitions
              if (nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;  // too big
              if (nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;  // too small
              
              int l = j + 1, r = n - 1;
              while (l < r)
                {
                  int sum = nums[l] + nums[r] + nums[i] + nums[j];
                  if (sum < target) l++;
                  else if (sum > target) r--;
                  else 
                    {
                      res.push_back(vector<int>{nums[i], nums[j], nums[l], nums[r]});
                      do l++; while (l < r && nums[l] == nums[l-1]);
                      do r--; while (l < r && nums[r] == nums[r+1]);
                    }
                }
            }
        }

      return res;
    }
};
