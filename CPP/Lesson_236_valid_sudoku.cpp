// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 236 -- Valid Sudoku
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Validate 9x9 board: rows, cols, 3x3 boxes have unique 1-9 (ignore '.').
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
bool isValid(vector<vector<char>> b){set<string> s;for(int i=0;i<9;i++)for(int j=0;j<9;j++){char c=b[i][j];if(c=='.')continue;string r="r"+to_string(i)+c,co="c"+to_string(j)+c,k="b"+to_string(i/3)+to_string(j/3)+c;if(!s.insert(r).second||!s.insert(co).second||!s.insert(k).second)return false;}return true;}
int main(){vector<vector<char>> bd={{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};cout<<isValid(bd)<<"\n";}
