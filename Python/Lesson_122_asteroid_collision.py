# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 122 -- Asteroid Collision
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 61
# =============================================================
#
# QUESTION:
#   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
# =============================================================
def collide(a):
    st=[]
    for x in a:
        while st and x<0<st[-1]:
            if st[-1]<-x: st.pop(); continue
            elif st[-1]==-x: st.pop()
            break
        else:
            st.append(x)
    return st

if __name__=="__main__":
    print(collide([5,10,-5]))
    print(collide([8,-8]))
    print(collide([10,2,-5]))
