// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 083 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, determine if it is a valid BST.
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
    bool go(TreeNode* n, long lo, long hi){
        if (!n) return true;
        if (n->val <= lo || n->val >= hi) return false;
        return go(n->left, lo, n->val) && go(n->right, n->val, hi);
    }
public:
    bool isValidBST(TreeNode* root){ return go(root, LONG_MIN, LONG_MAX); }
};
int main(){ auto r = new TreeNode(2); r->left = new TreeNode(1); r->right = new TreeNode(3);
    cout<<Solution().isValidBST(r)<<endl;
    auto b = new TreeNode(5); b->left = new TreeNode(1); b->right = new TreeNode(4);
    b->right->left = new TreeNode(3); b->right->right = new TreeNode(6);
    cout<<Solution().isValidBST(b)<<endl; }
