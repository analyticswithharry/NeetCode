// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 075 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Merge k sorted linked lists into one sorted list.
//
//   Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6
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
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
struct Cmp { bool operator()(ListNode* a, ListNode* b) const { return a->val > b->val; } };
class Solution { public:
    ListNode* mergeKLists(vector<ListNode*>& lists){
        priority_queue<ListNode*, vector<ListNode*>, Cmp> pq;
        for (auto n: lists) if (n) pq.push(n);
        ListNode d(0), *cur = &d;
        while (!pq.empty()){
            auto n = pq.top(); pq.pop(); cur->next = n; cur = n;
            if (n->next) pq.push(n->next);
        }
        return d.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ vector<ListNode*> ls = { fromArr({1,4,5}), fromArr({1,3,4}), fromArr({2,6}) };
    auto r = Solution().mergeKLists(ls); while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
