// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 084 -- Kth Smallest Element in a BST
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given a BST, return the kth smallest value (1-indexed). Use inorder traversal.
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
    int kthSmallest(TreeNode* root, int k){
        stack<TreeNode*> st; TreeNode* cur = root;
        while (!st.empty() || cur){
            while (cur){ st.push(cur); cur = cur->left; }
            cur = st.top(); st.pop(); if (--k == 0) return cur->val;
            cur = cur->right;
        }
        return -1;
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(1); r->right = new TreeNode(4);
    r->left->right = new TreeNode(2);
    cout<<Solution().kthSmallest(r,1)<<" "<<Solution().kthSmallest(r,3)<<endl; }
