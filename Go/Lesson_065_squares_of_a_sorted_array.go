//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 065 -- Squares of a Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Given a sorted (non-decreasing) array, return an array of squares of each number, also sorted.
//
//   Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
// =============================================================

package main
import "fmt"
func abs(x int) int { if x<0 {return -x}; return x }
func sortedSquares(nums []int) []int {
    n := len(nums); out := make([]int,n); l,r,k := 0,n-1,n-1
    for l<=r { if abs(nums[l])>abs(nums[r]) { out[k]=nums[l]*nums[l]; l++ } else { out[k]=nums[r]*nums[r]; r-- }; k-- }
    return out
}
func main(){ fmt.Println(sortedSquares([]int{-4,-1,0,3,10})) }
