// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 082 -- Count Good Nodes in Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   A node X is good if no node on the path from root to X has value greater than X. Count good nodes.
//
//   Example: [3,1,4,3,null,1,5] -> 4
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
    int dfs(TreeNode* n, int mx){ if (!n) return 0;
        int c = n->val >= mx ? 1 : 0; int m = max(mx, n->val);
        return c + dfs(n->left, m) + dfs(n->right, m); }
public:
    int goodNodes(TreeNode* root){ return dfs(root, root->val); }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(1); r->right = new TreeNode(4);
    r->left->left = new TreeNode(3); r->right->left = new TreeNode(1); r->right->right = new TreeNode(5);
    cout<<Solution().goodNodes(r)<<endl; }
