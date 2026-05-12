# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 239 -- Majority Element II
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 120
# =============================================================
#
# QUESTION:
#   All elements appearing more than n/3 times. Boyer-Moore variant.
# =============================================================
def majorityIII(nums):
    c1=c2=0; n1=n2=None
    for x in nums:
        if x==n1: c1+=1
        elif x==n2: c2+=1
        elif c1==0: n1=x; c1=1
        elif c2==0: n2=x; c2=1
        else: c1-=1; c2-=1
    return [n for n in {n1,n2} if n is not None and nums.count(n)>len(nums)//3]
if __name__=="__main__":
    print(majorityIII([3,2,3])); print(majorityIII([1,1,1,3,3,2,2,2]))
