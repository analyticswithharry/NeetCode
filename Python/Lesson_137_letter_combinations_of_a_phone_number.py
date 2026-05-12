# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 137 -- Letter Combinations of a Phone Number
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 69
# =============================================================
#
# QUESTION:
#   Given digits 2-9, return all possible letter combinations the number could represent.
# =============================================================
def letters(d):
    if not d: return []
    m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=['']
    for c in d:
        res=[p+ch for p in res for ch in m[c]]
    return res

if __name__=="__main__":
    print(letters("23"))
