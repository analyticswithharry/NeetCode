// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 137 -- Letter Combinations of a Phone Number
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Given digits 2-9, return all possible letter combinations the number could represent.
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
vector<string> letters(string d){if(d.empty())return {};vector<string> m={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};vector<string> r={""};for(char c:d){vector<string> n;for(auto& p:r)for(char x:m[c-'0'])n.push_back(p+x);r=n;}return r;}
int main(){auto v=letters("23");for(auto&s:v)cout<<s<<" ";cout<<"\n";}
