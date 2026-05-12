// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 122 -- Asteroid Collision
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
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
vector<int> collide(vector<int> a){vector<int> st;for(int x:a){bool alive=true;while(alive&&!st.empty()&&x<0&&st.back()>0){if(st.back()<-x){st.pop_back();}else if(st.back()==-x){st.pop_back();alive=false;}else alive=false;}if(alive)st.push_back(x);}return st;}
int main(){auto a=collide({5,10,-5});for(int x:a)cout<<x<<" ";cout<<"\n";auto b=collide({8,-8});for(int x:b)cout<<x<<" ";cout<<"\n";auto c=collide({10,2,-5});for(int x:c)cout<<x<<" ";cout<<"\n";}
