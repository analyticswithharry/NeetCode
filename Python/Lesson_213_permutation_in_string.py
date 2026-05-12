# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 213 -- Permutation in String
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 107
# =============================================================
#
# QUESTION:
#   Return true if s2 contains a permutation of s1.
# =============================================================
def checkInclusion(s1,s2):
    if len(s1)>len(s2): return False
    a=[0]*26; b=[0]*26
    for c in s1: a[ord(c)-97]+=1
    for i,c in enumerate(s2):
        b[ord(c)-97]+=1
        if i>=len(s1): b[ord(s2[i-len(s1)])-97]-=1
        if a==b: return True
    return False
if __name__=="__main__":
    print(checkInclusion("ab","eidbaooo"))
    print(checkInclusion("ab","eidboaoo"))
