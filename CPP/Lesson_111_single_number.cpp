// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 111 -- Single Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given a non-empty array of integers, every element appears twice except for one. Find that single one. O(1) extra space.
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
int single(vector<int>&a){int r=0;for(int x:a)r^=x;return r;}
int main(){cout<<single(*new vector<int>{2,2,1})<<"\n"<<single(*new vector<int>{4,1,2,1,2})<<"\n";}
