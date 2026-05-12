// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 078 -- Same Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   Given two binary trees, check if they are structurally identical with same node values.
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
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution { public:
    bool isSameTree(TreeNode* p, TreeNode* q){
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    }
};
int main(){ auto a = new TreeNode(1); a->left = new TreeNode(2); a->right = new TreeNode(3);
    auto b = new TreeNode(1); b->left = new TreeNode(2); b->right = new TreeNode(3);
    cout<<Solution().isSameTree(a,b)<<endl; }
