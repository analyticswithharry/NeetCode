// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 005 -- Binary Tree Inorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the inorder (Left, Root, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 3, 2]
// =============================================================

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> out; stack<TreeNode*> st; TreeNode* cur = root;
        while (cur || !st.empty()) {
            while (cur) { st.push(cur); cur = cur->left; }
            cur = st.top(); st.pop(); out.push_back(cur->val); cur = cur->right;
        }
        return out;
    }
};

int main() {
    auto* r = new TreeNode(1); r->right = new TreeNode(2); r->right->left = new TreeNode(3);
    for (int v : Solution().inorderTraversal(r)) cout << v << " ";
    cout << endl;
}
