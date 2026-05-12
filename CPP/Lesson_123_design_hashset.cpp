// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 123 -- Design HashSet
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Design a HashSet (without built-in set): add, remove, contains.
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
struct MyHashSet{ vector<vector<int>> b=vector<vector<int>>(769); int h(int k){return k%769;} void add(int k){auto& x=b[h(k)];if(find(x.begin(),x.end(),k)==x.end())x.push_back(k);} void remove(int k){auto& x=b[h(k)];x.erase(std::remove(x.begin(),x.end(),k),x.end());} bool contains(int k){auto& x=b[h(k)];return find(x.begin(),x.end(),k)!=x.end();}};
int main(){MyHashSet s; s.add(1); s.add(2); cout<<boolalpha<<s.contains(1)<<" "<<s.contains(3)<<"\n"; s.remove(2); cout<<s.contains(2)<<"\n";}
