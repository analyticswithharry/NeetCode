//go:build ignore

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

package main

import "fmt"

func reverseString(s []byte) {
    l, r := 0, len(s)-1
    for l < r { s[l], s[r] = s[r], s[l]; l++; r-- }
}

func main() {
    s := []byte("hello")
    reverseString(s)
    fmt.Println(string(s))
}
