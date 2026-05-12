// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 004 -- Merge Two Sorted Lists
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 2
// =============================================================
//
// QUESTION:
//   You are given the heads of two sorted linked lists list1 and list2.
//   Merge them into one sorted list and return its head.
//
//   Example:
//     Input : 1->2->4, 1->3->4
//     Output: 1->1->2->3->4->4
// =============================================================

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

struct ListNode { int val; ListNode* next; ListNode(int v=0):val(v),next(nullptr){} };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        ListNode d, *t = &d;
        while (a && b) {
            if (a->val <= b->val) { t->next = a; a = a->next; }
            else { t->next = b; b = b->next; }
            t = t->next;
        }
        t->next = a ? a : b;
        return d.next;
    }
};

ListNode* build(vector<int> v){ ListNode* d=new ListNode(); ListNode* t=d;
    for(int x: v){ t->next=new ListNode(x); t=t->next;} return d->next; }

int main() {
    auto* r = Solution().mergeTwoLists(build({1,2,4}), build({1,3,4}));
    while (r) { cout << r->val << " "; r = r->next; }
    cout << endl;
}
