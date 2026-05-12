// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 134 -- Bitwise AND of Numbers Range
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.
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
int rangeAnd(int m,int n){int s=0;while(m!=n){m>>=1;n>>=1;s++;}return m<<s;}
int main(){cout<<rangeAnd(5,7)<<"\n"<<rangeAnd(0,0)<<"\n";}
