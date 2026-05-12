# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 149 -- Daily Temperatures
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 75
# =============================================================
#
# QUESTION:
#   For each day, return number of days until a warmer temperature, or 0.
# =============================================================
def dailyT(t):
    res=[0]*len(t); st=[]
    for i,x in enumerate(t):
        while st and t[st[-1]]<x:
            j=st.pop(); res[j]=i-j
        st.append(i)
    return res

if __name__=="__main__":
    print(dailyT([73,74,75,71,69,72,76,73]))
