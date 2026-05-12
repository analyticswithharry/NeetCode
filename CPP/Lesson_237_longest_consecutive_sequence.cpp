// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 237 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Length of longest run of consecutive integers in unsorted array. O(n) hashset.
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
int longestConsec(vector<int> n){unordered_set<int> s(n.begin(),n.end());int best=0;for(int x:s)if(!s.count(x-1)){int y=x;while(s.count(y+1))y++;best=max(best,y-x+1);}return best;}
int main(){cout<<longestConsec({100,4,200,1,3,2})<<"\n";}
