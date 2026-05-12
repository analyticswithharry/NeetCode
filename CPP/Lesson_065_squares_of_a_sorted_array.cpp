// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 065 -- Squares of a Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Given a sorted (non-decreasing) array, return an array of squares of each number, also sorted.
//
//   Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
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
    vector<int> sortedSquares(vector<int>& nums){
        int n=nums.size(), l=0, r=n-1, k=n-1; vector<int> out(n);
        while (l<=r){ if (abs(nums[l])>abs(nums[r])){ out[k--]=nums[l]*nums[l]; l++; } else { out[k--]=nums[r]*nums[r]; r--; } }
        return out;
    }
};
int main(){ vector<int> v={-4,-1,0,3,10}; for (int x: Solution().sortedSquares(v)) cout<<x<<" "; cout<<endl; }
