# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 136 -- Car Pooling
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 68
# =============================================================
#
# QUESTION:
#   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
# =============================================================
def carPool(t,cap):
    e=[0]*1001
    for n,a,b in t: e[a]+=n; e[b]-=n
    s=0
    for v in e:
        s+=v
        if s>cap: return False
    return True

if __name__=="__main__":
    print(carPool([[2,1,5],[3,3,7]],4))
    print(carPool([[2,1,5],[3,3,7]],5))
