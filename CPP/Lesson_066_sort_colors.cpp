// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 066 -- Sort Colors
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0,1,2 in-place. Dutch National Flag.
//
//   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
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
    void sortColors(vector<int>& nums){
        int l=0,m=0,r=(int)nums.size()-1;
        while (m<=r){
            if (nums[m]==0) swap(nums[l++], nums[m++]);
            else if (nums[m]==2) swap(nums[m], nums[r--]);
            else m++;
        }
    }
};
int main(){ vector<int> v={2,0,2,1,1,0}; Solution().sortColors(v); for (int x: v) cout<<x<<" "; cout<<endl; }
