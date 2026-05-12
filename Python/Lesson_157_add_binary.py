# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 157 -- Add Binary
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 79
# =============================================================
#
# QUESTION:
#   Given two binary strings, return their sum as a binary string.
# =============================================================
def addBin(a,b):
    return bin(int(a,2)+int(b,2))[2:]

if __name__=="__main__":
    print(addBin("11","1")); print(addBin("1010","1011"))
