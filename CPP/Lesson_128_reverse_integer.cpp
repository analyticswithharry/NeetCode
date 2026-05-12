// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 128 -- Reverse Integer
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Reverse digits of a signed 32-bit integer; return 0 on overflow.
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
int rev(int x){long r=0;while(x){r=r*10+x%10;x/=10;}if(r<INT_MIN||r>INT_MAX)return 0;return (int)r;}
int main(){cout<<rev(123)<<"\n"<<rev(-456)<<"\n"<<rev(1534236469)<<"\n";}
