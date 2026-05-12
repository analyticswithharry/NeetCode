//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 061 -- Contains Duplicate
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Given an integer array nums, return true if any value appears at least twice.
//
//   Example: [1,2,3,1] -> true; [1,2,3,4] -> false
// =============================================================

package main
import "fmt"
func containsDuplicate(nums []int) bool {
    m := map[int]bool{}
    for _,n := range nums { if m[n] { return true }; m[n]=true }
    return false
}
func main(){ fmt.Println(containsDuplicate([]int{1,2,3,1}), containsDuplicate([]int{1,2,3,4})) }
