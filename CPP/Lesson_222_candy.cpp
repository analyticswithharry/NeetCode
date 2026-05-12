// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 222 -- Candy
// Category   : Greedy
// Difficulty : Hard
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
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
int candy(vector<int> r){int n=r.size();vector<int> a(n,1);for(int i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(int i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=max(a[i],a[i+1]+1);return accumulate(a.begin(),a.end(),0);}
int main(){cout<<candy({1,0,2})<<"\n";}
