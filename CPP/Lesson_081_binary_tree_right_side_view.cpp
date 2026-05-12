// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 081 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   Return the values of nodes you'd see ordered from top to bottom from the right side.
//
//   Example: [1,2,3,null,5,null,4] -> [1,3,4]
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
    vector<int> rightSideView(TreeNode* root){
        vector<int> out; if (!root) return out;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()){
            int n = q.size();
            for (int i=0;i<n;i++){ auto x = q.front(); q.pop(); if (i == n-1) out.push_back(x->val);
                if (x->left) q.push(x->left); if (x->right) q.push(x->right); }
        }
        return out;
    }
};
int main(){ auto r = new TreeNode(1); r->left = new TreeNode(2); r->right = new TreeNode(3);
    r->left->right = new TreeNode(5); r->right->right = new TreeNode(4);
    for (int x: Solution().rightSideView(r)) cout<<x<<" "; cout<<endl; }
