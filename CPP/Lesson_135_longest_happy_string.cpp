// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 135 -- Longest Happy String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.
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
string longest(int a,int b,int c){priority_queue<pair<int,char>> h;if(a)h.push({a,'a'});if(b)h.push({b,'b'});if(c)h.push({c,'c'});string s;while(!h.empty()){auto [c1,ch1]=h.top();h.pop();int n=s.size();if(n>=2&&s[n-1]==ch1&&s[n-2]==ch1){if(h.empty())break;auto [c2,ch2]=h.top();h.pop();s+=ch2;if(c2-1)h.push({c2-1,ch2});h.push({c1,ch1});}else{s+=ch1;if(c1-1)h.push({c1-1,ch1});}}return s;}
int main(){cout<<longest(1,1,7)<<"\n"<<longest(7,1,0)<<"\n";}
