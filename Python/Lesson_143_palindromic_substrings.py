# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 143 -- Palindromic Substrings
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 72
# =============================================================
#
# QUESTION:
#   Count number of palindromic substrings in s.
# =============================================================
def count(s):
    c=0
    for i in range(len(s)):
        for a,b in [(i,i),(i,i+1)]:
            while a>=0 and b<len(s) and s[a]==s[b]: c+=1; a-=1; b+=1
    return c

if __name__=="__main__":
    print(count("abc")); print(count("aaa"))
