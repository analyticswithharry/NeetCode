// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 118 -- Meeting Rooms III
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.
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
int mostBooked(int n,vector<vector<int>> m){sort(m.begin(),m.end());priority_queue<int,vector<int>,greater<int>> fr;for(int i=0;i<n;i++)fr.push(i);priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<>> busy;vector<long long> cnt(n,0);for(auto& x:m){while(!busy.empty()&&busy.top().first<=x[0]){fr.push(busy.top().second);busy.pop();}int r; long long e;if(!fr.empty()){r=fr.top();fr.pop();e=x[1];}else{auto t=busy.top();busy.pop();r=t.second;e=t.first+x[1]-x[0];}busy.push({e,r});cnt[r]++;}int mi=0;for(int i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
int main(){cout<<mostBooked(2,{{0,10},{1,5},{2,7},{3,4}})<<"\n";}
