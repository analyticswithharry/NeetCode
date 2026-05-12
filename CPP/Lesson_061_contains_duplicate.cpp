// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 061 -- Contains Duplicate
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Given an integer array nums, return true if any value appears at least twice.
//
//   Example: [1,2,3,1] -> true; [1,2,3,4] -> false
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
    bool containsDuplicate(vector<int>& nums){
        unordered_set<int> s;
        for (int n: nums) if (!s.insert(n).second) return true;
        return false;
    }
};
int main(){ vector<int> a={1,2,3,1}, b={1,2,3,4};
    cout<<Solution().containsDuplicate(a)<<" "<<Solution().containsDuplicate(b)<<endl; }
