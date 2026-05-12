// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 080 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree as list of lists.
//
//   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
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
    vector<vector<int>> levelOrder(TreeNode* root){
        vector<vector<int>> out; if (!root) return out;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()){
            int n = q.size(); vector<int> lvl;
            for (int i=0;i<n;i++){ auto x = q.front(); q.pop(); lvl.push_back(x->val);
                if (x->left) q.push(x->left); if (x->right) q.push(x->right); }
            out.push_back(lvl);
        }
        return out;
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(9); r->right = new TreeNode(20);
    r->right->left = new TreeNode(15); r->right->right = new TreeNode(7);
    for (auto& lvl: Solution().levelOrder(r)){ for (int x: lvl) cout<<x<<" "; cout<<"|"; } cout<<endl; }
