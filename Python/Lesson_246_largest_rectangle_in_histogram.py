# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 246 -- Largest Rectangle In Histogram
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 123
# =============================================================
#
# QUESTION:
#   Max rectangular area in histogram. Monotonic stack.
# =============================================================
def largestRect(h):
    st=[]; best=0; h=h+[0]
    for i,x in enumerate(h):
        while st and h[st[-1]]>x:
            top=st.pop()
            w=i if not st else i-st[-1]-1
            best=max(best,h[top]*w)
        st.append(i)
    return best
if __name__=="__main__":
    print(largestRect([2,1,5,6,2,3]))
