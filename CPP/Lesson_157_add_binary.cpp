// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 157 -- Add Binary
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given two binary strings, return their sum as a binary string.
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
string addBin(string a,string b){int i=a.size()-1,j=b.size()-1,c=0;string r;while(i>=0||j>=0||c){int s=c+(i>=0?a[i--]-'0':0)+(j>=0?b[j--]-'0':0);r+=char('0'+s%2);c=s/2;}reverse(r.begin(),r.end());return r;}
int main(){cout<<addBin("11","1")<<"\n"<<addBin("1010","1011")<<"\n";}
