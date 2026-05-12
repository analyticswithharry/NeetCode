// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 113 -- Search In Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 57
// =============================================================
//
// QUESTION:
//   Given a rotated sorted array (no duplicates) and target, return index or -1. O(log n).
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
int search(vector<int>&a,int t){int lo=0,hi=a.size()-1;while(lo<=hi){int m=(lo+hi)/2;if(a[m]==t)return m;if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return -1;}
int main(){vector<int> v={4,5,6,7,0,1,2};cout<<search(v,0)<<"\n"<<search(v,3)<<"\n";}
