// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 062 -- Valid Sudoku
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Determine if a 9x9 Sudoku board is valid (no duplicates in any row, column, or 3x3 box). Empty cells are '.'.
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
class Solution { public:
    bool isValidSudoku(vector<vector<char>>& b){
        set<string> s;
        for (int i=0;i<9;i++) for (int j=0;j<9;j++){
            char v=b[i][j]; if (v=='.') continue;
            string r="r"+to_string(i)+v, c="c"+to_string(j)+v, x="b"+to_string(i/3)+to_string(j/3)+v;
            if (!s.insert(r).second || !s.insert(c).second || !s.insert(x).second) return false;
        }
        return true;
    }
};
int main(){
    vector<vector<char>> b = {
        {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}};
    cout<<Solution().isValidSudoku(b)<<endl;
}
