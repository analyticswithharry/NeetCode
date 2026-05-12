// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 008 -- Maximum Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 4
// =============================================================
//
// QUESTION:
//   Given an integer array nums, find the contiguous subarray (containing
//   at least one number) which has the largest sum and return its sum.
//
//   Example:
//     Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
//     Output: 6   (subarray [4,-1,2,1])
// =============================================================

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best = nums[0], cur = nums[0];
        for (int i = 1; i < (int)nums.size(); ++i) {
            cur = max(nums[i], cur + nums[i]);
            best = max(best, cur);
        }
        return best;
    }
};

int main() {
    vector<int> v = {-2,1,-3,4,-1,2,1,-5,4};
    cout << Solution().maxSubArray(v) << endl;
}
