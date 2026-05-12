// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 142 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return values seen from the right side of a binary tree.
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
vector<int> view(TN* root){vector<int> res;if(!root)return res;queue<TN*> q;q.push(root);while(!q.empty()){int n=q.size();for(int i=0;i<n;i++){auto x=q.front();q.pop();if(i==n-1)res.push_back(x->val);if(x->l)q.push(x->l);if(x->r)q.push(x->r);}}return res;}
int main(){TN n5(5),n4(4),n2(2,nullptr,&n5),n3(3,nullptr,&n4),n1(1,&n2,&n3);auto r=view(&n1);for(int x:r)cout<<x<<" ";cout<<"\n";}
