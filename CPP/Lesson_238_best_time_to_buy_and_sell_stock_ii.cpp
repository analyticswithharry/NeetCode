// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 238 -- Best Time to Buy And Sell Stock II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Multiple transactions allowed. Sum positive deltas.
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
int maxProfit(vector<int> p){int s=0;for(int i=1;i<(int)p.size();i++)s+=max(0,p[i]-p[i-1]);return s;}
int main(){cout<<maxProfit({7,1,5,3,6,4})<<"\n";}
