// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 077 -- Find the Duplicate Number
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).
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
    int findDuplicate(vector<int>& nums){
        int slow = nums[0], fast = nums[0];
        do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
        slow = nums[0];
        while (slow != fast){ slow = nums[slow]; fast = nums[fast]; }
        return slow;
    }
};
int main(){ vector<int> a={1,3,4,2,2}, b={3,1,3,4,2};
    cout<<Solution().findDuplicate(a)<<" "<<Solution().findDuplicate(b)<<endl; }
