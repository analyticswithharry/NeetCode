// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 220 -- Minimum Window Substring
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Smallest substring of s containing all chars of t.
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
string minWindow(string s,string t){if(t.empty())return"";unordered_map<char,int> need,have;for(char c:t)need[c]++;int nn=need.size(),hn=0,l=0,rl=INT_MAX,rs=0;for(int r=0;r<(int)s.size();r++){have[s[r]]++;if(need.count(s[r])&&have[s[r]]==need[s[r]])hn++;while(hn==nn){if(r-l+1<rl){rl=r-l+1;rs=l;}have[s[l]]--;if(need.count(s[l])&&have[s[l]]<need[s[l]])hn--;l++;}}return rl==INT_MAX?"":s.substr(rs,rl);}
int main(){cout<<minWindow("ADOBECODEBANC","ABC")<<"\n";}
