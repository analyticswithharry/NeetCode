// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 139 -- Roman to Integer
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Convert Roman numeral string to integer.
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
int r2i(string s){unordered_map<char,int> m={{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};int t=0,p=0;for(int i=s.size()-1;i>=0;i--){int v=m[s[i]];if(v<p)t-=v;else{t+=v;p=v;}}return t;}
int main(){cout<<r2i("III")<<"\n"<<r2i("LVIII")<<"\n"<<r2i("MCMXCIV")<<"\n";}
