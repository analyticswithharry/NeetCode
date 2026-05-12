// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 244 -- Minimum Interval to Include Each Query
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   For each query q, find smallest interval covering q.
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
vector<int> minInterval(vector<vector<int>> iv,vector<int> q){sort(iv.begin(),iv.end());vector<int> idx(q.size());iota(idx.begin(),idx.end(),0);sort(idx.begin(),idx.end(),[&](int a,int b){return q[a]<q[b];});vector<int> res(q.size());priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> h;int i=0;for(int k:idx){int v=q[k];while(i<(int)iv.size()&&iv[i][0]<=v){h.push({iv[i][1]-iv[i][0]+1,iv[i][1]});i++;}while(!h.empty()&&h.top().second<v)h.pop();res[k]=h.empty()?-1:h.top().first;}return res;}
int main(){auto r=minInterval({{1,4},{2,4},{3,6},{4,4}},{2,3,4,5});for(int x:r)cout<<x<<" ";cout<<"\n";}
