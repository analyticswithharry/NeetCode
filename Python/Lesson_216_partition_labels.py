# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 216 -- Partition Labels
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 108
# =============================================================
#
# QUESTION:
#   Partition string so each char appears in at most one part. Return sizes.
# =============================================================
def partitionLabels(s):
    last={c:i for i,c in enumerate(s)}
    res=[]; start=0; end=0
    for i,c in enumerate(s):
        end=max(end,last[c])
        if i==end: res.append(end-start+1); start=i+1
    return res
if __name__=="__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))
