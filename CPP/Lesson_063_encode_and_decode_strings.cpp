// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 063 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Design encode/decode of a list of strings into one string and back.
//
//   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
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
class Codec { public:
    string encode(vector<string>& strs){ string r; for (auto& s: strs) r += to_string(s.size())+"#"+s; return r; }
    vector<string> decode(string s){ vector<string> out; size_t i=0;
        while (i < s.size()){ size_t j = s.find('#', i); int n = stoi(s.substr(i, j-i));
            out.push_back(s.substr(j+1, n)); i = j+1+n; } return out; }
};
int main(){ vector<string> v={"lint","code","love","you"}; Codec c; auto e=c.encode(v);
    cout<<e<<endl; for (auto& x: c.decode(e)) cout<<x<<" "; cout<<endl; }
