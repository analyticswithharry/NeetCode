// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 148 -- Best Time to Buy And Sell Stock With Cooldown
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Stock prices; can do unlimited transactions but after selling must cooldown 1 day. Max profit.
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
int maxP(vector<int>&p){int hold=-p[0],sold=0,rest=0;for(int i=1;i<(int)p.size();i++){int h=max(hold,rest-p[i]);int s=hold+p[i];int r=max(rest,sold);hold=h;sold=s;rest=r;}return max(sold,rest);}
int main(){vector<int> v={1,2,3,0,2};cout<<maxP(v)<<"\n";}
