// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 233 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Merge K sorted linked lists into one. Use heap.
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
struct N{int v;N* n;N(int v):v(v),n(nullptr){}};
N* mergeK(vector<N*> L){priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> q;for(int i=0;i<(int)L.size();i++)if(L[i])q.push({L[i]->v,i});N* d=new N(0);N* c=d;while(!q.empty()){auto [v,i]=q.top();q.pop();c->n=new N(v);c=c->n;L[i]=L[i]->n;if(L[i])q.push({L[i]->v,i});}return d->n;}
N* to(vector<int> a){N* d=new N(0);N* c=d;for(int x:a){c->n=new N(x);c=c->n;}return d->n;}
int main(){auto r=mergeK({to({1,4,5}),to({1,3,4}),to({2,6})});while(r){cout<<r->v<<" ";r=r->n;}cout<<"\n";}
