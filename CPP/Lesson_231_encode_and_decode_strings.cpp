// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 231 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Length-prefix encoding for arbitrary strings.
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
string encode(vector<string> a){string r;for(auto&s:a)r+=to_string(s.size())+"#"+s;return r;}
vector<string> decode(string s){vector<string> r;int i=0;while(i<(int)s.size()){int j=s.find('#',i);int n=stoi(s.substr(i,j-i));r.push_back(s.substr(j+1,n));i=j+1+n;}return r;}
int main(){auto e=encode({"hello","world","#42"});cout<<e<<"\n";for(auto&s:decode(e))cout<<s<<"|";cout<<"\n";}
