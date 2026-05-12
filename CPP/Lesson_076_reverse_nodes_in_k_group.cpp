// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 076 -- Reverse Nodes in k-Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.
//
//   Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
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
    ListNode* reverseKGroup(ListNode* head, int k){
        ListNode* cur = head; int cnt = 0;
        while (cur && cnt < k){ cur = cur->next; cnt++; }
        if (cnt < k) return head;
        ListNode* prev = nullptr; cur = head;
        for (int i=0;i<k;i++){ ListNode* n = cur->next; cur->next = prev; prev = cur; cur = n; }
        head->next = reverseKGroup(cur, k);
        return prev;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().reverseKGroup(fromArr({1,2,3,4,5}), 2);
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl;
    auto s = Solution().reverseKGroup(fromArr({1,2,3,4,5}), 3);
    while (s){ cout<<s->val<<" "; s=s->next; } cout<<endl; }
