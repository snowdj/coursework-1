#include <vector>

using std::vector;

class Solution {
  /* Scan array, and solve each by sorted 2-sum */
  
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
      vector<vector<int> > res;
      std::sort(nums.begin(), nums.end());
      
      for (unsigned k = 0; k != nums.size(); k++)
        {
          if (nums[k] > 0) break;  // scanning negatives only
          if (k > 0 && nums[k] == nums[k-1]) continue; // skip repetitions
          int target = -nums[k];
          int i = k + 1, j = nums.size() - 1;
          
          // two pointers scanning for sorted 2-sum problem
          while (i < j)
            {
              int sum = nums[i] + nums[j];
              if (sum == target)
                {
                  res.push_back(vector<int>{nums[k], nums[i], nums[j]});
                  while (i < j && nums[i+1] == nums[i]) i++;  // skip duplicates
                  while (i < j && nums[j-1] == nums[j]) j--;  // skip duplicates
                  i++; j--;
                }
              else if (sum < target) i++;
              else j--;
            }
        }
      return res;
    }
};
