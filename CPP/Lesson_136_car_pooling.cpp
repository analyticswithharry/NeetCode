// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 136 -- Car Pooling
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
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
bool carPool(vector<vector<int>> t,int cap){vector<int> e(1001,0);for(auto& x:t){e[x[1]]+=x[0];e[x[2]]-=x[0];}int s=0;for(int v:e){s+=v;if(s>cap)return false;}return true;}
int main(){cout<<boolalpha<<carPool({{2,1,5},{3,3,7}},4)<<"\n"<<carPool({{2,1,5},{3,3,7}},5)<<"\n";}
