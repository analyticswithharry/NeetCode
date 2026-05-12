// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 219 -- Find K Closest Elements
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Return k closest sorted ints to x (binary search the window).
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
vector<int> findClosest(vector<int> a,int k,int x){int l=0,r=a.size()-k;while(l<r){int m=(l+r)/2;if(x-a[m]>a[m+k]-x)l=m+1;else r=m;}return vector<int>(a.begin()+l,a.begin()+l+k);}
int main(){auto r=findClosest({1,2,3,4,5},4,3);for(int x:r)cout<<x<<" ";cout<<"\n";}
