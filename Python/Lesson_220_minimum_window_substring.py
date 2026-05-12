# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 220 -- Minimum Window Substring
# Category   : Sliding Window
# Difficulty : Hard
# Study Plan : Day 110
# =============================================================
#
# QUESTION:
#   Smallest substring of s containing all chars of t.
# =============================================================
from collections import Counter
def minWindow(s,t):
    if not t: return ""
    need=Counter(t); have={}; need_n=len(need); have_n=0
    res=[-1,-1]; resl=float('inf'); l=0
    for r,c in enumerate(s):
        have[c]=have.get(c,0)+1
        if c in need and have[c]==need[c]: have_n+=1
        while have_n==need_n:
            if r-l+1<resl: res=[l,r]; resl=r-l+1
            have[s[l]]-=1
            if s[l] in need and have[s[l]]<need[s[l]]: have_n-=1
            l+=1
    return s[res[0]:res[1]+1] if resl!=float('inf') else ""
if __name__=="__main__":
    print(minWindow("ADOBECODEBANC","ABC"))
