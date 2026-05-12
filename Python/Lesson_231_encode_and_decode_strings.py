# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 231 -- Encode and Decode Strings
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 116
# =============================================================
#
# QUESTION:
#   Length-prefix encoding for arbitrary strings.
# =============================================================
def encode(strs): return "".join(f"{len(s)}#{s}" for s in strs)
def decode(s):
    res=[]; i=0
    while i<len(s):
        j=s.index('#',i); n=int(s[i:j]); res.append(s[j+1:j+1+n]); i=j+1+n
    return res
if __name__=="__main__":
    e=encode(["hello","world","#42"]); print(e); print(decode(e))
