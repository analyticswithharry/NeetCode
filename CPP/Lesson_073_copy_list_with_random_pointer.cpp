// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 073 -- Copy List With Random Pointer
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Deep copy a linked list where each node has next and a random pointer that may point to any node or null.
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
struct Node { int val; Node *next; Node *random; Node(int v):val(v),next(nullptr),random(nullptr){} };
class Solution { public:
    Node* copyRandomList(Node* head){
        if (!head) return nullptr;
        unordered_map<Node*, Node*> m; Node* cur = head;
        while (cur){ m[cur] = new Node(cur->val); cur = cur->next; }
        cur = head;
        while (cur){ m[cur]->next = m[cur->next]; m[cur]->random = m[cur->random]; cur = cur->next; }
        return m[head];
    }
};
int main(){
    auto a = new Node(1), b = new Node(2); a->next=b; a->random=b; b->random=b;
    auto c = Solution().copyRandomList(a);
    cout<<c->val<<","<<c->random->val<<" "<<c->next->val<<","<<c->next->random->val<<endl;
}
