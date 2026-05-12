// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 132 -- Split Array Largest Sum
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
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
bool can(vector<int>&a,int k,int mx){int c=1,s=0;for(int x:a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;}
int split(vector<int>&a,int k){int lo=*max_element(a.begin(),a.end()),hi=accumulate(a.begin(),a.end(),0);while(lo<hi){int m=(lo+hi)/2;if(can(a,k,m))hi=m;else lo=m+1;}return lo;}
int main(){vector<int> v={7,2,5,10,8};cout<<split(v,2)<<"\n";}
