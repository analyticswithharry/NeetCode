// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 124 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
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
vector<int> topK(vector<int> a,int k){unordered_map<int,int> m;for(int x:a)m[x]++;vector<pair<int,int>> v(m.begin(),m.end());sort(v.begin(),v.end(),[](auto&p,auto&q){return p.second>q.second;});vector<int> r;for(int i=0;i<k;i++)r.push_back(v[i].first);return r;}
int main(){auto v=topK({1,1,1,2,2,3},2);for(int x:v)cout<<x<<" ";cout<<"\n";}
