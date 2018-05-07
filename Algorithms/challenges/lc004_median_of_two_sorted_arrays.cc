#include <vector>

using std::vector;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        unsigned m = nums1.size(), n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2, nums1);

        vector<int>& A = nums1, B = nums2;
        unsigned mid = (m+n+1) / 2;
        unsigned lo = 0, hi = m;
        while (lo <= hi) 
          {
            unsigned i = (lo + hi) / 2;
            unsigned j = mid - i;
            if (i < m && B[j-1] > A[i])  // i is too small, increase i
              lo = i + 1;
            else if (i > 0 && A[i-1] > B[j])  // i is too big, decrease i
              hi = i -1;
            else  // i is perfect
              {
                int max_of_left;
                if (i == 0)
                  max_of_left = B[j-1];
                else if (j==0)
                  max_of_left = A[i-1];
                else
                  max_of_left = std::max(A[i-1], B[j-1]);

                if ((m+n) % 2 == 1)  // totally odd number of elements
                  return max_of_left;  // left side has 1 more than right side

                // find min value of right side
                int min_of_right;
                if (i==m)
                  min_of_right = B[j];
                else if(j==n)
                  min_of_right = A[i];
                else
                  min_of_right = std::min(A[i], B[j]);
                return (max_of_left + min_of_right) / 2.0;
              }
          }
        return -1;
    }
};
