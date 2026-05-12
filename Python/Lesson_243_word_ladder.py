# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 243 -- Word Ladder
# Category   : Graphs
# Difficulty : Hard
# Study Plan : Day 122
# =============================================================
#
# QUESTION:
#   Shortest transformation sequence length from begin to end. BFS with wildcard buckets.
# =============================================================
from collections import defaultdict, deque
def ladderLength(b,e,wl):
    if e not in wl: return 0
    L=len(b); buckets=defaultdict(list)
    for w in wl:
        for i in range(L): buckets[w[:i]+'*'+w[i+1:]].append(w)
    q=deque([(b,1)]); seen={b}
    while q:
        w,d=q.popleft()
        if w==e: return d
        for i in range(L):
            for nb in buckets[w[:i]+'*'+w[i+1:]]:
                if nb not in seen: seen.add(nb); q.append((nb,d+1))
    return 0
if __name__=="__main__":
    print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
