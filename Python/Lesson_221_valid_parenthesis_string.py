# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 221 -- Valid Parenthesis String
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 111
# =============================================================
#
# QUESTION:
#   '*' can be '(' ')' or empty. Determine if string can be valid.
# =============================================================
def checkValid(s):
    lo=hi=0
    for c in s:
        lo+=1 if c=='(' else -1
        hi+=1 if c!=')' else -1
        if hi<0: return False
        lo=max(lo,0)
    return lo==0
if __name__=="__main__":
    print(checkValid("(*))"))
    print(checkValid("(*)"))
