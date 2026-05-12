// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 143 -- Palindromic Substrings
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Count number of palindromic substrings in s.
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
int ex(string& s,int a,int b){int c=0;while(a>=0&&b<(int)s.size()&&s[a]==s[b]){c++;a--;b++;}return c;}
int count(string s){int c=0;for(int i=0;i<(int)s.size();i++){c+=ex(s,i,i)+ex(s,i,i+1);}return c;}
int main(){cout<<count("abc")<<"\n"<<count("aaa")<<"\n";}
