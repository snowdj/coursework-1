#include <vector>

using std::vector;

class Solution {
public:
    int maxArea(vector<int>& height) {
      int maxarea = 0;
      int l = 0, r = height.size() - 1;
      while (l < r) 
        {
          int h = std::min(height[l], height[r]);
          maxarea = std::max(maxarea, (r - l) * h);

          // keep moving shorter edge if next height is the same
          while (l < r && h == height[l]) l++;
          while (l < r && h == height[r]) r--;
        }
      return maxarea;
    }
};
