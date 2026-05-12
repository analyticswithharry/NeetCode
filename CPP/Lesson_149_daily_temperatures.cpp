// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 149 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   For each day, return number of days until a warmer temperature, or 0.
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
vector<int> dailyT(vector<int> t){vector<int> r(t.size(),0);stack<int> st;for(int i=0;i<(int)t.size();i++){while(!st.empty()&&t[st.top()]<t[i]){int j=st.top();st.pop();r[j]=i-j;}st.push(i);}return r;}
int main(){auto v=dailyT({73,74,75,71,69,72,76,73});for(int x:v)cout<<x<<" ";cout<<"\n";}
