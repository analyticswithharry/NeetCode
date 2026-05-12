// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 159 -- Find Median From Data Stream
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Design MedianFinder: addNum, findMedian.
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
struct MedianFinder{ priority_queue<int> lo; priority_queue<int,vector<int>,greater<int>> hi; void addNum(int x){lo.push(x);hi.push(lo.top());lo.pop();if(hi.size()>lo.size()){lo.push(hi.top());hi.pop();}} double findMedian(){if(lo.size()>hi.size())return lo.top();return (lo.top()+hi.top())/2.0;}};
int main(){MedianFinder m;for(int x:{1,2,3}){m.addNum(x);cout<<m.findMedian()<<"\n";}}
