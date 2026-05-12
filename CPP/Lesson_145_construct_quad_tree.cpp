// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 145 -- Construct Quad Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   Given an n x n grid of 0/1, build a quad tree representation. Return root.
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
struct QN{bool val,isLeaf;QN *tl=nullptr,*tr=nullptr,*bl=nullptr,*br=nullptr;QN(bool v,bool l):val(v),isLeaf(l){}};
vector<vector<int>> G;
QN* rec(int r,int c,int n){bool same=true;for(int i=r;i<r+n;i++)for(int j=c;j<c+n;j++)if(G[i][j]!=G[r][c])same=false;if(same)return new QN(G[r][c]==1,true);int h=n/2;QN* q=new QN(true,false);q->tl=rec(r,c,h);q->tr=rec(r,c+h,h);q->bl=rec(r+h,c,h);q->br=rec(r+h,c+h,h);return q;}
void ser(QN* n,vector<string>& out){if(n->isLeaf){out.push_back(n->val?"1":"0");return;}out.push_back("#");ser(n->tl,out);ser(n->tr,out);ser(n->bl,out);ser(n->br,out);}
int main(){G={{0,1},{1,0}};auto r=rec(0,0,2);vector<string> o;ser(r,o);for(auto&s:o)cout<<s<<" ";cout<<"\n";}
