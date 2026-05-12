# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 148 -- Best Time to Buy And Sell Stock With Cooldown
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 74
# =============================================================
#
# QUESTION:
#   Stock prices; can do unlimited transactions but after selling must cooldown 1 day. Max profit.
# =============================================================
def maxP(p):
    hold=-p[0]; sold=0; rest=0
    for i in range(1,len(p)):
        h=max(hold,rest-p[i])
        s=hold+p[i]
        r=max(rest,sold)
        hold,sold,rest=h,s,r
    return max(sold,rest)

if __name__=="__main__":
    print(maxP([1,2,3,0,2]))
