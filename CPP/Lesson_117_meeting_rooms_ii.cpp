// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 117 -- Meeting Rooms II
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given an array of meeting time intervals, return the minimum number of conference rooms required.
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
int minRooms(vector<vector<int>> it){sort(it.begin(),it.end());priority_queue<int,vector<int>,greater<int>> h;for(auto& x:it){if(!h.empty()&&h.top()<=x[0])h.pop();h.push(x[1]);}return h.size();}
int main(){cout<<minRooms({{0,30},{5,10},{15,20}})<<"\n"<<minRooms({{7,10},{2,4}})<<"\n";}
