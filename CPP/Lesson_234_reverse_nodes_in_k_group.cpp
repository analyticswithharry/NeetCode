// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 234 -- Reverse Nodes In K Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Reverse nodes in groups of k. Remaining tail stays.
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
N* reverseK(N* head,int k){N* d=new N(0);d->n=head;N* g=d;while(true){N* kth=g;for(int i=0;i<k;i++){kth=kth->n;if(!kth)return d->n;}N* nxt=kth->n;N* pre=nxt;N* cur=g->n;while(cur!=nxt){N* t=cur->n;cur->n=pre;pre=cur;cur=t;}N* tmp=g->n;g->n=kth;g=tmp;}}
N* to(vector<int> a){N* d=new N(0);N* c=d;for(int x:a){c->n=new N(x);c=c->n;}return d->n;}
int main(){auto r=reverseK(to({1,2,3,4,5}),2);while(r){cout<<r->v<<" ";r=r->n;}cout<<"\n";}
