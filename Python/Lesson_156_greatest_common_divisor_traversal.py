# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 156 -- Greatest Common Divisor Traversal
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 78
# =============================================================
#
# QUESTION:
#   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
# =============================================================
from math import gcd
def can(a):
    n=len(a); par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    def u(x,y):
        x,y=f(x),f(y)
        if x!=y: par[x]=y
    pmap={}
    def primes(x):
        ps=[]; d=2
        while d*d<=x:
            if x%d==0:
                ps.append(d)
                while x%d==0: x//=d
            d+=1
        if x>1: ps.append(x)
        return ps
    for i,x in enumerate(a):
        for p in primes(x):
            if p in pmap: u(i,pmap[p])
            else: pmap[p]=i
    r=f(0)
    return all(f(i)==r for i in range(n))

if __name__=="__main__":
    print(can([2,3,6])); print(can([3,9,5])); print(can([4,3,12,8]))
