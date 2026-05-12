// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 150 -- Online Stock Span
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
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
struct StockSpanner{vector<pair<int,int>> st; int next(int p){int s=1;while(!st.empty()&&st.back().first<=p){s+=st.back().second;st.pop_back();}st.push_back({p,s});return s;}};
int main(){StockSpanner s;for(int v:{100,80,60,70,60,75,85})cout<<s.next(v)<<" ";cout<<"\n";}
