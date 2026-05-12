// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 213 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return true if s2 contains a permutation of s1.
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
bool checkInclusion(string s1,string s2){if(s1.size()>s2.size())return false;vector<int> a(26),b(26);for(char c:s1)a[c-'a']++;for(int i=0;i<(int)s2.size();i++){b[s2[i]-'a']++;if(i>=(int)s1.size())b[s2[i-s1.size()]-'a']--;if(a==b)return true;}return false;}
int main(){cout<<checkInclusion("ab","eidbaooo")<<"\n"<<checkInclusion("ab","eidboaoo")<<"\n";}
