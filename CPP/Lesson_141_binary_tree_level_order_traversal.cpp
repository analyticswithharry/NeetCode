// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 141 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree (values grouped by level).
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
vector<vector<int>> levels(TN* root){vector<vector<int>> res;if(!root)return res;queue<TN*> q;q.push(root);while(!q.empty()){vector<int> lvl;int n=q.size();for(int i=0;i<n;i++){auto x=q.front();q.pop();lvl.push_back(x->val);if(x->l)q.push(x->l);if(x->r)q.push(x->r);}res.push_back(lvl);}return res;}
int main(){TN n15(15),n7(7),n9(9),n20(20,&n15,&n7),n3(3,&n9,&n20);auto r=levels(&n3);for(auto& v:r){for(int x:v)cout<<x<<" ";cout<<"| ";}cout<<"\n";}
