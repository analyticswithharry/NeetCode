// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 125 -- Merge Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.
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
vector<int> merge(vector<int> a,int m,vector<int> b,int n){int i=m-1,j=n-1,k=m+n-1;while(j>=0){if(i>=0&&a[i]>b[j])a[k--]=a[i--];else a[k--]=b[j--];}return a;}
int main(){auto v=merge({1,2,3,0,0,0},3,{2,5,6},3);for(int x:v)cout<<x<<" ";cout<<"\n";}
