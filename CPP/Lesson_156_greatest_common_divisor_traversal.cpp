// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 156 -- Greatest Common Divisor Traversal
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
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
vector<int> par;
int f(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
void u(int x,int y){x=f(x);y=f(y);if(x!=y)par[x]=y;}
vector<int> primes(int x){vector<int> r;for(int d=2;1LL*d*d<=x;d++)if(x%d==0){r.push_back(d);while(x%d==0)x/=d;}if(x>1)r.push_back(x);return r;}
bool can(vector<int> a){int n=a.size();par.assign(n,0);iota(par.begin(),par.end(),0);unordered_map<int,int> pm;for(int i=0;i<n;i++)for(int p:primes(a[i])){auto it=pm.find(p);if(it!=pm.end())u(i,it->second);else pm[p]=i;}int r=f(0);for(int i=0;i<n;i++)if(f(i)!=r)return false;return true;}
int main(){cout<<boolalpha<<can({2,3,6})<<"\n"<<can({3,9,5})<<"\n"<<can({4,3,12,8})<<"\n";}
