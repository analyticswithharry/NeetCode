// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 010 -- Search Insert Position
// Category   : Binary Search
// Difficulty : Easy
// Study Plan : Day 5
// =============================================================
//
// QUESTION:
//   Given a sorted array of distinct integers and a target, return the
//   index if the target is found. If not, return the index where it would
//   be inserted in order. Must run in O(log n).
//
//   Example:
//     Input : nums = [1,3,5,6], target = 5    Output: 2
//     Input : nums = [1,3,5,6], target = 2    Output: 1
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
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < target) l = m + 1; else r = m;
        }
        return l;
    }
};

int main() {
    vector<int> v = {1,3,5,6};
    cout << Solution().searchInsert(v, 5) << endl;
    cout << Solution().searchInsert(v, 2) << endl;
}
