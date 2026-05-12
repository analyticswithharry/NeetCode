// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 070 -- Remove Nth Node From End of List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Remove the nth node from the end of a linked list and return its head.
//
//   Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5
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
class Solution { public:
    ListNode* removeNthFromEnd(ListNode* head, int n){
        ListNode d(0); d.next = head; ListNode *fast=&d, *slow=&d;
        for (int i=0;i<n;i++) fast = fast->next;
        while (fast->next){ fast = fast->next; slow = slow->next; }
        slow->next = slow->next->next; return d.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().removeNthFromEnd(fromArr({1,2,3,4,5}), 2);
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
