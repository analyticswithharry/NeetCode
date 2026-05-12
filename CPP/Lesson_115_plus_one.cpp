// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 115 -- Plus One
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
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
vector<int> plusOne(vector<int> d){for(int i=d.size()-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}d.insert(d.begin(),1);return d;}
int main(){auto a=plusOne({1,2,3});for(int x:a)cout<<x<<" ";cout<<"\n";auto b=plusOne({9,9});for(int x:b)cout<<x<<" ";cout<<"\n";}
