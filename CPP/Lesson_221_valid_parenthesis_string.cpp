// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 221 -- Valid Parenthesis String
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   '*' can be '(' ')' or empty. Determine if string can be valid.
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
bool checkValid(string s){int lo=0,hi=0;for(char c:s){lo+=c=='('?1:-1;hi+=c!=')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo==0;}
int main(){cout<<checkValid("(*))")<<"\n";}
