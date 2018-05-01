#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;


class solution 
{
public:
  vector<int> twoSum(vector<int>& nums, int target)
  {
    unordered_map<int, int> tbl;
    vector<int> res;
    
    for (unsigned i = 0; i < nums.size(); i++) 
      {
        int y = target - nums[i];
        if (tbl.find(y) != tbl.end()) 
          {
            res.push_back(tbl[y]);
            res.push_back(i);
            return res;
          }
        tbl[nums[i]] = i;
      }
    return res;
  }
};

