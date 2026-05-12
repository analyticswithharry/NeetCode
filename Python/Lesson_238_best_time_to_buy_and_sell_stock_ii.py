# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 238 -- Best Time to Buy And Sell Stock II
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 119
# =============================================================
#
# QUESTION:
#   Multiple transactions allowed. Sum positive deltas.
# =============================================================
def maxProfit(p):
    return sum(max(0,p[i]-p[i-1]) for i in range(1,len(p)))
if __name__=="__main__":
    print(maxProfit([7,1,5,3,6,4]))
