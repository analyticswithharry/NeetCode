// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 071 -- Reorder List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...
//
//   Example: 1->2->3->4 -> 1->4->2->3
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
    void reorderList(ListNode* head){
        if (!head || !head->next) return;
        ListNode *slow=head, *fast=head;
        while (fast->next && fast->next->next){ slow=slow->next; fast=fast->next->next; }
        ListNode *prev=nullptr, *cur=slow->next; slow->next=nullptr;
        while (cur){ ListNode* n=cur->next; cur->next=prev; prev=cur; cur=n; }
        ListNode *l1=head, *l2=prev;
        while (l2){ ListNode *t1=l1->next, *t2=l2->next; l1->next=l2; l2->next=t1; l1=t1; l2=t2; }
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto h = fromArr({1,2,3,4}); Solution().reorderList(h);
    while (h){ cout<<h->val<<" "; h=h->next; } cout<<endl; }
