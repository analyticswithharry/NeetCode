// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 120 -- Clone Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given a node in a connected undirected graph, return a deep copy of the graph.
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
struct Node{int val; vector<Node*> neighbors; Node(int v):val(v){}};
unordered_map<Node*,Node*> seen;
Node* clone(Node* n){if(!n)return nullptr;if(seen.count(n))return seen[n];Node* c=new Node(n->val);seen[n]=c;for(auto y:n->neighbors)c->neighbors.push_back(clone(y));return c;}
int main(){Node a(1),b(2);a.neighbors={&b};b.neighbors={&a};Node* c=clone(&a);cout<<c->val<<" "<<c->neighbors[0]->val<<" "<<c->neighbors[0]->neighbors[0]->val<<"\n";}
