// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 064 -- Move Zeroes
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Move all 0s to the end while maintaining relative order. In-place.
//
//   Example: [0,1,0,3,12] -> [1,3,12,0,0]
// =============================================================

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <numeric>
#include <functional>
#include <cmath>
using namespace std;
class Solution { public:
    void moveZeroes(vector<int>& nums){
        int j=0; for (size_t i=0;i<nums.size();++i) if (nums[i]) swap(nums[i], nums[j++]);
    }
};
int main(){ vector<int> v={0,1,0,3,12}; Solution().moveZeroes(v); for (int x: v) cout<<x<<" "; cout<<endl; }
