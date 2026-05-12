// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 085 -- Construct Binary Tree from Preorder and Inorder
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.
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
    int p = 0; unordered_map<int,int> idx;
    TreeNode* go(vector<int>& pre, int l, int r){
        if (l > r) return nullptr;
        int v = pre[p++]; TreeNode* root = new TreeNode(v); int m = idx[v];
        root->left = go(pre, l, m-1); root->right = go(pre, m+1, r);
        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder){
        for (int i=0;i<(int)inorder.size();i++) idx[inorder[i]] = i;
        return go(preorder, 0, inorder.size()-1);
    }
};
void pre(TreeNode* n){ if (!n) return; cout<<n->val<<" "; pre(n->left); pre(n->right); }
int main(){ vector<int> p={3,9,20,15,7}, i={9,3,15,20,7};
    auto t = Solution().buildTree(p, i); pre(t); cout<<endl; }
