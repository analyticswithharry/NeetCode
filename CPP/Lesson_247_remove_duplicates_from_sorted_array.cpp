// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 247 -- Remove Duplicates From Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   In-place dedupe of sorted array. Return new length.
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
int dedupe(vector<int>& a){if(a.empty())return 0;int k=1;for(int i=1;i<(int)a.size();i++)if(a[i]!=a[k-1])a[k++]=a[i];return k;}
int main(){vector<int> a={1,1,2,2,3};cout<<dedupe(a)<<"\n";}
