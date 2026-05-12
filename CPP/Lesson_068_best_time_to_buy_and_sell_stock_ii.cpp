// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 068 -- Best Time to Buy and Sell Stock II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   You may complete as many transactions as you like (buy then sell). Return max profit.
//
//   Example: [7,1,5,3,6,4] -> 7  (buy 1 sell 5, buy 3 sell 6)
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
    int maxProfit(vector<int>& p){ int s=0; for (size_t i=1;i<p.size();++i) s += max(0, p[i]-p[i-1]); return s; }
};
int main(){ vector<int> v={7,1,5,3,6,4}; cout<<Solution().maxProfit(v)<<endl; }
