// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 146 -- Count Good Nodes In Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
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
struct TN{int val;TN*l;TN*r;TN(int v,TN*a=nullptr,TN*b=nullptr):val(v),l(a),r(b){}};
int rec(TN* n,int m){if(!n)return 0;int c=n->val>=m?1:0;int nm=max(m,n->val);return c+rec(n->l,nm)+rec(n->r,nm);}
int good(TN* r){return rec(r,INT_MIN);}
int main(){TN n3a(3),n1a(1,&n3a,nullptr),n1b(1),n5(5),n4(4,&n1b,&n5),root(3,&n1a,&n4);cout<<good(&root)<<"\n";}
