// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 138 -- Matchsticks to Square
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Use all matchsticks to form a square. Return true if possible.
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
vector<int> M; int SIDE; vector<int> S(4,0);
bool rec(int i){if(i==(int)M.size())return S[0]==SIDE&&S[1]==SIDE&&S[2]==SIDE;for(int j=0;j<4;j++){if(S[j]+M[i]>SIDE)continue;if(j>0&&S[j]==S[j-1])continue;S[j]+=M[i];if(rec(i+1))return true;S[j]-=M[i];}return false;}
bool square(vector<int> m){int s=0;for(int x:m)s+=x;if(s%4)return false;SIDE=s/4;sort(m.rbegin(),m.rend());if(m[0]>SIDE)return false;M=m;S=vector<int>(4,0);return rec(0);}
int main(){cout<<boolalpha<<square({1,1,2,2,2})<<"\n"<<square({3,3,3,3,4})<<"\n";}
