// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 133 -- Counting Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   For 0..n return array where ans[i] = number of 1-bits in i.
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
vector<int> cb(int n){vector<int> a(n+1);for(int i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
int main(){auto v=cb(5);for(int x:v)cout<<x<<" ";cout<<"\n";}
