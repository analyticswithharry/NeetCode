// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 069 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.
//
//   Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
        ListNode dummy(0), *cur=&dummy; int carry=0;
        while (l1 || l2 || carry){
            int x = (l1?l1->val:0) + (l2?l2->val:0) + carry;
            carry = x/10; cur->next = new ListNode(x%10); cur = cur->next;
            if (l1) l1=l1->next; if (l2) l2=l2->next;
        }
        return dummy.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next = new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().addTwoNumbers(fromArr({2,4,3}), fromArr({5,6,4}));
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
