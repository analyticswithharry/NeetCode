// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 248 -- Detect Squares
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   Add point or count axis-aligned squares with given query point.
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
class DS{map<pair<int,int>,int> c;public:void add(int x,int y){c[{x,y}]++;}int count(int x,int y){int tot=0;for(auto& [k,v]:c){auto [a,b]=k;if(a==x||abs(a-x)!=abs(b-y))continue;auto it1=c.find({a,y}),it2=c.find({x,b});if(it1!=c.end()&&it2!=c.end())tot+=v*it1->second*it2->second;}return tot;}};
int main(){DS d;d.add(3,10);d.add(11,2);d.add(3,2);cout<<d.count(11,10)<<"\n";}
