// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 158 -- Minimum Array End
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.
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
long long minEnd(long long n,long long x){n--;long long r=x,bit=1,nb=1;while(nb<=n){if((x&bit)==0){if(n&nb)r|=bit;nb<<=1;}bit<<=1;}return r;}
int main(){cout<<minEnd(3,4)<<"\n"<<minEnd(2,7)<<"\n";}
