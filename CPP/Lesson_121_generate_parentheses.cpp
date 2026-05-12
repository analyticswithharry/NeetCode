// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 121 -- Generate Parentheses
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given n pairs of parentheses, generate all combinations of well-formed parentheses.
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
vector<string> R; int N;
void rec(string s,int o,int c){if((int)s.size()==2*N){R.push_back(s);return;}if(o<N)rec(s+"(",o+1,c);if(c<o)rec(s+")",o,c+1);}
vector<string> gen(int n){R.clear();N=n;rec("",0,0);return R;}
int main(){auto v=gen(3);for(auto&s:v)cout<<s<<" ";cout<<"\n";}
