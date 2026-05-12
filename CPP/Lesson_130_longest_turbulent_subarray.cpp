// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 130 -- Longest Turbulent Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given an array, return length of longest turbulent subarray (alternating > <).
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
int turb(vector<int>&a){int inc=1,dec=1,b=1;for(int i=1;i<(int)a.size();i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else inc=dec=1;b=max({b,inc,dec});}return b;}
int main(){vector<int> v={9,4,2,10,7,8,8,1,9};cout<<turb(v)<<"\n";}
