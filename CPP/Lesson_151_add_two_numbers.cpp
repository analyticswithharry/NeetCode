// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 151 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
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
struct LN{int val;LN* next;LN(int v):val(v),next(nullptr){}};
LN* add(LN* a,LN* b){LN* d=new LN(0);LN* cur=d;int c=0;while(a||b||c){int v=c+(a?a->val:0)+(b?b->val:0);c=v/10;cur->next=new LN(v%10);cur=cur->next;if(a)a=a->next;if(b)b=b->next;}return d->next;}
LN* fromArr(vector<int> x){LN* d=new LN(0);LN* c=d;for(int v:x){c->next=new LN(v);c=c->next;}return d->next;}
int main(){auto r=add(fromArr({2,4,3}),fromArr({5,6,4}));while(r){cout<<r->val<<" ";r=r->next;}cout<<"\n";}
