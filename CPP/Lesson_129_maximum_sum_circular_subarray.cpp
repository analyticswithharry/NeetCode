// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 129 -- Maximum Sum Circular Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
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
int maxCirc(vector<int>&a){int tot=0,mxc=a[0],cur=a[0],mnc=a[0],c2=a[0];for(int i=0;i<(int)a.size();i++){if(i>0){cur=max(a[i],cur+a[i]);mxc=max(mxc,cur);c2=min(a[i],c2+a[i]);mnc=min(mnc,c2);}tot+=a[i];}return mxc<0?mxc:max(mxc,tot-mnc);}
int main(){vector<int> a={1,-2,3,-2}, b={5,-3,5}, c={-3,-2,-3};cout<<maxCirc(a)<<"\n"<<maxCirc(b)<<"\n"<<maxCirc(c)<<"\n";}
