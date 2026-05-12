// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 114 -- Search In Rotated Sorted Array II
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 57
// =============================================================
//
// QUESTION:
//   Rotated sorted array may contain duplicates. Return true if target exists.
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
bool search(vector<int>&a,int t){int lo=0,hi=a.size()-1;while(lo<=hi){int m=(lo+hi)/2;if(a[m]==t)return true;if(a[lo]==a[m]&&a[m]==a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
int main(){vector<int>v={2,5,6,0,0,1,2};cout<<boolalpha<<search(v,0)<<"\n"<<search(v,3)<<"\n";}
