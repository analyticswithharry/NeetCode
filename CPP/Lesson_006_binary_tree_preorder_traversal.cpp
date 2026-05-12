// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 006 -- Binary Tree Preorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the preorder (Root, Left, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 2, 3]
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> out; if (!root) return out;
        stack<TreeNode*> st; st.push(root);
        while (!st.empty()) {
            auto* n = st.top(); st.pop(); out.push_back(n->val);
            if (n->right) st.push(n->right);
            if (n->left)  st.push(n->left);
        }
        return out;
    }
};

int main() {
    auto* r = new TreeNode(1); r->right = new TreeNode(2); r->right->left = new TreeNode(3);
    for (int v : Solution().preorderTraversal(r)) cout << v << " ";
    cout << endl;
}
