# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 063 -- Encode and Decode Strings
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 32
# =============================================================
#
# QUESTION:
#   Design encode/decode of a list of strings into one string and back.
#
#   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
# =============================================================

class Codec:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s):
        out, i = [], 0
        while i < len(s):
            j = s.index("#", i); n = int(s[i:j])
            out.append(s[j+1:j+1+n]); i = j+1+n
        return out

if __name__ == "__main__":
    c = Codec(); e = c.encode(["lint","code","love","you"])
    print(e); print(c.decode(e))
