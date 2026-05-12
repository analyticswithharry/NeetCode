// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 079 -- Subtree of Another Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
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
class Solution {
    bool same(TreeNode* p, TreeNode* q){
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return same(p->left,q->left) && same(p->right,q->right);
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* sub){
        if (!root) return false;
        if (same(root, sub)) return true;
        return isSubtree(root->left, sub) || isSubtree(root->right, sub);
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(4); r->right = new TreeNode(5);
    r->left->left = new TreeNode(1); r->left->right = new TreeNode(2);
    auto s = new TreeNode(4); s->left = new TreeNode(1); s->right = new TreeNode(2);
    cout<<Solution().isSubtree(r, s)<<endl; }
