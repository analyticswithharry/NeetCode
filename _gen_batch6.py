"""Batch 6: lessons 111-135."""
from _lesson_writer import write_lessons

L = []

# 111 Single Number
L.append((111, "Single Number", "Bit Manipulation", "Easy", 56,
"Given a non-empty array of integers, every element appears twice except for one. Find that single one. O(1) extra space.",
{
"Python": '''def single(nums):
    r = 0
    for x in nums: r ^= x
    return r

if __name__ == "__main__":
    print(single([2,2,1]))
    print(single([4,1,2,1,2]))
''',
"JavaScript": '''function single(nums){let r=0;for(const x of nums)r^=x;return r;}
console.log(single([2,2,1]));
console.log(single([4,1,2,1,2]));
''',
"Java": '''public class __CLASS__{
  static int single(int[] a){int r=0;for(int x:a)r^=x;return r;}
  public static void main(String[] a){System.out.println(single(new int[]{2,2,1}));System.out.println(single(new int[]{4,1,2,1,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int single(vector<int>&a){int r=0;for(int x:a)r^=x;return r;}
int main(){cout<<single(*new vector<int>{2,2,1})<<"\\n"<<single(*new vector<int>{4,1,2,1,2})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func single(a []int) int { r:=0; for _,x:=range a { r^=x }; return r }
func main(){ fmt.Println(single([]int{2,2,1})); fmt.Println(single([]int{4,1,2,1,2})) }
''',
"R": '''single <- function(a) Reduce(bitwXor, a, 0)
cat(single(c(2,2,1)),"\\n"); cat(single(c(4,1,2,1,2)),"\\n")
''',
}))

# 112 Sum of Two Integers
L.append((112, "Sum of Two Integers", "Bit Manipulation", "Medium", 56,
"Given two integers a and b, return the sum without using + or -.",
{
"Python": '''def add(a,b):
    M=0xFFFFFFFF
    while b & M:
        c=((a & b) << 1) & M
        a=(a ^ b) & M
        b=c
    return a if a<=0x7FFFFFFF else ~(a^M)

if __name__=="__main__":
    print(add(1,2)); print(add(-2,3))
''',
"JavaScript": '''function add(a,b){while(b!==0){const c=(a&b)<<1;a=a^b;b=c;}return a|0;}
console.log(add(1,2));console.log(add(-2,3));
''',
"Java": '''public class __CLASS__{
  static int add(int a,int b){while(b!=0){int c=(a&b)<<1;a=a^b;b=c;}return a;}
  public static void main(String[]x){System.out.println(add(1,2));System.out.println(add(-2,3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int add(int a,int b){while(b){int c=(unsigned)(a&b)<<1;a=a^b;b=c;}return a;}
int main(){cout<<add(1,2)<<"\\n"<<add(-2,3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func add(a,b int) int { for b!=0 { c:=(a&b)<<1; a=a^b; b=c }; return a }
func main(){ fmt.Println(add(1,2)); fmt.Println(add(-2,3)) }
''',
"R": '''add <- function(a,b){ while(b!=0){ c <- bitwShiftL(bitwAnd(a,b),1); a <- bitwXor(a,b); b <- c }; a }
cat(add(1,2),"\\n"); cat(add(-2,3),"\\n")
''',
}))

# 113 Search Rotated Sorted Array
L.append((113, "Search In Rotated Sorted Array", "Binary Search", "Medium", 57,
"Given a rotated sorted array (no duplicates) and target, return index or -1. O(log n).",
{
"Python": '''def search(a,t):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t: return m
        if a[lo]<=a[m]:
            if a[lo]<=t<a[m]: hi=m-1
            else: lo=m+1
        else:
            if a[m]<t<=a[hi]: lo=m+1
            else: hi=m-1
    return -1

if __name__=="__main__":
    print(search([4,5,6,7,0,1,2],0))
    print(search([4,5,6,7,0,1,2],3))
''',
"JavaScript": '''function search(a,t){let lo=0,hi=a.length-1;while(lo<=hi){const m=(lo+hi)>>1;if(a[m]===t)return m;if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return -1;}
console.log(search([4,5,6,7,0,1,2],0));
console.log(search([4,5,6,7,0,1,2],3));
''',
"Java": '''public class __CLASS__{
  static int search(int[]a,int t){int lo=0,hi=a.length-1;while(lo<=hi){int m=(lo+hi)>>>1;if(a[m]==t)return m;if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return -1;}
  public static void main(String[]x){System.out.println(search(new int[]{4,5,6,7,0,1,2},0));System.out.println(search(new int[]{4,5,6,7,0,1,2},3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int search(vector<int>&a,int t){int lo=0,hi=a.size()-1;while(lo<=hi){int m=(lo+hi)/2;if(a[m]==t)return m;if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return -1;}
int main(){vector<int> v={4,5,6,7,0,1,2};cout<<search(v,0)<<"\\n"<<search(v,3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func search(a []int,t int) int { lo,hi:=0,len(a)-1; for lo<=hi { m:=(lo+hi)/2; if a[m]==t { return m }; if a[lo]<=a[m] { if a[lo]<=t && t<a[m] { hi=m-1 } else { lo=m+1 } } else { if a[m]<t && t<=a[hi] { lo=m+1 } else { hi=m-1 } } }; return -1 }
func main(){ a:=[]int{4,5,6,7,0,1,2}; fmt.Println(search(a,0)); fmt.Println(search(a,3)) }
''',
"R": '''search <- function(a,t){ lo<-1;hi<-length(a); while(lo<=hi){ m<-(lo+hi)%/%2; if(a[m]==t)return(m-1); if(a[lo]<=a[m]){ if(a[lo]<=t && t<a[m]) hi<-m-1 else lo<-m+1 } else { if(a[m]<t && t<=a[hi]) lo<-m+1 else hi<-m-1 } }; -1 }
cat(search(c(4,5,6,7,0,1,2),0),"\\n"); cat(search(c(4,5,6,7,0,1,2),3),"\\n")
''',
}))

# 114 Search in Rotated Sorted Array II (with duplicates)
L.append((114, "Search In Rotated Sorted Array II", "Binary Search", "Medium", 57,
"Rotated sorted array may contain duplicates. Return true if target exists.",
{
"Python": '''def search(a,t):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t: return True
        if a[lo]==a[m]==a[hi]: lo+=1; hi-=1
        elif a[lo]<=a[m]:
            if a[lo]<=t<a[m]: hi=m-1
            else: lo=m+1
        else:
            if a[m]<t<=a[hi]: lo=m+1
            else: hi=m-1
    return False

if __name__=="__main__":
    print(search([2,5,6,0,0,1,2],0))
    print(search([2,5,6,0,0,1,2],3))
''',
"JavaScript": '''function search(a,t){let lo=0,hi=a.length-1;while(lo<=hi){const m=(lo+hi)>>1;if(a[m]===t)return true;if(a[lo]===a[m]&&a[m]===a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
console.log(search([2,5,6,0,0,1,2],0));
console.log(search([2,5,6,0,0,1,2],3));
''',
"Java": '''public class __CLASS__{
  static boolean search(int[]a,int t){int lo=0,hi=a.length-1;while(lo<=hi){int m=(lo+hi)>>>1;if(a[m]==t)return true;if(a[lo]==a[m]&&a[m]==a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
  public static void main(String[]x){System.out.println(search(new int[]{2,5,6,0,0,1,2},0));System.out.println(search(new int[]{2,5,6,0,0,1,2},3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool search(vector<int>&a,int t){int lo=0,hi=a.size()-1;while(lo<=hi){int m=(lo+hi)/2;if(a[m]==t)return true;if(a[lo]==a[m]&&a[m]==a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
int main(){vector<int>v={2,5,6,0,0,1,2};cout<<boolalpha<<search(v,0)<<"\\n"<<search(v,3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func search(a []int,t int) bool { lo,hi:=0,len(a)-1; for lo<=hi { m:=(lo+hi)/2; if a[m]==t { return true }; if a[lo]==a[m] && a[m]==a[hi] { lo++; hi-- } else if a[lo]<=a[m] { if a[lo]<=t && t<a[m] { hi=m-1 } else { lo=m+1 } } else { if a[m]<t && t<=a[hi] { lo=m+1 } else { hi=m-1 } } }; return false }
func main(){ a:=[]int{2,5,6,0,0,1,2}; fmt.Println(search(a,0)); fmt.Println(search(a,3)) }
''',
"R": '''search <- function(a,t){ lo<-1;hi<-length(a); while(lo<=hi){ m<-(lo+hi)%/%2; if(a[m]==t) return(TRUE); if(a[lo]==a[m] && a[m]==a[hi]){ lo<-lo+1; hi<-hi-1 } else if(a[lo]<=a[m]){ if(a[lo]<=t && t<a[m]) hi<-m-1 else lo<-m+1 } else { if(a[m]<t && t<=a[hi]) lo<-m+1 else hi<-m-1 } }; FALSE }
cat(search(c(2,5,6,0,0,1,2),0),"\\n"); cat(search(c(2,5,6,0,0,1,2),3),"\\n")
''',
}))

# 115 Plus One
L.append((115, "Plus One", "Math and Geometry", "Easy", 58,
"Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.",
{
"Python": '''def plusOne(d):
    d=d[:]
    for i in range(len(d)-1,-1,-1):
        if d[i]<9: d[i]+=1; return d
        d[i]=0
    return [1]+d

if __name__=="__main__":
    print(plusOne([1,2,3]))
    print(plusOne([9,9]))
''',
"JavaScript": '''function plusOne(d){d=d.slice();for(let i=d.length-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}return [1,...d];}
console.log(plusOne([1,2,3]));console.log(plusOne([9,9]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] plusOne(int[]d){d=d.clone();for(int i=d.length-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}int[] r=new int[d.length+1];r[0]=1;return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(plusOne(new int[]{1,2,3})));System.out.println(Arrays.toString(plusOne(new int[]{9,9})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> plusOne(vector<int> d){for(int i=d.size()-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}d.insert(d.begin(),1);return d;}
int main(){auto a=plusOne({1,2,3});for(int x:a)cout<<x<<" ";cout<<"\\n";auto b=plusOne({9,9});for(int x:b)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func plusOne(d []int) []int { d=append([]int{},d...); for i:=len(d)-1;i>=0;i-- { if d[i]<9 { d[i]++; return d }; d[i]=0 }; return append([]int{1},d...) }
func main(){ fmt.Println(plusOne([]int{1,2,3})); fmt.Println(plusOne([]int{9,9})) }
''',
"R": '''plusOne <- function(d){ for(i in length(d):1){ if(d[i]<9){ d[i]<-d[i]+1; return(d) }; d[i]<-0 }; c(1,d) }
print(plusOne(c(1,2,3))); print(plusOne(c(9,9)))
''',
}))

# 116 Spiral Matrix
L.append((116, "Spiral Matrix", "Math and Geometry", "Medium", 58,
"Given m x n matrix, return all elements in spiral order.",
{
"Python": '''def spiral(m):
    res=[]
    if not m: return res
    t,b,l,r=0,len(m)-1,0,len(m[0])-1
    while t<=b and l<=r:
        for j in range(l,r+1): res.append(m[t][j])
        t+=1
        for i in range(t,b+1): res.append(m[i][r])
        r-=1
        if t<=b:
            for j in range(r,l-1,-1): res.append(m[b][j])
            b-=1
        if l<=r:
            for i in range(b,t-1,-1): res.append(m[i][l])
            l+=1
    return res

if __name__=="__main__":
    print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
''',
"JavaScript": '''function spiral(m){const res=[];if(!m.length)return res;let t=0,b=m.length-1,l=0,r=m[0].length-1;while(t<=b&&l<=r){for(let j=l;j<=r;j++)res.push(m[t][j]);t++;for(let i=t;i<=b;i++)res.push(m[i][r]);r--;if(t<=b){for(let j=r;j>=l;j--)res.push(m[b][j]);b--;}if(l<=r){for(let i=b;i>=t;i--)res.push(m[i][l]);l++;}}return res;}
console.log(spiral([[1,2,3],[4,5,6],[7,8,9]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Integer> spiral(int[][]m){List<Integer> r=new ArrayList<>();if(m.length==0)return r;int t=0,b=m.length-1,l=0,rg=m[0].length-1;while(t<=b&&l<=rg){for(int j=l;j<=rg;j++)r.add(m[t][j]);t++;for(int i=t;i<=b;i++)r.add(m[i][rg]);rg--;if(t<=b){for(int j=rg;j>=l;j--)r.add(m[b][j]);b--;}if(l<=rg){for(int i=b;i>=t;i--)r.add(m[i][l]);l++;}}return r;}
  public static void main(String[]x){System.out.println(spiral(new int[][]{{1,2,3},{4,5,6},{7,8,9}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> spiral(vector<vector<int>>&m){vector<int> r;if(m.empty())return r;int t=0,b=m.size()-1,l=0,rg=m[0].size()-1;while(t<=b&&l<=rg){for(int j=l;j<=rg;j++)r.push_back(m[t][j]);t++;for(int i=t;i<=b;i++)r.push_back(m[i][rg]);rg--;if(t<=b){for(int j=rg;j>=l;j--)r.push_back(m[b][j]);b--;}if(l<=rg){for(int i=b;i>=t;i--)r.push_back(m[i][l]);l++;}}return r;}
int main(){vector<vector<int>> m={{1,2,3},{4,5,6},{7,8,9}};auto r=spiral(m);for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func spiral(m [][]int) []int { var r []int; if len(m)==0 { return r }; t,b,l,rg:=0,len(m)-1,0,len(m[0])-1; for t<=b && l<=rg { for j:=l;j<=rg;j++ { r=append(r,m[t][j]) }; t++; for i:=t;i<=b;i++ { r=append(r,m[i][rg]) }; rg--; if t<=b { for j:=rg;j>=l;j-- { r=append(r,m[b][j]) }; b-- }; if l<=rg { for i:=b;i>=t;i-- { r=append(r,m[i][l]) }; l++ } }; return r }
func main(){ fmt.Println(spiral([][]int{{1,2,3},{4,5,6},{7,8,9}})) }
''',
"R": '''spiral <- function(m){ r<-c(); if(length(m)==0) return(r); t<-1;b<-nrow(m);l<-1;rg<-ncol(m); while(t<=b && l<=rg){ for(j in l:rg) r<-c(r,m[t,j]); t<-t+1; if(t<=b) for(i in t:b) r<-c(r,m[i,rg]); rg<-rg-1; if(t<=b && l<=rg) for(j in rg:l) r<-c(r,m[b,j]); b<-b-1; if(l<=rg && t<=b) for(i in b:t) r<-c(r,m[i,l]); l<-l+1 }; r }
print(spiral(matrix(1:9,3,3,byrow=TRUE)))
''',
}))

# 117 Meeting Rooms II
L.append((117, "Meeting Rooms II", "Intervals", "Medium", 59,
"Given an array of meeting time intervals, return the minimum number of conference rooms required.",
{
"Python": '''import heapq
def minRooms(it):
    it.sort(key=lambda x:x[0]); h=[]
    for s,e in it:
        if h and h[0]<=s: heapq.heappop(h)
        heapq.heappush(h,e)
    return len(h)

if __name__=="__main__":
    print(minRooms([[0,30],[5,10],[15,20]]))
    print(minRooms([[7,10],[2,4]]))
''',
"JavaScript": '''function minRooms(it){it.sort((a,b)=>a[0]-b[0]);const h=[];for(const [s,e] of it){let mi=0;for(let i=1;i<h.length;i++)if(h[i]<h[mi])mi=i;if(h.length&&h[mi]<=s)h.splice(mi,1);h.push(e);}return h.length;}
console.log(minRooms([[0,30],[5,10],[15,20]]));
console.log(minRooms([[7,10],[2,4]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int minRooms(int[][]it){Arrays.sort(it,(a,b)->a[0]-b[0]);PriorityQueue<Integer> h=new PriorityQueue<>();for(int[] x:it){if(!h.isEmpty()&&h.peek()<=x[0])h.poll();h.add(x[1]);}return h.size();}
  public static void main(String[]x){System.out.println(minRooms(new int[][]{{0,30},{5,10},{15,20}}));System.out.println(minRooms(new int[][]{{7,10},{2,4}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int minRooms(vector<vector<int>> it){sort(it.begin(),it.end());priority_queue<int,vector<int>,greater<int>> h;for(auto& x:it){if(!h.empty()&&h.top()<=x[0])h.pop();h.push(x[1]);}return h.size();}
int main(){cout<<minRooms({{0,30},{5,10},{15,20}})<<"\\n"<<minRooms({{7,10},{2,4}})<<"\\n";}
''',
"Go": '''package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func minRooms(it [][]int) int { sort.Slice(it,func(i,j int) bool{return it[i][0]<it[j][0]}); h:=&IH{}; heap.Init(h); for _,x:=range it { if h.Len()>0 && (*h)[0]<=x[0] { heap.Pop(h) }; heap.Push(h,x[1]) }; return h.Len() }
func main(){ fmt.Println(minRooms([][]int{{0,30},{5,10},{15,20}})); fmt.Println(minRooms([][]int{{7,10},{2,4}})) }
''',
"R": '''minRooms <- function(it){ it <- it[order(sapply(it,`[`,1))]; h<-c(); for(x in it){ if(length(h)>0 && min(h)<=x[1]){ h<-h[-which.min(h)] }; h<-c(h,x[2]) }; length(h) }
cat(minRooms(list(c(0,30),c(5,10),c(15,20))),"\\n"); cat(minRooms(list(c(7,10),c(2,4))),"\\n")
''',
}))

# 118 Meeting Rooms III
L.append((118, "Meeting Rooms III", "Intervals", "Hard", 59,
"Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.",
{
"Python": '''import heapq
def mostBooked(n, meets):
    meets.sort()
    free=list(range(n))
    heapq.heapify(free)
    busy=[]  # (endTime, room)
    cnt=[0]*n
    for s,e in meets:
        while busy and busy[0][0]<=s:
            _,r=heapq.heappop(busy); heapq.heappush(free,r)
        if free:
            r=heapq.heappop(free)
            heapq.heappush(busy,(e,r))
        else:
            t,r=heapq.heappop(busy)
            heapq.heappush(busy,(t+e-s,r))
        cnt[r]+=1
    return cnt.index(max(cnt))

if __name__=="__main__":
    print(mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]))
''',
"JavaScript": '''function mostBooked(n,meets){meets.sort((a,b)=>a[0]-b[0]);const free=Array.from({length:n},(_,i)=>i);const busy=[];const cnt=new Array(n).fill(0);const popMin=arr=>{let mi=0;for(let i=1;i<arr.length;i++)if(Array.isArray(arr[i])?(arr[i][0]<arr[mi][0]||(arr[i][0]===arr[mi][0]&&arr[i][1]<arr[mi][1])):arr[i]<arr[mi])mi=i;return arr.splice(mi,1)[0];};for(const [s,e] of meets){for(let i=busy.length-1;i>=0;i--)if(busy[i][0]<=s){free.push(busy[i][1]);busy.splice(i,1);}if(free.length){const r=popMin(free);busy.push([e,r]);cnt[r]++;}else{const [t,r]=popMin(busy);busy.push([t+e-s,r]);cnt[r]++;}}let mi=0;for(let i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
console.log(mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int mostBooked(int n,int[][]m){Arrays.sort(m,(a,b)->a[0]-b[0]);PriorityQueue<Integer> free=new PriorityQueue<>();for(int i=0;i<n;i++)free.add(i);PriorityQueue<long[]> busy=new PriorityQueue<>((a,b)->a[0]!=b[0]?Long.compare(a[0],b[0]):Long.compare(a[1],b[1]));long[] cnt=new long[n];for(int[] x:m){while(!busy.isEmpty()&&busy.peek()[0]<=x[0]){free.add((int)busy.poll()[1]);}int r;long e;if(!free.isEmpty()){r=free.poll();e=x[1];}else{long[] top=busy.poll();r=(int)top[1];e=top[0]+x[1]-x[0];}busy.add(new long[]{e,r});cnt[r]++;}int mi=0;for(int i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
  public static void main(String[]x){System.out.println(mostBooked(2,new int[][]{{0,10},{1,5},{2,7},{3,4}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int mostBooked(int n,vector<vector<int>> m){sort(m.begin(),m.end());priority_queue<int,vector<int>,greater<int>> fr;for(int i=0;i<n;i++)fr.push(i);priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<>> busy;vector<long long> cnt(n,0);for(auto& x:m){while(!busy.empty()&&busy.top().first<=x[0]){fr.push(busy.top().second);busy.pop();}int r; long long e;if(!fr.empty()){r=fr.top();fr.pop();e=x[1];}else{auto t=busy.top();busy.pop();r=t.second;e=t.first+x[1]-x[0];}busy.push({e,r});cnt[r]++;}int mi=0;for(int i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
int main(){cout<<mostBooked(2,{{0,10},{1,5},{2,7},{3,4}})<<"\\n";}
''',
"Go": '''package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
type Pair struct{ T int64; R int }
type PH []Pair
func (h PH) Len() int{return len(h)}; func (h PH) Less(i,j int) bool{ if h[i].T!=h[j].T{return h[i].T<h[j].T}; return h[i].R<h[j].R }; func (h PH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *PH) Push(x any){*h=append(*h,x.(Pair))}; func (h *PH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func mostBooked(n int, m [][]int) int { sort.Slice(m,func(i,j int) bool{return m[i][0]<m[j][0]}); fr:=&IH{}; for i:=0;i<n;i++{ heap.Push(fr,i) }; busy:=&PH{}; cnt:=make([]int64,n); for _,x:=range m { for busy.Len()>0 && (*busy)[0].T<=int64(x[0]) { p:=heap.Pop(busy).(Pair); heap.Push(fr,p.R) }; var r int; var e int64; if fr.Len()>0 { r=heap.Pop(fr).(int); e=int64(x[1]) } else { p:=heap.Pop(busy).(Pair); r=p.R; e=p.T+int64(x[1]-x[0]) }; heap.Push(busy,Pair{e,r}); cnt[r]++ }; mi:=0; for i:=1;i<n;i++{ if cnt[i]>cnt[mi]{ mi=i } }; return mi }
func main(){ fmt.Println(mostBooked(2,[][]int{{0,10},{1,5},{2,7},{3,4}})) }
''',
"R": '''mostBooked <- function(n,m){ m <- m[order(sapply(m,`[`,1))]; fr <- 0:(n-1); busy <- list(); cnt <- rep(0,n); for(x in m){ keep<-c(); for(i in seq_along(busy)){ if(busy[[i]][1]<=x[1]){ fr<-c(fr,busy[[i]][2]) } else keep<-c(keep,i) }; busy<-busy[keep]; if(length(fr)>0){ r<-min(fr); fr<-fr[fr!=r]; e<-x[2] } else { ts<-sapply(busy,`[`,1); k<-which.min(ts); r<-busy[[k]][2]; e<-busy[[k]][1]+x[2]-x[1]; busy<-busy[-k] }; busy[[length(busy)+1]] <- c(e,r); cnt[r+1]<-cnt[r+1]+1 }; which.max(cnt)-1 }
cat(mostBooked(2,list(c(0,10),c(1,5),c(2,7),c(3,4))),"\\n")
''',
}))

# 119 Max Area Island
L.append((119, "Max Area of Island", "Graphs", "Medium", 60,
"Given m x n binary grid, return max area of an island (4-directionally connected 1s).",
{
"Python": '''def maxArea(g):
    m,n=len(g),len(g[0]); best=0
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or g[i][j]!=1: return 0
        g[i][j]=0
        return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
    for i in range(m):
        for j in range(n):
            if g[i][j]==1: best=max(best,dfs(i,j))
    return best

if __name__=="__main__":
    print(maxArea([[1,1,0],[1,0,0],[0,0,1]]))
''',
"JavaScript": '''function maxArea(g){const m=g.length,n=g[0].length;let best=0;function dfs(i,j){if(i<0||j<0||i>=m||j>=n||g[i][j]!==1)return 0;g[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}for(let i=0;i<m;i++)for(let j=0;j<n;j++)if(g[i][j]===1)best=Math.max(best,dfs(i,j));return best;}
console.log(maxArea([[1,1,0],[1,0,0],[0,0,1]]));
''',
"Java": '''public class __CLASS__{
  static int M,N; static int[][] G;
  static int dfs(int i,int j){if(i<0||j<0||i>=M||j>=N||G[i][j]!=1)return 0;G[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}
  static int maxArea(int[][]g){G=g;M=g.length;N=g[0].length;int b=0;for(int i=0;i<M;i++)for(int j=0;j<N;j++)if(g[i][j]==1)b=Math.max(b,dfs(i,j));return b;}
  public static void main(String[]x){System.out.println(maxArea(new int[][]{{1,1,0},{1,0,0},{0,0,1}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int M,N; vector<vector<int>>* G;
int dfs(int i,int j){if(i<0||j<0||i>=M||j>=N||(*G)[i][j]!=1)return 0;(*G)[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}
int maxArea(vector<vector<int>> g){G=&g;M=g.size();N=g[0].size();int b=0;for(int i=0;i<M;i++)for(int j=0;j<N;j++)if(g[i][j]==1)b=max(b,dfs(i,j));return b;}
int main(){cout<<maxArea({{1,1,0},{1,0,0},{0,0,1}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxArea(g [][]int) int { m,n:=len(g),len(g[0]); var dfs func(i,j int) int; dfs=func(i,j int) int { if i<0||j<0||i>=m||j>=n||g[i][j]!=1 { return 0 }; g[i][j]=0; return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1) }; b:=0; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==1 { v:=dfs(i,j); if v>b { b=v } } } }; return b }
func main(){ fmt.Println(maxArea([][]int{{1,1,0},{1,0,0},{0,0,1}})) }
''',
"R": '''maxArea <- function(g){ m<-nrow(g); n<-ncol(g); dfs <- function(i,j){ if(i<1||j<1||i>m||j>n||g[i,j]!=1) return(0); g[i,j] <<- 0; 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1) }; b<-0; for(i in 1:m) for(j in 1:n) if(g[i,j]==1) b<-max(b,dfs(i,j)); b }
g <- matrix(c(1,1,0,1,0,0,0,0,1),3,3,byrow=TRUE); cat(maxArea(g),"\\n")
''',
}))

# 120 Clone Graph
L.append((120, "Clone Graph", "Graphs", "Medium", 60,
"Given a node in a connected undirected graph, return a deep copy of the graph.",
{
"Python": '''class Node:
    def __init__(self,v,nei=None): self.val=v; self.neighbors=nei or []

def clone(n):
    if not n: return None
    seen={}
    def dfs(x):
        if x in seen: return seen[x]
        c=Node(x.val); seen[x]=c
        for y in x.neighbors: c.neighbors.append(dfs(y))
        return c
    return dfs(n)

if __name__=="__main__":
    a=Node(1); b=Node(2); a.neighbors=[b]; b.neighbors=[a]
    c=clone(a); print(c.val, c.neighbors[0].val, c.neighbors[0].neighbors[0].val)
''',
"JavaScript": '''class Node{constructor(v,n=[]){this.val=v;this.neighbors=n;}}
function clone(n){if(!n)return null;const seen=new Map();function dfs(x){if(seen.has(x))return seen.get(x);const c=new Node(x.val);seen.set(x,c);for(const y of x.neighbors)c.neighbors.push(dfs(y));return c;}return dfs(n);}
const a=new Node(1),b=new Node(2);a.neighbors=[b];b.neighbors=[a];const c=clone(a);console.log(c.val,c.neighbors[0].val,c.neighbors[0].neighbors[0].val);
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class Node{int val;List<Node> neighbors=new ArrayList<>();Node(int v){val=v;}}
  static Map<Node,Node> seen=new HashMap<>();
  static Node clone(Node n){if(n==null)return null;if(seen.containsKey(n))return seen.get(n);Node c=new Node(n.val);seen.put(n,c);for(Node y:n.neighbors)c.neighbors.add(clone(y));return c;}
  public static void main(String[]x){Node a=new Node(1),b=new Node(2);a.neighbors.add(b);b.neighbors.add(a);Node c=clone(a);System.out.println(c.val+" "+c.neighbors.get(0).val+" "+c.neighbors.get(0).neighbors.get(0).val);}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct Node{int val; vector<Node*> neighbors; Node(int v):val(v){}};
unordered_map<Node*,Node*> seen;
Node* clone(Node* n){if(!n)return nullptr;if(seen.count(n))return seen[n];Node* c=new Node(n->val);seen[n]=c;for(auto y:n->neighbors)c->neighbors.push_back(clone(y));return c;}
int main(){Node a(1),b(2);a.neighbors={&b};b.neighbors={&a};Node* c=clone(&a);cout<<c->val<<" "<<c->neighbors[0]->val<<" "<<c->neighbors[0]->neighbors[0]->val<<"\\n";}
''',
"Go": '''package main
import "fmt"
type Node struct{ Val int; Neighbors []*Node }
func clone(n *Node, seen map[*Node]*Node) *Node { if n==nil { return nil }; if c,ok:=seen[n]; ok { return c }; c:=&Node{Val:n.Val}; seen[n]=c; for _,y:=range n.Neighbors { c.Neighbors=append(c.Neighbors,clone(y,seen)) }; return c }
func main(){ a:=&Node{Val:1}; b:=&Node{Val:2}; a.Neighbors=[]*Node{b}; b.Neighbors=[]*Node{a}; c:=clone(a,map[*Node]*Node{}); fmt.Println(c.Val, c.Neighbors[0].Val, c.Neighbors[0].Neighbors[0].Val) }
''',
"R": '''# Simulate clone via id refs
clone <- function(adj){ adj } # adjacency-list copy is the deep-copy in R
adj <- list(`1`=c(2), `2`=c(1)); print(clone(adj))
''',
}))

# 121 Generate Parentheses
L.append((121, "Generate Parentheses", "Stack", "Medium", 61,
"Given n pairs of parentheses, generate all combinations of well-formed parentheses.",
{
"Python": '''def gen(n):
    res=[]
    def rec(s,o,c):
        if len(s)==2*n: res.append(s); return
        if o<n: rec(s+"(",o+1,c)
        if c<o: rec(s+")",o,c+1)
    rec("",0,0); return res

if __name__=="__main__":
    print(gen(3))
''',
"JavaScript": '''function gen(n){const res=[];function rec(s,o,c){if(s.length===2*n){res.push(s);return;}if(o<n)rec(s+"(",o+1,c);if(c<o)rec(s+")",o,c+1);}rec("",0,0);return res;}
console.log(gen(3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<String> R=new ArrayList<>(); static int N;
  static void rec(String s,int o,int c){if(s.length()==2*N){R.add(s);return;}if(o<N)rec(s+"(",o+1,c);if(c<o)rec(s+")",o,c+1);}
  static List<String> gen(int n){R.clear();N=n;rec("",0,0);return R;}
  public static void main(String[]x){System.out.println(gen(3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<string> R; int N;
void rec(string s,int o,int c){if((int)s.size()==2*N){R.push_back(s);return;}if(o<N)rec(s+"(",o+1,c);if(c<o)rec(s+")",o,c+1);}
vector<string> gen(int n){R.clear();N=n;rec("",0,0);return R;}
int main(){auto v=gen(3);for(auto&s:v)cout<<s<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func gen(n int) []string { var r []string; var rec func(s string,o,c int); rec=func(s string,o,c int){ if len(s)==2*n { r=append(r,s); return }; if o<n { rec(s+"(",o+1,c) }; if c<o { rec(s+")",o,c+1) } }; rec("",0,0); return r }
func main(){ fmt.Println(gen(3)) }
''',
"R": '''gen <- function(n){ r<-c(); rec <- function(s,o,c){ if(nchar(s)==2*n){ r[[length(r)+1]]<<-s; return() }; if(o<n) rec(paste0(s,"("),o+1,c); if(c<o) rec(paste0(s,")"),o,c+1) }; rec("",0,0); r }
print(gen(3))
''',
}))

# 122 Asteroid Collision
L.append((122, "Asteroid Collision", "Stack", "Medium", 61,
"Given an array of asteroids (positive=right, negative=left), return state after all collisions.",
{
"Python": '''def collide(a):
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
''',
"JavaScript": '''function collide(a){const st=[];outer: for(const x of a){while(st.length&&x<0&&st[st.length-1]>0){if(st[st.length-1]<-x){st.pop();continue;}else if(st[st.length-1]===-x){st.pop();}continue outer;}st.push(x);}return st;}
console.log(collide([5,10,-5]));console.log(collide([8,-8]));console.log(collide([10,2,-5]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] collide(int[]a){Deque<Integer> st=new ArrayDeque<>();outer: for(int x:a){while(!st.isEmpty()&&x<0&&st.peek()>0){if(st.peek()<-x){st.pop();continue;}else if(st.peek()==-x){st.pop();}continue outer;}st.push(x);}int[] r=new int[st.size()];for(int i=r.length-1;i>=0;i--)r[i]=st.pop();return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(collide(new int[]{5,10,-5})));System.out.println(Arrays.toString(collide(new int[]{8,-8})));System.out.println(Arrays.toString(collide(new int[]{10,2,-5})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> collide(vector<int> a){vector<int> st;for(int x:a){bool alive=true;while(alive&&!st.empty()&&x<0&&st.back()>0){if(st.back()<-x){st.pop_back();}else if(st.back()==-x){st.pop_back();alive=false;}else alive=false;}if(alive)st.push_back(x);}return st;}
int main(){auto a=collide({5,10,-5});for(int x:a)cout<<x<<" ";cout<<"\\n";auto b=collide({8,-8});for(int x:b)cout<<x<<" ";cout<<"\\n";auto c=collide({10,2,-5});for(int x:c)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func collide(a []int) []int { var st []int; outer: for _,x:=range a { for len(st)>0 && x<0 && st[len(st)-1]>0 { if st[len(st)-1]<-x { st=st[:len(st)-1]; continue }; if st[len(st)-1]==-x { st=st[:len(st)-1] }; continue outer }; st=append(st,x) }; return st }
func main(){ fmt.Println(collide([]int{5,10,-5})); fmt.Println(collide([]int{8,-8})); fmt.Println(collide([]int{10,2,-5})) }
''',
"R": '''collide <- function(a){ st<-c(); for(x in a){ alive<-TRUE; while(alive && length(st)>0 && x<0 && st[length(st)]>0){ if(st[length(st)] < -x){ st<-st[-length(st)] } else if(st[length(st)] == -x){ st<-st[-length(st)]; alive<-FALSE } else alive<-FALSE }; if(alive) st<-c(st,x) }; st }
print(collide(c(5,10,-5))); print(collide(c(8,-8))); print(collide(c(10,2,-5)))
''',
}))

# 123 Design HashSet
L.append((123, "Design HashSet", "Arrays and Hashing", "Easy", 62,
"Design a HashSet (without built-in set): add, remove, contains.",
{
"Python": '''class MyHashSet:
    def __init__(self): self.b=[[] for _ in range(769)]
    def _h(self,k): return k%769
    def add(self,k):
        b=self.b[self._h(k)]
        if k not in b: b.append(k)
    def remove(self,k):
        b=self.b[self._h(k)]
        if k in b: b.remove(k)
    def contains(self,k): return k in self.b[self._h(k)]

if __name__=="__main__":
    s=MyHashSet(); s.add(1); s.add(2); print(s.contains(1), s.contains(3)); s.remove(2); print(s.contains(2))
''',
"JavaScript": '''class MyHashSet{constructor(){this.b=Array.from({length:769},()=>[]);}_h(k){return k%769;}add(k){const b=this.b[this._h(k)];if(!b.includes(k))b.push(k);}remove(k){const b=this.b[this._h(k)];const i=b.indexOf(k);if(i>=0)b.splice(i,1);}contains(k){return this.b[this._h(k)].includes(k);}}
const s=new MyHashSet();s.add(1);s.add(2);console.log(s.contains(1),s.contains(3));s.remove(2);console.log(s.contains(2));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class MyHashSet{List<List<Integer>> b=new ArrayList<>();MyHashSet(){for(int i=0;i<769;i++)b.add(new ArrayList<>());}int h(int k){return k%769;}void add(int k){var x=b.get(h(k));if(!x.contains(k))x.add(k);}void remove(int k){b.get(h(k)).remove(Integer.valueOf(k));}boolean contains(int k){return b.get(h(k)).contains(k);}}
  public static void main(String[]x){MyHashSet s=new MyHashSet();s.add(1);s.add(2);System.out.println(s.contains(1)+" "+s.contains(3));s.remove(2);System.out.println(s.contains(2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct MyHashSet{ vector<vector<int>> b=vector<vector<int>>(769); int h(int k){return k%769;} void add(int k){auto& x=b[h(k)];if(find(x.begin(),x.end(),k)==x.end())x.push_back(k);} void remove(int k){auto& x=b[h(k)];x.erase(std::remove(x.begin(),x.end(),k),x.end());} bool contains(int k){auto& x=b[h(k)];return find(x.begin(),x.end(),k)!=x.end();}};
int main(){MyHashSet s; s.add(1); s.add(2); cout<<boolalpha<<s.contains(1)<<" "<<s.contains(3)<<"\\n"; s.remove(2); cout<<s.contains(2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type MyHashSet struct{ b [769][]int }
func (s *MyHashSet) h(k int) int { return ((k%769)+769)%769 }
func (s *MyHashSet) Add(k int){ i:=s.h(k); for _,x:=range s.b[i]{ if x==k{ return } }; s.b[i]=append(s.b[i],k) }
func (s *MyHashSet) Remove(k int){ i:=s.h(k); for j,x:=range s.b[i]{ if x==k{ s.b[i]=append(s.b[i][:j],s.b[i][j+1:]...); return } } }
func (s *MyHashSet) Contains(k int) bool { i:=s.h(k); for _,x:=range s.b[i]{ if x==k{ return true } }; return false }
func main(){ s:=&MyHashSet{}; s.Add(1); s.Add(2); fmt.Println(s.Contains(1), s.Contains(3)); s.Remove(2); fmt.Println(s.Contains(2)) }
''',
"R": '''MyHashSet <- function(){ env <- new.env(hash=TRUE); list(add=function(k) assign(as.character(k),TRUE,envir=env), remove=function(k){ if(exists(as.character(k),envir=env)) rm(list=as.character(k),envir=env) }, contains=function(k) exists(as.character(k),envir=env)) }
s <- MyHashSet(); s$add(1); s$add(2); cat(s$contains(1), s$contains(3),"\\n"); s$remove(2); cat(s$contains(2),"\\n")
''',
}))

# 124 Top K Frequent Elements
L.append((124, "Top K Frequent Elements", "Arrays and Hashing", "Medium", 62,
"Given an integer array nums and integer k, return the k most frequent elements.",
{
"Python": '''from collections import Counter
def topK(a,k):
    return [x for x,_ in Counter(a).most_common(k)]

if __name__=="__main__":
    print(topK([1,1,1,2,2,3],2))
''',
"JavaScript": '''function topK(a,k){const m=new Map();for(const x of a)m.set(x,(m.get(x)||0)+1);return [...m.entries()].sort((p,q)=>q[1]-p[1]).slice(0,k).map(e=>e[0]);}
console.log(topK([1,1,1,2,2,3],2));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] topK(int[]a,int k){Map<Integer,Integer> m=new HashMap<>();for(int x:a)m.merge(x,1,Integer::sum);List<Map.Entry<Integer,Integer>> e=new ArrayList<>(m.entrySet());e.sort((p,q)->q.getValue()-p.getValue());int[] r=new int[k];for(int i=0;i<k;i++)r[i]=e.get(i).getKey();return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(topK(new int[]{1,1,1,2,2,3},2)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> topK(vector<int> a,int k){unordered_map<int,int> m;for(int x:a)m[x]++;vector<pair<int,int>> v(m.begin(),m.end());sort(v.begin(),v.end(),[](auto&p,auto&q){return p.second>q.second;});vector<int> r;for(int i=0;i<k;i++)r.push_back(v[i].first);return r;}
int main(){auto v=topK({1,1,1,2,2,3},2);for(int x:v)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import ("fmt";"sort")
func topK(a []int,k int) []int { m:=map[int]int{}; for _,x:=range a { m[x]++ }; type P struct{V,C int}; var v []P; for kk,c:=range m { v=append(v,P{kk,c}) }; sort.Slice(v,func(i,j int) bool{return v[i].C>v[j].C}); r:=make([]int,k); for i:=0;i<k;i++ { r[i]=v[i].V }; return r }
func main(){ fmt.Println(topK([]int{1,1,1,2,2,3},2)) }
''',
"R": '''topK <- function(a,k){ t <- sort(table(a),decreasing=TRUE); as.integer(names(t)[1:k]) }
print(topK(c(1,1,1,2,2,3),2))
''',
}))

# 125 Merge Sorted Array
L.append((125, "Merge Sorted Array", "Two Pointers", "Easy", 63,
"Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.",
{
"Python": '''def merge(a,m,b,n):
    i,j,k=m-1,n-1,m+n-1
    while j>=0:
        if i>=0 and a[i]>b[j]: a[k]=a[i]; i-=1
        else: a[k]=b[j]; j-=1
        k-=1
    return a

if __name__=="__main__":
    print(merge([1,2,3,0,0,0],3,[2,5,6],3))
''',
"JavaScript": '''function merge(a,m,b,n){let i=m-1,j=n-1,k=m+n-1;while(j>=0){if(i>=0&&a[i]>b[j]){a[k--]=a[i--];}else{a[k--]=b[j--];}}return a;}
console.log(merge([1,2,3,0,0,0],3,[2,5,6],3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] merge(int[]a,int m,int[]b,int n){int i=m-1,j=n-1,k=m+n-1;while(j>=0){if(i>=0&&a[i]>b[j])a[k--]=a[i--];else a[k--]=b[j--];}return a;}
  public static void main(String[]x){System.out.println(Arrays.toString(merge(new int[]{1,2,3,0,0,0},3,new int[]{2,5,6},3)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> merge(vector<int> a,int m,vector<int> b,int n){int i=m-1,j=n-1,k=m+n-1;while(j>=0){if(i>=0&&a[i]>b[j])a[k--]=a[i--];else a[k--]=b[j--];}return a;}
int main(){auto v=merge({1,2,3,0,0,0},3,{2,5,6},3);for(int x:v)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func merge(a []int,m int,b []int,n int) []int { i,j,k:=m-1,n-1,m+n-1; for j>=0 { if i>=0 && a[i]>b[j] { a[k]=a[i]; i-- } else { a[k]=b[j]; j-- }; k-- }; return a }
func main(){ fmt.Println(merge([]int{1,2,3,0,0,0},3,[]int{2,5,6},3)) }
''',
"R": '''merge2 <- function(a,m,b,n){ i<-m;j<-n;k<-m+n; while(j>=1){ if(i>=1 && a[i]>b[j]){ a[k]<-a[i]; i<-i-1 } else { a[k]<-b[j]; j<-j-1 }; k<-k-1 }; a }
print(merge2(c(1,2,3,0,0,0),3,c(2,5,6),3))
''',
}))

# 126 Container With Most Water
L.append((126, "Container With Most Water", "Two Pointers", "Medium", 63,
"Given heights, find two lines that form the container holding most water.",
{
"Python": '''def maxArea(h):
    l,r=0,len(h)-1; b=0
    while l<r:
        b=max(b,(r-l)*min(h[l],h[r]))
        if h[l]<h[r]: l+=1
        else: r-=1
    return b

if __name__=="__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
''',
"JavaScript": '''function maxArea(h){let l=0,r=h.length-1,b=0;while(l<r){b=Math.max(b,(r-l)*Math.min(h[l],h[r]));if(h[l]<h[r])l++;else r--;}return b;}
console.log(maxArea([1,8,6,2,5,4,8,3,7]));
''',
"Java": '''public class __CLASS__{
  static int maxArea(int[]h){int l=0,r=h.length-1,b=0;while(l<r){b=Math.max(b,(r-l)*Math.min(h[l],h[r]));if(h[l]<h[r])l++;else r--;}return b;}
  public static void main(String[]x){System.out.println(maxArea(new int[]{1,8,6,2,5,4,8,3,7}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxArea(vector<int>&h){int l=0,r=h.size()-1,b=0;while(l<r){b=max(b,(r-l)*min(h[l],h[r]));if(h[l]<h[r])l++;else r--;}return b;}
int main(){vector<int> v={1,8,6,2,5,4,8,3,7};cout<<maxArea(v)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxArea(h []int) int { l,r:=0,len(h)-1; b:=0; for l<r { x:=(r-l); m:=h[l]; if h[r]<m { m=h[r] }; if x*m>b { b=x*m }; if h[l]<h[r] { l++ } else { r-- } }; return b }
func main(){ fmt.Println(maxArea([]int{1,8,6,2,5,4,8,3,7})) }
''',
"R": '''maxArea <- function(h){ l<-1; r<-length(h); b<-0; while(l<r){ b<-max(b,(r-l)*min(h[l],h[r])); if(h[l]<h[r]) l<-l+1 else r<-r-1 }; b }
cat(maxArea(c(1,8,6,2,5,4,8,3,7)),"\\n")
''',
}))

# 127 Number of 1 Bits
L.append((127, "Number of 1 Bits", "Bit Manipulation", "Easy", 64,
"Return the number of 1 bits in unsigned int.",
{
"Python": '''def hw(n):
    c=0
    while n: n&=n-1; c+=1
    return c

if __name__=="__main__":
    print(hw(11)); print(hw(128))
''',
"JavaScript": '''function hw(n){let c=0;while(n){n&=n-1;c++;}return c;}
console.log(hw(11));console.log(hw(128));
''',
"Java": '''public class __CLASS__{
  static int hw(int n){int c=0;while(n!=0){n&=n-1;c++;}return c;}
  public static void main(String[]x){System.out.println(hw(11));System.out.println(hw(128));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int hw(unsigned n){int c=0;while(n){n&=n-1;c++;}return c;}
int main(){cout<<hw(11)<<"\\n"<<hw(128)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func hw(n uint) int { c:=0; for n!=0 { n &= n-1; c++ }; return c }
func main(){ fmt.Println(hw(11)); fmt.Println(hw(128)) }
''',
"R": '''hw <- function(n){ c<-0; while(n!=0){ if(bitwAnd(n,1)==1) c<-c+1; n<-bitwShiftR(n,1) }; c }
cat(hw(11),"\\n"); cat(hw(128),"\\n")
''',
}))

# 128 Reverse Integer
L.append((128, "Reverse Integer", "Bit Manipulation", "Medium", 64,
"Reverse digits of a signed 32-bit integer; return 0 on overflow.",
{
"Python": '''def rev(x):
    s=-1 if x<0 else 1; x*=s; r=0
    while x: r=r*10+x%10; x//=10
    r*=s
    if r<-2**31 or r>2**31-1: return 0
    return r

if __name__=="__main__":
    print(rev(123)); print(rev(-456)); print(rev(1534236469))
''',
"JavaScript": '''function rev(x){const s=x<0?-1:1;x=Math.abs(x);let r=0;while(x){r=r*10+x%10;x=Math.floor(x/10);}r*=s;if(r<-2**31||r>2**31-1)return 0;return r;}
console.log(rev(123));console.log(rev(-456));console.log(rev(1534236469));
''',
"Java": '''public class __CLASS__{
  static int rev(int x){long r=0;while(x!=0){r=r*10+x%10;x/=10;}if(r<Integer.MIN_VALUE||r>Integer.MAX_VALUE)return 0;return (int)r;}
  public static void main(String[]a){System.out.println(rev(123));System.out.println(rev(-456));System.out.println(rev(1534236469));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int rev(int x){long r=0;while(x){r=r*10+x%10;x/=10;}if(r<INT_MIN||r>INT_MAX)return 0;return (int)r;}
int main(){cout<<rev(123)<<"\\n"<<rev(-456)<<"\\n"<<rev(1534236469)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func rev(x int) int { r:=0; for x!=0 { r=r*10+x%10; x/=10 }; if r<-(1<<31) || r>(1<<31)-1 { return 0 }; return r }
func main(){ fmt.Println(rev(123)); fmt.Println(rev(-456)); fmt.Println(rev(1534236469)) }
''',
"R": '''rev <- function(x){ s<-sign(x); x<-abs(x); r<-0; while(x>0){ r<-r*10+x%%10; x<-x%/%10 }; r<-r*s; if(r < -2^31 || r > 2^31-1) 0 else r }
cat(rev(123),"\\n"); cat(rev(-456),"\\n"); cat(rev(1534236469),"\\n")
''',
}))

# 129 Maximum Sum Circular Subarray
L.append((129, "Maximum Sum Circular Subarray", "Greedy", "Medium", 65,
"Given a circular integer array, find the maximum subarray sum (subarray may wrap).",
{
"Python": '''def maxCirc(a):
    tot=0; mxc=cur=a[0]; mnc=cur2=a[0]
    for i,x in enumerate(a):
        if i: cur=max(x,cur+x); mxc=max(mxc,cur); cur2=min(x,cur2+x); mnc=min(mnc,cur2)
        tot+=x
    return mxc if mxc<0 else max(mxc,tot-mnc)

if __name__=="__main__":
    print(maxCirc([1,-2,3,-2]))
    print(maxCirc([5,-3,5]))
    print(maxCirc([-3,-2,-3]))
''',
"JavaScript": '''function maxCirc(a){let tot=0,mxc=a[0],cur=a[0],mnc=a[0],cur2=a[0];for(let i=0;i<a.length;i++){if(i){cur=Math.max(a[i],cur+a[i]);mxc=Math.max(mxc,cur);cur2=Math.min(a[i],cur2+a[i]);mnc=Math.min(mnc,cur2);}tot+=a[i];}return mxc<0?mxc:Math.max(mxc,tot-mnc);}
console.log(maxCirc([1,-2,3,-2]));console.log(maxCirc([5,-3,5]));console.log(maxCirc([-3,-2,-3]));
''',
"Java": '''public class __CLASS__{
  static int maxCirc(int[]a){int tot=0,mxc=a[0],cur=a[0],mnc=a[0],c2=a[0];for(int i=0;i<a.length;i++){if(i>0){cur=Math.max(a[i],cur+a[i]);mxc=Math.max(mxc,cur);c2=Math.min(a[i],c2+a[i]);mnc=Math.min(mnc,c2);}tot+=a[i];}return mxc<0?mxc:Math.max(mxc,tot-mnc);}
  public static void main(String[]x){System.out.println(maxCirc(new int[]{1,-2,3,-2}));System.out.println(maxCirc(new int[]{5,-3,5}));System.out.println(maxCirc(new int[]{-3,-2,-3}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxCirc(vector<int>&a){int tot=0,mxc=a[0],cur=a[0],mnc=a[0],c2=a[0];for(int i=0;i<(int)a.size();i++){if(i>0){cur=max(a[i],cur+a[i]);mxc=max(mxc,cur);c2=min(a[i],c2+a[i]);mnc=min(mnc,c2);}tot+=a[i];}return mxc<0?mxc:max(mxc,tot-mnc);}
int main(){vector<int> a={1,-2,3,-2}, b={5,-3,5}, c={-3,-2,-3};cout<<maxCirc(a)<<"\\n"<<maxCirc(b)<<"\\n"<<maxCirc(c)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxCirc(a []int) int { tot,mxc,cur,mnc,c2:=0,a[0],a[0],a[0],a[0]; for i,x:=range a { if i>0 { if x>cur+x { cur=x } else { cur+=x }; if cur>mxc { mxc=cur }; if x<c2+x { c2=x } else { c2+=x }; if c2<mnc { mnc=c2 } }; tot+=x }; if mxc<0 { return mxc }; if mxc>tot-mnc { return mxc }; return tot-mnc }
func main(){ fmt.Println(maxCirc([]int{1,-2,3,-2})); fmt.Println(maxCirc([]int{5,-3,5})); fmt.Println(maxCirc([]int{-3,-2,-3})) }
''',
"R": '''maxCirc <- function(a){ tot<-0; mxc<-a[1]; cur<-a[1]; mnc<-a[1]; c2<-a[1]; for(i in seq_along(a)){ if(i>1){ cur<-max(a[i],cur+a[i]); mxc<-max(mxc,cur); c2<-min(a[i],c2+a[i]); mnc<-min(mnc,c2) }; tot<-tot+a[i] }; if(mxc<0) mxc else max(mxc,tot-mnc) }
cat(maxCirc(c(1,-2,3,-2)),"\\n"); cat(maxCirc(c(5,-3,5)),"\\n"); cat(maxCirc(c(-3,-2,-3)),"\\n")
''',
}))

# 130 Longest Turbulent Subarray
L.append((130, "Longest Turbulent Subarray", "Greedy", "Medium", 65,
"Given an array, return length of longest turbulent subarray (alternating > <).",
{
"Python": '''def turb(a):
    n=len(a); inc=dec=1; b=1
    for i in range(1,n):
        if a[i]>a[i-1]: inc=dec+1; dec=1
        elif a[i]<a[i-1]: dec=inc+1; inc=1
        else: inc=dec=1
        b=max(b,inc,dec)
    return b

if __name__=="__main__":
    print(turb([9,4,2,10,7,8,8,1,9]))
''',
"JavaScript": '''function turb(a){let inc=1,dec=1,b=1;for(let i=1;i<a.length;i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else{inc=dec=1;}b=Math.max(b,inc,dec);}return b;}
console.log(turb([9,4,2,10,7,8,8,1,9]));
''',
"Java": '''public class __CLASS__{
  static int turb(int[]a){int inc=1,dec=1,b=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else inc=dec=1;b=Math.max(b,Math.max(inc,dec));}return b;}
  public static void main(String[]x){System.out.println(turb(new int[]{9,4,2,10,7,8,8,1,9}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int turb(vector<int>&a){int inc=1,dec=1,b=1;for(int i=1;i<(int)a.size();i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else inc=dec=1;b=max({b,inc,dec});}return b;}
int main(){vector<int> v={9,4,2,10,7,8,8,1,9};cout<<turb(v)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func turb(a []int) int { inc,dec,b:=1,1,1; for i:=1;i<len(a);i++ { if a[i]>a[i-1] { inc=dec+1; dec=1 } else if a[i]<a[i-1] { dec=inc+1; inc=1 } else { inc=1; dec=1 }; m:=inc; if dec>m { m=dec }; if m>b { b=m } }; return b }
func main(){ fmt.Println(turb([]int{9,4,2,10,7,8,8,1,9})) }
''',
"R": '''turb <- function(a){ inc<-1; dec<-1; b<-1; for(i in 2:length(a)){ if(a[i]>a[i-1]){ inc<-dec+1; dec<-1 } else if(a[i]<a[i-1]){ dec<-inc+1; inc<-1 } else { inc<-1; dec<-1 }; b<-max(b,inc,dec) }; b }
cat(turb(c(9,4,2,10,7,8,8,1,9)),"\\n")
''',
}))

# 131 Time Based Key Value Store
L.append((131, "Time Based Key Value Store", "Binary Search", "Medium", 66,
"Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.",
{
"Python": '''import bisect
class TimeMap:
    def __init__(self): self.m={}
    def set(self,k,v,t): self.m.setdefault(k,([],[]))[0].append(t); self.m[k][1].append(v)
    def get(self,k,t):
        if k not in self.m: return ""
        ts,vs=self.m[k]
        i=bisect.bisect_right(ts,t)-1
        return vs[i] if i>=0 else ""

if __name__=="__main__":
    tm=TimeMap(); tm.set("foo","bar",1); print(tm.get("foo",1)); print(tm.get("foo",3)); tm.set("foo","bar2",4); print(tm.get("foo",4)); print(tm.get("foo",5))
''',
"JavaScript": '''class TimeMap{constructor(){this.m=new Map();}set(k,v,t){if(!this.m.has(k))this.m.set(k,[[],[]]);const [ts,vs]=this.m.get(k);ts.push(t);vs.push(v);}get(k,t){if(!this.m.has(k))return "";const [ts,vs]=this.m.get(k);let lo=0,hi=ts.length-1,r=-1;while(lo<=hi){const m=(lo+hi)>>1;if(ts[m]<=t){r=m;lo=m+1;}else hi=m-1;}return r<0?"":vs[r];}}
const tm=new TimeMap();tm.set("foo","bar",1);console.log(tm.get("foo",1));console.log(tm.get("foo",3));tm.set("foo","bar2",4);console.log(tm.get("foo",4));console.log(tm.get("foo",5));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class TimeMap{Map<String,List<int[]>> mt=new HashMap<>();Map<String,List<String>> mv=new HashMap<>();void set(String k,String v,int t){mt.computeIfAbsent(k,x->new ArrayList<>()).add(new int[]{t});mv.computeIfAbsent(k,x->new ArrayList<>()).add(v);}String get(String k,int t){if(!mt.containsKey(k))return "";var ts=mt.get(k);var vs=mv.get(k);int lo=0,hi=ts.size()-1,r=-1;while(lo<=hi){int m=(lo+hi)>>>1;if(ts.get(m)[0]<=t){r=m;lo=m+1;}else hi=m-1;}return r<0?"":vs.get(r);}}
  public static void main(String[]x){TimeMap tm=new TimeMap();tm.set("foo","bar",1);System.out.println(tm.get("foo",1));System.out.println(tm.get("foo",3));tm.set("foo","bar2",4);System.out.println(tm.get("foo",4));System.out.println(tm.get("foo",5));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct TimeMap{ unordered_map<string,vector<pair<int,string>>> m; void set(string k,string v,int t){m[k].push_back({t,v});} string get(string k,int t){auto it=m.find(k);if(it==m.end())return ""; auto& v=it->second; int lo=0,hi=v.size()-1,r=-1; while(lo<=hi){int mid=(lo+hi)/2; if(v[mid].first<=t){r=mid;lo=mid+1;} else hi=mid-1;} return r<0?"":v[r].second;}};
int main(){TimeMap tm; tm.set("foo","bar",1); cout<<tm.get("foo",1)<<"\\n"<<tm.get("foo",3)<<"\\n"; tm.set("foo","bar2",4); cout<<tm.get("foo",4)<<"\\n"<<tm.get("foo",5)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type TimeMap struct{ ts map[string][]int; vs map[string][]string }
func New() *TimeMap { return &TimeMap{map[string][]int{},map[string][]string{}} }
func (m *TimeMap) Set(k,v string,t int){ m.ts[k]=append(m.ts[k],t); m.vs[k]=append(m.vs[k],v) }
func (m *TimeMap) Get(k string,t int) string { ts,ok:=m.ts[k]; if !ok { return "" }; lo,hi,r:=0,len(ts)-1,-1; for lo<=hi { mid:=(lo+hi)/2; if ts[mid]<=t { r=mid; lo=mid+1 } else { hi=mid-1 } }; if r<0 { return "" }; return m.vs[k][r] }
func main(){ tm:=New(); tm.Set("foo","bar",1); fmt.Println(tm.Get("foo",1)); fmt.Println(tm.Get("foo",3)); tm.Set("foo","bar2",4); fmt.Println(tm.Get("foo",4)); fmt.Println(tm.Get("foo",5)) }
''',
"R": '''TimeMap <- function(){ env<-new.env(hash=TRUE); list(set=function(k,v,t){ x<-if(exists(k,envir=env)) get(k,envir=env) else list(t=c(),v=c()); x$t<-c(x$t,t); x$v<-c(x$v,v); assign(k,x,envir=env) }, get=function(k,t){ if(!exists(k,envir=env)) return(""); x<-get(k,envir=env); idx<-max(c(0,which(x$t<=t))); if(idx==0) "" else x$v[idx] }) }
tm<-TimeMap(); tm$set("foo","bar",1); cat(tm$get("foo",1),"\\n"); cat(tm$get("foo",3),"\\n"); tm$set("foo","bar2",4); cat(tm$get("foo",4),"\\n"); cat(tm$get("foo",5),"\\n")
''',
}))

# 132 Split Array Largest Sum
L.append((132, "Split Array Largest Sum", "Binary Search", "Hard", 66,
"Split nums into k non-empty contiguous parts to minimize the largest sum among parts.",
{
"Python": '''def split(a,k):
    def can(mx):
        c,s=1,0
        for x in a:
            if s+x>mx: c+=1; s=x
            else: s+=x
        return c<=k
    lo,hi=max(a),sum(a)
    while lo<hi:
        m=(lo+hi)//2
        if can(m): hi=m
        else: lo=m+1
    return lo

if __name__=="__main__":
    print(split([7,2,5,10,8],2))
''',
"JavaScript": '''function split(a,k){const can=mx=>{let c=1,s=0;for(const x of a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;};let lo=Math.max(...a),hi=a.reduce((p,q)=>p+q,0);while(lo<hi){const m=(lo+hi)>>1;if(can(m))hi=m;else lo=m+1;}return lo;}
console.log(split([7,2,5,10,8],2));
''',
"Java": '''public class __CLASS__{
  static boolean can(int[]a,int k,int mx){int c=1,s=0;for(int x:a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;}
  static int split(int[]a,int k){int lo=0,hi=0;for(int x:a){lo=Math.max(lo,x);hi+=x;}while(lo<hi){int m=(lo+hi)>>>1;if(can(a,k,m))hi=m;else lo=m+1;}return lo;}
  public static void main(String[]x){System.out.println(split(new int[]{7,2,5,10,8},2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool can(vector<int>&a,int k,int mx){int c=1,s=0;for(int x:a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;}
int split(vector<int>&a,int k){int lo=*max_element(a.begin(),a.end()),hi=accumulate(a.begin(),a.end(),0);while(lo<hi){int m=(lo+hi)/2;if(can(a,k,m))hi=m;else lo=m+1;}return lo;}
int main(){vector<int> v={7,2,5,10,8};cout<<split(v,2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func split(a []int,k int) int { can:=func(mx int) bool { c,s:=1,0; for _,x:=range a { if s+x>mx { c++; s=x } else { s+=x } }; return c<=k }; lo,hi:=a[0],0; for _,x:=range a { if x>lo { lo=x }; hi+=x }; for lo<hi { m:=(lo+hi)/2; if can(m) { hi=m } else { lo=m+1 } }; return lo }
func main(){ fmt.Println(split([]int{7,2,5,10,8},2)) }
''',
"R": '''split2 <- function(a,k){ can<-function(mx){ c<-1; s<-0; for(x in a){ if(s+x>mx){ c<-c+1; s<-x } else s<-s+x }; c<=k }; lo<-max(a); hi<-sum(a); while(lo<hi){ m<-(lo+hi)%/%2; if(can(m)) hi<-m else lo<-m+1 }; lo }
cat(split2(c(7,2,5,10,8),2),"\\n")
''',
}))

# 133 Counting Bits
L.append((133, "Counting Bits", "Bit Manipulation", "Easy", 67,
"For 0..n return array where ans[i] = number of 1-bits in i.",
{
"Python": '''def cb(n):
    a=[0]*(n+1)
    for i in range(1,n+1): a[i]=a[i>>1]+(i&1)
    return a

if __name__=="__main__":
    print(cb(5))
''',
"JavaScript": '''function cb(n){const a=new Array(n+1).fill(0);for(let i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
console.log(cb(5));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] cb(int n){int[] a=new int[n+1];for(int i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
  public static void main(String[]x){System.out.println(Arrays.toString(cb(5)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> cb(int n){vector<int> a(n+1);for(int i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
int main(){auto v=cb(5);for(int x:v)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func cb(n int) []int { a:=make([]int,n+1); for i:=1;i<=n;i++ { a[i]=a[i>>1]+(i&1) }; return a }
func main(){ fmt.Println(cb(5)) }
''',
"R": '''cb <- function(n){ a<-rep(0,n+1); for(i in 1:n) a[i+1]<-a[(i %/% 2)+1] + (i %% 2); a }
print(cb(5))
''',
}))

# 134 Bitwise AND of Numbers Range
L.append((134, "Bitwise AND of Numbers Range", "Bit Manipulation", "Medium", 67,
"Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.",
{
"Python": '''def rangeAnd(m,n):
    s=0
    while m!=n: m>>=1; n>>=1; s+=1
    return m<<s

if __name__=="__main__":
    print(rangeAnd(5,7)); print(rangeAnd(0,0))
''',
"JavaScript": '''function rangeAnd(m,n){let s=0;while(m!==n){m>>=1;n>>=1;s++;}return m<<s;}
console.log(rangeAnd(5,7));console.log(rangeAnd(0,0));
''',
"Java": '''public class __CLASS__{
  static int rangeAnd(int m,int n){int s=0;while(m!=n){m>>=1;n>>=1;s++;}return m<<s;}
  public static void main(String[]x){System.out.println(rangeAnd(5,7));System.out.println(rangeAnd(0,0));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int rangeAnd(int m,int n){int s=0;while(m!=n){m>>=1;n>>=1;s++;}return m<<s;}
int main(){cout<<rangeAnd(5,7)<<"\\n"<<rangeAnd(0,0)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func rangeAnd(m,n int) int { s:=0; for m!=n { m>>=1; n>>=1; s++ }; return m<<s }
func main(){ fmt.Println(rangeAnd(5,7)); fmt.Println(rangeAnd(0,0)) }
''',
"R": '''rangeAnd <- function(m,n){ s<-0; while(m!=n){ m<-bitwShiftR(m,1); n<-bitwShiftR(n,1); s<-s+1 }; bitwShiftL(m,s) }
cat(rangeAnd(5,7),"\\n"); cat(rangeAnd(0,0),"\\n")
''',
}))

# 135 Longest Happy String
L.append((135, "Longest Happy String", "Heap Priority Queue", "Medium", 68,
"Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.",
{
"Python": '''import heapq
def longest(a,b,c):
    h=[]
    for cnt,ch in [(-a,'a'),(-b,'b'),(-c,'c')]:
        if cnt: heapq.heappush(h,(cnt,ch))
    out=[]
    while h:
        c1,ch1=heapq.heappop(h)
        if len(out)>=2 and out[-1]==out[-2]==ch1:
            if not h: break
            c2,ch2=heapq.heappop(h)
            out.append(ch2); c2+=1
            if c2: heapq.heappush(h,(c2,ch2))
            heapq.heappush(h,(c1,ch1))
        else:
            out.append(ch1); c1+=1
            if c1: heapq.heappush(h,(c1,ch1))
    return "".join(out)

if __name__=="__main__":
    print(longest(1,1,7))
    print(longest(7,1,0))
''',
"JavaScript": '''function longest(a,b,c){const h=[];if(a)h.push([a,'a']);if(b)h.push([b,'b']);if(c)h.push([c,'c']);const out=[];const popMax=()=>{let mi=0;for(let i=1;i<h.length;i++)if(h[i][0]>h[mi][0])mi=i;return h.splice(mi,1)[0];};while(h.length){const [c1,ch1]=popMax();if(out.length>=2&&out[out.length-1]===ch1&&out[out.length-2]===ch1){if(!h.length)break;const [c2,ch2]=popMax();out.push(ch2);if(c2-1)h.push([c2-1,ch2]);h.push([c1,ch1]);}else{out.push(ch1);if(c1-1)h.push([c1-1,ch1]);}}return out.join("");}
console.log(longest(1,1,7));console.log(longest(7,1,0));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String longest(int a,int b,int c){PriorityQueue<int[]> h=new PriorityQueue<>((p,q)->q[0]-p[0]);if(a>0)h.add(new int[]{a,'a'});if(b>0)h.add(new int[]{b,'b'});if(c>0)h.add(new int[]{c,'c'});StringBuilder sb=new StringBuilder();while(!h.isEmpty()){int[] x=h.poll();int n=sb.length();if(n>=2&&sb.charAt(n-1)==(char)x[1]&&sb.charAt(n-2)==(char)x[1]){if(h.isEmpty())break;int[] y=h.poll();sb.append((char)y[1]);if(y[0]-1>0)h.add(new int[]{y[0]-1,y[1]});h.add(x);}else{sb.append((char)x[1]);if(x[0]-1>0)h.add(new int[]{x[0]-1,x[1]});}}return sb.toString();}
  public static void main(String[]x){System.out.println(longest(1,1,7));System.out.println(longest(7,1,0));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string longest(int a,int b,int c){priority_queue<pair<int,char>> h;if(a)h.push({a,'a'});if(b)h.push({b,'b'});if(c)h.push({c,'c'});string s;while(!h.empty()){auto [c1,ch1]=h.top();h.pop();int n=s.size();if(n>=2&&s[n-1]==ch1&&s[n-2]==ch1){if(h.empty())break;auto [c2,ch2]=h.top();h.pop();s+=ch2;if(c2-1)h.push({c2-1,ch2});h.push({c1,ch1});}else{s+=ch1;if(c1-1)h.push({c1-1,ch1});}}return s;}
int main(){cout<<longest(1,1,7)<<"\\n"<<longest(7,1,0)<<"\\n";}
''',
"Go": '''package main
import ("fmt";"container/heap")
type Item struct{ Cnt int; Ch byte }
type PQ []Item
func (p PQ) Len() int{return len(p)}; func (p PQ) Less(i,j int) bool{return p[i].Cnt>p[j].Cnt}; func (p PQ) Swap(i,j int){p[i],p[j]=p[j],p[i]}
func (p *PQ) Push(x any){*p=append(*p,x.(Item))}; func (p *PQ) Pop() any{o:=*p; n:=len(o); x:=o[n-1]; *p=o[:n-1]; return x}
func longest(a,b,c int) string { h:=&PQ{}; if a>0 { *h=append(*h,Item{a,'a'}) }; if b>0 { *h=append(*h,Item{b,'b'}) }; if c>0 { *h=append(*h,Item{c,'c'}) }; heap.Init(h); var s []byte; for h.Len()>0 { x:=heap.Pop(h).(Item); n:=len(s); if n>=2 && s[n-1]==x.Ch && s[n-2]==x.Ch { if h.Len()==0 { break }; y:=heap.Pop(h).(Item); s=append(s,y.Ch); if y.Cnt-1>0 { heap.Push(h,Item{y.Cnt-1,y.Ch}) }; heap.Push(h,x) } else { s=append(s,x.Ch); if x.Cnt-1>0 { heap.Push(h,Item{x.Cnt-1,x.Ch}) } } }; return string(s) }
func main(){ fmt.Println(longest(1,1,7)); fmt.Println(longest(7,1,0)) }
''',
"R": '''longest <- function(a,b,c){ h<-list(); if(a>0) h[[length(h)+1]]<-c(a,utf8ToInt('a')); if(b>0) h[[length(h)+1]]<-c(b,utf8ToInt('b')); if(c>0) h[[length(h)+1]]<-c(c,utf8ToInt('c')); s<-c(); popMax<-function(){ idx<-which.max(sapply(h,`[`,1)); x<-h[[idx]]; h[[idx]]<<-NULL; x }; while(length(h)>0){ x<-popMax(); n<-length(s); if(n>=2 && s[n]==x[2] && s[n-1]==x[2]){ if(length(h)==0) break; y<-popMax(); s<-c(s,y[2]); if(y[1]-1>0) h[[length(h)+1]]<-c(y[1]-1,y[2]); h[[length(h)+1]]<-x } else { s<-c(s,x[2]); if(x[1]-1>0) h[[length(h)+1]]<-c(x[1]-1,x[2]) } }; intToUtf8(s) }
cat(longest(1,1,7),"\\n"); cat(longest(7,1,0),"\\n")
''',
}))

write_lessons(L)
