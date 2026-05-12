// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 001 -- Reverse String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 1
// =============================================================
//
// QUESTION:
//   Write a function that reverses a string. The input string is given as
//   an array of characters s. You must do this by modifying the input array
//   in-place with O(1) extra memory.
//
//   Example:
//     Input : s = ['h','e','l','l','o']
//     Output: ['o','l','l','e','h']
// =============================================================

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = (int)s.size() - 1;
        while (l < r) swap(s[l++], s[r--]);
    }
};

int main() {
    vector<char> s = {'h','e','l','l','o'};
    Solution().reverseString(s);
    for (char c : s) cout << c;
    cout << endl;
}
