// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 152 -- Find The Duplicate Number
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.
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
int dup(vector<int> a){int s=a[0],f=a[0];do{s=a[s];f=a[a[f]];}while(s!=f);s=a[0];while(s!=f){s=a[s];f=a[f];}return s;}
int main(){cout<<dup({1,3,4,2,2})<<"\n"<<dup({3,1,3,4,2})<<"\n";}
