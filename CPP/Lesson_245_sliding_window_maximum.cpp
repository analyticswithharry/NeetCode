// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 245 -- Sliding Window Maximum
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max in each window of size k. Monotonic deque.
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
vector<int> maxSliding(vector<int> n,int k){deque<int> dq;vector<int> out;for(int i=0;i<(int)n.size();i++){while(!dq.empty()&&n[dq.back()]<=n[i])dq.pop_back();dq.push_back(i);if(dq.front()<=i-k)dq.pop_front();if(i>=k-1)out.push_back(n[dq.front()]);}return out;}
int main(){for(int x:maxSliding({1,3,-1,-3,5,3,6,7},3))cout<<x<<" ";cout<<"\n";}
