// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 235 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
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
vector<int> productExceptSelf(vector<int> n){vector<int> o(n.size(),1);int p=1;for(int i=0;i<(int)n.size();i++){o[i]=p;p*=n[i];}p=1;for(int i=n.size()-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
int main(){for(int x:productExceptSelf({1,2,3,4}))cout<<x<<" ";cout<<"\n";}
