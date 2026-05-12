//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 066 -- Sort Colors
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0,1,2 in-place. Dutch National Flag.
//
//   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
// =============================================================

package main
import "fmt"
func sortColors(nums []int) []int {
    l,m,r := 0,0,len(nums)-1
    for m<=r {
        switch nums[m] {
        case 0: nums[l], nums[m] = nums[m], nums[l]; l++; m++
        case 2: nums[m], nums[r] = nums[r], nums[m]; r--
        default: m++
        }
    }
    return nums
}
func main(){ fmt.Println(sortColors([]int{2,0,2,1,1,0})) }
