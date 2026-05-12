// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 241 -- First Missing Positive
// Category   : Arrays and Hashing
// Difficulty : Hard
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
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
int firstMissing(vector<int> n){int N=n.size();for(int i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i])swap(n[i],n[n[i]-1]);for(int i=0;i<N;i++)if(n[i]!=i+1)return i+1;return N+1;}
int main(){cout<<firstMissing({3,4,-1,1})<<"\n";}
