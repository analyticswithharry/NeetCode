// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 246 -- Largest Rectangle In Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max rectangular area in histogram. Monotonic stack.
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
int largestRect(vector<int> h){h.push_back(0);stack<int> st;int best=0;for(int i=0;i<(int)h.size();i++){while(!st.empty()&&h[st.top()]>h[i]){int top=st.top();st.pop();int w=st.empty()?i:i-st.top()-1;best=max(best,h[top]*w);}st.push(i);}return best;}
int main(){cout<<largestRect({2,1,5,6,2,3})<<"\n";}
