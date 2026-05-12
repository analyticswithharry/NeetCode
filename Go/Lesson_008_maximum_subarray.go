//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 008 -- Maximum Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 4
// =============================================================
//
// QUESTION:
//   Given an integer array nums, find the contiguous subarray (containing
//   at least one number) which has the largest sum and return its sum.
//
//   Example:
//     Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
//     Output: 6   (subarray [4,-1,2,1])
// =============================================================

package main

import "fmt"

func maxSubArray(nums []int) int {
    best, cur := nums[0], nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > cur + nums[i] { cur = nums[i] } else { cur += nums[i] }
        if cur > best { best = cur }
    }
    return best
}

func main() { fmt.Println(maxSubArray([]int{-2,1,-3,4,-1,2,1,-5,4})) }
