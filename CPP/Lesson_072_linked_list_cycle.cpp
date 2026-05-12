// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 072 -- Linked List Cycle
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Determine if a linked list has a cycle. Floyd's tortoise and hare.
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
    bool hasCycle(ListNode* head){
        ListNode *slow=head, *fast=head;
        while (fast && fast->next){ slow=slow->next; fast=fast->next->next; if (slow==fast) return true; }
        return false;
    }
};
int main(){
    auto a = new ListNode(1), b = new ListNode(2), c = new ListNode(3);
    a->next=b; b->next=c; c->next=a; cout<<Solution().hasCycle(a)<<endl;
    auto d = new ListNode(1); d->next = new ListNode(2); cout<<Solution().hasCycle(d)<<endl;
}
