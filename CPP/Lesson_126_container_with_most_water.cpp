// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 126 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that form the container holding most water.
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
int maxArea(vector<int>&h){int l=0,r=h.size()-1,b=0;while(l<r){b=max(b,(r-l)*min(h[l],h[r]));if(h[l]<h[r])l++;else r--;}return b;}
int main(){vector<int> v={1,8,6,2,5,4,8,3,7};cout<<maxArea(v)<<"\n";}
