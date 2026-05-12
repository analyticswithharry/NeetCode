// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 127 -- Number of 1 Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Return the number of 1 bits in unsigned int.
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
int hw(unsigned n){int c=0;while(n){n&=n-1;c++;}return c;}
int main(){cout<<hw(11)<<"\n"<<hw(128)<<"\n";}
