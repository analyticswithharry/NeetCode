// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 112 -- Sum of Two Integers
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given two integers a and b, return the sum without using + or -.
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
int add(int a,int b){while(b){int c=(unsigned)(a&b)<<1;a=a^b;b=c;}return a;}
int main(){cout<<add(1,2)<<"\n"<<add(-2,3)<<"\n";}
