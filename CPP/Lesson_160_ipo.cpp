// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 160 -- IPO
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
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
int ipo(int k,int w,vector<int> p,vector<int> c){int n=p.size();vector<pair<int,int>> proj;for(int i=0;i<n;i++)proj.push_back({c[i],p[i]});sort(proj.begin(),proj.end());priority_queue<int> h;int i=0;for(int s=0;s<k;s++){while(i<n&&proj[i].first<=w){h.push(proj[i].second);i++;}if(h.empty())break;w+=h.top();h.pop();}return w;}
int main(){cout<<ipo(2,0,{1,2,3},{0,1,1})<<"\n"<<ipo(3,0,{1,2,3},{0,1,2})<<"\n";}
