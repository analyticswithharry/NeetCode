// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 067 -- Reverse Vowels of a String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
//
//   Example: hello -> holle
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
    string reverseVowels(string s){
        string v="aeiouAEIOU"; int l=0,r=s.size()-1;
        while (l<r){ while (l<r && v.find(s[l])==string::npos) l++; while (l<r && v.find(s[r])==string::npos) r--;
            swap(s[l],s[r]); l++; r--; }
        return s;
    }
};
int main(){ cout<<Solution().reverseVowels("hello")<<" "<<Solution().reverseVowels("leetcode")<<endl; }
