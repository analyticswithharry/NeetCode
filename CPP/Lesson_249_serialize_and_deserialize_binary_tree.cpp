// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 249 -- Serialize And Deserialize Binary Tree
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Pre-order serialize with null markers; queue-based deserialize.
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
struct T{int v;T*l;T*r;T(int v):v(v),l(0),r(0){}};
void dfs(T* n,string& s){if(!n){s+="#,";return;}s+=to_string(n->v)+",";dfs(n->l,s);dfs(n->r,s);}
string ser(T* r){string s;dfs(r,s);return s;}
int gi;vector<string> ar;
T* dfs2(){string x=ar[gi++];if(x=="#")return 0;T* n=new T(stoi(x));n->l=dfs2();n->r=dfs2();return n;}
T* des(string s){ar.clear();string cur;for(char c:s){if(c==','){ar.push_back(cur);cur.clear();}else cur+=c;}gi=0;return dfs2();}
int main(){T* r=new T(1);r->l=new T(2);r->r=new T(3);r->r->l=new T(4);r->r->r=new T(5);string s=ser(r);cout<<s<<"\n"<<ser(des(s))<<"\n";}
