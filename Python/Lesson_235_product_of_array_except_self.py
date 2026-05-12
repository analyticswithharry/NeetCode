# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 235 -- Product of Array Except Self
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 118
# =============================================================
#
# QUESTION:
#   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
# =============================================================
def productExceptSelf(n):
    out=[1]*len(n); p=1
    for i in range(len(n)): out[i]=p; p*=n[i]
    p=1
    for i in range(len(n)-1,-1,-1): out[i]*=p; p*=n[i]
    return out
if __name__=="__main__":
    print(productExceptSelf([1,2,3,4]))
