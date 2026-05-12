// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 216 -- Partition Labels
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Partition string so each char appears in at most one part. Return sizes.
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
vector<int> partitionLabels(string s){int last[26]={0};for(int i=0;i<(int)s.size();i++)last[s[i]-'a']=i;vector<int> r;int st=0,e=0;for(int i=0;i<(int)s.size();i++){e=max(e,last[s[i]-'a']);if(i==e){r.push_back(e-st+1);st=i+1;}}return r;}
int main(){auto r=partitionLabels("ababcbacadefegdehijhklij");for(int x:r)cout<<x<<" ";cout<<"\n";}
