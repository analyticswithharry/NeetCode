//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 077 -- Find the Duplicate Number
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).
// =============================================================

package main
import "fmt"
func findDuplicate(nums []int) int {
    slow, fast := nums[0], nums[0]
    for { slow = nums[slow]; fast = nums[nums[fast]]; if slow == fast { break } }
    slow = nums[0]
    for slow != fast { slow = nums[slow]; fast = nums[fast] }
    return slow
}
func main(){ fmt.Println(findDuplicate([]int{1,3,4,2,2}), findDuplicate([]int{3,1,3,4,2})) }
