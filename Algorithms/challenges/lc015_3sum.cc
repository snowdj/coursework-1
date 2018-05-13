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
          if (k > 0 && nums[k] == nums[k-1]) continue; // skip repetitions
          if (nums[k] > 0) break;  // scanning negatives only

          int target = -nums[k];
          int i = k + 1, j = nums.size() - 1;
          
          // two pointers scanning for sorted 2-sum problem
          while (i < j)
            {
              int sum = nums[i] + nums[j];
              if (sum < target) i++;
              else if (sum > target) j--;
              else
                {
                  res.push_back(vector<int>{nums[k], nums[i], nums[j]});
                  do i++; while (i < j && nums[i] == nums[i-1]);  // skip duplicates
                  do j--; while (i < j && nums[j] == nums[j+1]);  // skip duplicates
                }
            }
        }
      return res;
    }
};
