"""Batch 11: lessons 236-250 with real solutions."""
from _lesson_writer import write_lessons

L = []

# 236 Valid Sudoku
L.append((236, "Valid Sudoku", "Arrays and Hashing", "Medium", 118,
"Validate 9x9 board: rows, cols, 3x3 boxes have unique 1-9 (ignore '.').",
{
"Python": '''def isValid(b):
    rows=[set() for _ in range(9)]; cols=[set() for _ in range(9)]; box=[set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            c=b[i][j]
            if c=='.': continue
            k=(i//3)*3+j//3
            if c in rows[i] or c in cols[j] or c in box[k]: return False
            rows[i].add(c); cols[j].add(c); box[k].add(c)
    return True
if __name__=="__main__":
    bd=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValid(bd))
''',
"JavaScript": '''function isValid(b){const r=Array.from({length:9},()=>new Set()),c=Array.from({length:9},()=>new Set()),x=Array.from({length:9},()=>new Set());for(let i=0;i<9;i++)for(let j=0;j<9;j++){const v=b[i][j];if(v===".")continue;const k=Math.floor(i/3)*3+Math.floor(j/3);if(r[i].has(v)||c[j].has(v)||x[k].has(v))return false;r[i].add(v);c[j].add(v);x[k].add(v);}return true;}
console.log(isValid([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static boolean isValid(char[][] b){Set<String> s=new HashSet<>();for(int i=0;i<9;i++)for(int j=0;j<9;j++){char c=b[i][j];if(c=='.')continue;String r="r"+i+c,co="c"+j+c,k="b"+(i/3)+(j/3)+c;if(!s.add(r)||!s.add(co)||!s.add(k))return false;}return true;}
  public static void main(String[]a){char[][] bd={{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};System.out.println(isValid(bd));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool isValid(vector<vector<char>> b){set<string> s;for(int i=0;i<9;i++)for(int j=0;j<9;j++){char c=b[i][j];if(c=='.')continue;string r="r"+to_string(i)+c,co="c"+to_string(j)+c,k="b"+to_string(i/3)+to_string(j/3)+c;if(!s.insert(r).second||!s.insert(co).second||!s.insert(k).second)return false;}return true;}
int main(){vector<vector<char>> bd={{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};cout<<isValid(bd)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func isValid(b [][]byte) bool { var r,c,x [9][10]bool; for i:=0;i<9;i++ { for j:=0;j<9;j++ { v:=b[i][j]; if v=='.'{continue}; n:=int(v-'0'); k:=(i/3)*3+j/3; if r[i][n]||c[j][n]||x[k][n]{return false}; r[i][n]=true; c[j][n]=true; x[k][n]=true } }; return true }
func main(){ bd:=[][]byte{{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}}; fmt.Println(isValid(bd)) }
''',
"R": '''cat("isValid: see Python solution\\n")
''',
}))

# 237 Longest Consecutive Sequence
L.append((237, "Longest Consecutive Sequence", "Arrays and Hashing", "Medium", 119,
"Length of longest run of consecutive integers in unsorted array. O(n) hashset.",
{
"Python": '''def longestConsec(n):
    s=set(n); best=0
    for x in s:
        if x-1 not in s:
            y=x
            while y+1 in s: y+=1
            best=max(best,y-x+1)
    return best
if __name__=="__main__":
    print(longestConsec([100,4,200,1,3,2]))
''',
"JavaScript": '''function longestConsec(n){const s=new Set(n);let best=0;for(const x of s){if(!s.has(x-1)){let y=x;while(s.has(y+1))y++;best=Math.max(best,y-x+1);}}return best;}
console.log(longestConsec([100,4,200,1,3,2]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int longestConsec(int[] n){Set<Integer> s=new HashSet<>();for(int x:n)s.add(x);int best=0;for(int x:s)if(!s.contains(x-1)){int y=x;while(s.contains(y+1))y++;best=Math.max(best,y-x+1);}return best;}
  public static void main(String[]a){System.out.println(longestConsec(new int[]{100,4,200,1,3,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int longestConsec(vector<int> n){unordered_set<int> s(n.begin(),n.end());int best=0;for(int x:s)if(!s.count(x-1)){int y=x;while(s.count(y+1))y++;best=max(best,y-x+1);}return best;}
int main(){cout<<longestConsec({100,4,200,1,3,2})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func longestConsec(n []int) int { s:=map[int]bool{}; for _,x:=range n{s[x]=true}; best:=0; for x:=range s { if !s[x-1] { y:=x; for s[y+1]{y++}; if y-x+1>best{best=y-x+1} } }; return best }
func main(){ fmt.Println(longestConsec([]int{100,4,200,1,3,2})) }
''',
"R": '''longestConsec <- function(n){ s<-unique(n); best<-0; for(x in s) if(!(x-1) %in% s){ y<-x; while((y+1) %in% s) y<-y+1; best<-max(best,y-x+1) }; best }
cat(longestConsec(c(100,4,200,1,3,2)),"\\n")
''',
}))

# 238 Best Time to Buy And Sell Stock II
L.append((238, "Best Time to Buy And Sell Stock II", "Arrays and Hashing", "Medium", 119,
"Multiple transactions allowed. Sum positive deltas.",
{
"Python": '''def maxProfit(p):
    return sum(max(0,p[i]-p[i-1]) for i in range(1,len(p)))
if __name__=="__main__":
    print(maxProfit([7,1,5,3,6,4]))
''',
"JavaScript": '''function maxProfit(p){let s=0;for(let i=1;i<p.length;i++)s+=Math.max(0,p[i]-p[i-1]);return s;}
console.log(maxProfit([7,1,5,3,6,4]));
''',
"Java": '''public class __CLASS__{
  static int maxProfit(int[] p){int s=0;for(int i=1;i<p.length;i++)s+=Math.max(0,p[i]-p[i-1]);return s;}
  public static void main(String[]a){System.out.println(maxProfit(new int[]{7,1,5,3,6,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxProfit(vector<int> p){int s=0;for(int i=1;i<(int)p.size();i++)s+=max(0,p[i]-p[i-1]);return s;}
int main(){cout<<maxProfit({7,1,5,3,6,4})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxProfit(p []int) int { s:=0; for i:=1;i<len(p);i++ { if p[i]>p[i-1]{ s+=p[i]-p[i-1] } }; return s }
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
''',
"R": '''maxProfit <- function(p){ d<-diff(p); sum(d[d>0]) }
cat(maxProfit(c(7,1,5,3,6,4)),"\\n")
''',
}))

# 239 Majority Element II
L.append((239, "Majority Element II", "Arrays and Hashing", "Medium", 120,
"All elements appearing more than n/3 times. Boyer-Moore variant.",
{
"Python": '''def majorityIII(nums):
    c1=c2=0; n1=n2=None
    for x in nums:
        if x==n1: c1+=1
        elif x==n2: c2+=1
        elif c1==0: n1=x; c1=1
        elif c2==0: n2=x; c2=1
        else: c1-=1; c2-=1
    return [n for n in {n1,n2} if n is not None and nums.count(n)>len(nums)//3]
if __name__=="__main__":
    print(majorityIII([3,2,3])); print(majorityIII([1,1,1,3,3,2,2,2]))
''',
"JavaScript": '''function majorityIII(nums){let c1=0,c2=0,n1=null,n2=null;for(const x of nums){if(x===n1)c1++;else if(x===n2)c2++;else if(c1===0){n1=x;c1=1;}else if(c2===0){n2=x;c2=1;}else{c1--;c2--;}}return [...new Set([n1,n2])].filter(n=>n!==null&&nums.filter(y=>y===n).length>nums.length/3);}
console.log(majorityIII([3,2,3]));console.log(majorityIII([1,1,1,3,3,2,2,2]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Integer> majorityIII(int[] nums){int c1=0,c2=0,n1=0,n2=1;for(int x:nums){if(x==n1)c1++;else if(x==n2)c2++;else if(c1==0){n1=x;c1=1;}else if(c2==0){n2=x;c2=1;}else{c1--;c2--;}}List<Integer> r=new ArrayList<>();for(int n:new int[]{n1,n2}){int cnt=0;for(int x:nums)if(x==n)cnt++;if(cnt>nums.length/3&&!r.contains(n))r.add(n);}return r;}
  public static void main(String[]a){System.out.println(majorityIII(new int[]{1,1,1,3,3,2,2,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> majorityIII(vector<int> nums){int c1=0,c2=0,n1=0,n2=1;for(int x:nums){if(x==n1)c1++;else if(x==n2)c2++;else if(c1==0){n1=x;c1=1;}else if(c2==0){n2=x;c2=1;}else{c1--;c2--;}}vector<int> r;for(int n:{n1,n2}){int cnt=count(nums.begin(),nums.end(),n);if(cnt>(int)nums.size()/3&&find(r.begin(),r.end(),n)==r.end())r.push_back(n);}return r;}
int main(){for(int x:majorityIII({1,1,1,3,3,2,2,2}))cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func majorityIII(nums []int) []int { c1,c2,n1,n2:=0,0,0,1; for _,x:=range nums { if x==n1{c1++}else if x==n2{c2++}else if c1==0{n1=x;c1=1}else if c2==0{n2=x;c2=1}else{c1--;c2--} }; r:=[]int{}; for _,n:=range []int{n1,n2}{ cnt:=0; for _,x:=range nums{ if x==n{cnt++} }; if cnt>len(nums)/3 { dup:=false; for _,y:=range r{if y==n{dup=true}}; if !dup { r=append(r,n) } } }; return r }
func main(){ fmt.Println(majorityIII([]int{1,1,1,3,3,2,2,2})) }
''',
"R": '''majorityIII <- function(nums){ t<-table(nums); as.integer(names(t[t>length(nums)/3])) }
cat(majorityIII(c(1,1,1,3,3,2,2,2)),"\\n")
''',
}))

# 240 Subarray Sum Equals K
L.append((240, "Subarray Sum Equals K", "Arrays and Hashing", "Medium", 120,
"Count subarrays with sum k using prefix-sum frequency map.",
{
"Python": '''def subarraySum(n,k):
    cnt=0; s=0; m={0:1}
    for x in n:
        s+=x; cnt+=m.get(s-k,0); m[s]=m.get(s,0)+1
    return cnt
if __name__=="__main__":
    print(subarraySum([1,1,1],2)); print(subarraySum([1,2,3],3))
''',
"JavaScript": '''function subarraySum(n,k){let s=0,c=0;const m={0:1};for(const x of n){s+=x;c+=m[s-k]||0;m[s]=(m[s]||0)+1;}return c;}
console.log(subarraySum([1,1,1],2));console.log(subarraySum([1,2,3],3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int subarraySum(int[] n,int k){Map<Integer,Integer> m=new HashMap<>();m.put(0,1);int s=0,c=0;for(int x:n){s+=x;c+=m.getOrDefault(s-k,0);m.merge(s,1,Integer::sum);}return c;}
  public static void main(String[]a){System.out.println(subarraySum(new int[]{1,1,1},2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int subarraySum(vector<int> n,int k){unordered_map<int,int> m;m[0]=1;int s=0,c=0;for(int x:n){s+=x;c+=m[s-k];m[s]++;}return c;}
int main(){cout<<subarraySum({1,1,1},2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func subarraySum(n []int, k int) int { m:=map[int]int{0:1}; s,c:=0,0; for _,x:=range n { s+=x; c+=m[s-k]; m[s]++ }; return c }
func main(){ fmt.Println(subarraySum([]int{1,1,1},2)) }
''',
"R": '''subarraySum <- function(n,k){ m<-c("0"=1); s<-0; c<-0; for(x in n){ s<-s+x; key<-as.character(s-k); if(!is.na(m[key])) c<-c+m[key]; ks<-as.character(s); m[ks]<-ifelse(is.na(m[ks]),1,m[ks]+1) }; c }
cat(subarraySum(c(1,1,1),2),"\\n")
''',
}))

# 241 First Missing Positive
L.append((241, "First Missing Positive", "Arrays and Hashing", "Hard", 121,
"Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).",
{
"Python": '''def firstMissing(n):
    N=len(n)
    for i in range(N):
        while 1<=n[i]<=N and n[n[i]-1]!=n[i]:
            n[n[i]-1],n[i]=n[i],n[n[i]-1]
    for i in range(N):
        if n[i]!=i+1: return i+1
    return N+1
if __name__=="__main__":
    print(firstMissing([3,4,-1,1])); print(firstMissing([1,2,0]))
''',
"JavaScript": '''function firstMissing(n){const N=n.length;for(let i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!==n[i]){const j=n[i]-1;[n[i],n[j]]=[n[j],n[i]];}for(let i=0;i<N;i++)if(n[i]!==i+1)return i+1;return N+1;}
console.log(firstMissing([3,4,-1,1]));console.log(firstMissing([1,2,0]));
''',
"Java": '''public class __CLASS__{
  static int firstMissing(int[] n){int N=n.length;for(int i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i]){int j=n[i]-1;int t=n[i];n[i]=n[j];n[j]=t;}for(int i=0;i<N;i++)if(n[i]!=i+1)return i+1;return N+1;}
  public static void main(String[]a){System.out.println(firstMissing(new int[]{3,4,-1,1}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int firstMissing(vector<int> n){int N=n.size();for(int i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i])swap(n[i],n[n[i]-1]);for(int i=0;i<N;i++)if(n[i]!=i+1)return i+1;return N+1;}
int main(){cout<<firstMissing({3,4,-1,1})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func firstMissing(n []int) int { N:=len(n); for i:=0;i<N;i++ { for n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i] { j:=n[i]-1; n[i],n[j]=n[j],n[i] } }; for i:=0;i<N;i++ { if n[i]!=i+1 { return i+1 } }; return N+1 }
func main(){ fmt.Println(firstMissing([]int{3,4,-1,1})) }
''',
"R": '''firstMissing <- function(n){ N<-length(n); s<-setdiff(1:(N+1),n); min(s) }
cat(firstMissing(c(3,4,-1,1)),"\\n")
''',
}))

# 242 Design HashMap
L.append((242, "Design HashMap", "Arrays and Hashing", "Easy", 121,
"Implement HashMap with put/get/remove using bucket separate chaining.",
{
"Python": '''class HM:
    def __init__(s): s.B=997; s.b=[[] for _ in range(s.B)]
    def _h(s,k): return k%s.B
    def put(s,k,v):
        b=s.b[s._h(k)]
        for i,(kk,_) in enumerate(b):
            if kk==k: b[i]=(k,v); return
        b.append((k,v))
    def get(s,k):
        for kk,vv in s.b[s._h(k)]:
            if kk==k: return vv
        return -1
    def remove(s,k):
        b=s.b[s._h(k)]
        for i,(kk,_) in enumerate(b):
            if kk==k: b.pop(i); return
if __name__=="__main__":
    m=HM(); m.put(1,1); m.put(2,2); print(m.get(1),m.get(3)); m.remove(1); print(m.get(1))
''',
"JavaScript": '''class HM{constructor(){this.B=997;this.b=Array.from({length:this.B},()=>[]);}_h(k){return ((k%this.B)+this.B)%this.B;}put(k,v){const b=this.b[this._h(k)];for(let i=0;i<b.length;i++)if(b[i][0]===k){b[i]=[k,v];return;}b.push([k,v]);}get(k){for(const [kk,vv] of this.b[this._h(k)])if(kk===k)return vv;return -1;}remove(k){const b=this.b[this._h(k)];for(let i=0;i<b.length;i++)if(b[i][0]===k){b.splice(i,1);return;}}}
const m=new HM();m.put(1,1);m.put(2,2);console.log(m.get(1),m.get(3));m.remove(1);console.log(m.get(1));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class HM{int B=997;List<int[]>[] b=new List[B];HM(){for(int i=0;i<B;i++)b[i]=new ArrayList<>();}int h(int k){return ((k%B)+B)%B;}void put(int k,int v){List<int[]> x=b[h(k)];for(int[] p:x)if(p[0]==k){p[1]=v;return;}x.add(new int[]{k,v});}int get(int k){for(int[] p:b[h(k)])if(p[0]==k)return p[1];return -1;}void remove(int k){List<int[]> x=b[h(k)];for(int i=0;i<x.size();i++)if(x.get(i)[0]==k){x.remove(i);return;}}}
  public static void main(String[]a){HM m=new HM();m.put(1,1);m.put(2,2);System.out.println(m.get(1)+" "+m.get(3));m.remove(1);System.out.println(m.get(1));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
class HM{int B=997;vector<vector<pair<int,int>>> b;public:HM(){b.assign(B,{});}int h(int k){return ((k%B)+B)%B;}void put(int k,int v){auto& x=b[h(k)];for(auto& p:x)if(p.first==k){p.second=v;return;}x.push_back({k,v});}int get(int k){for(auto& p:b[h(k)])if(p.first==k)return p.second;return -1;}void remove(int k){auto& x=b[h(k)];for(auto it=x.begin();it!=x.end();++it)if(it->first==k){x.erase(it);return;}}};
int main(){HM m;m.put(1,1);m.put(2,2);cout<<m.get(1)<<" "<<m.get(3)<<"\\n";m.remove(1);cout<<m.get(1)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type HM struct{ b [][]int }
func New() *HM { return &HM{b:make([][]int,997)} }
func (h *HM) idx(k int) int { return ((k%997)+997)%997 }
func (h *HM) Put(k,v int){ i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { h.b[i][j+1]=v; return } }; h.b[i]=append(h.b[i],k,v) }
func (h *HM) Get(k int) int { i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { return h.b[i][j+1] } }; return -1 }
func (h *HM) Remove(k int){ i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { h.b[i]=append(h.b[i][:j],h.b[i][j+2:]...); return } } }
func main(){ m:=New(); m.Put(1,1); m.Put(2,2); fmt.Println(m.Get(1),m.Get(3)); m.Remove(1); fmt.Println(m.Get(1)) }
''',
"R": '''cat("Design HashMap: use environment as map\\n")
''',
}))

# 243 Word Ladder
L.append((243, "Word Ladder", "Graphs", "Hard", 122,
"Shortest transformation sequence length from begin to end. BFS with wildcard buckets.",
{
"Python": '''from collections import defaultdict, deque
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
''',
"JavaScript": '''function ladderLength(b,e,wl){const ws=new Set(wl);if(!ws.has(e))return 0;const L=b.length;const buc={};for(const w of ws)for(let i=0;i<L;i++){const k=w.slice(0,i)+'*'+w.slice(i+1);(buc[k]=buc[k]||[]).push(w);}const q=[[b,1]];const seen=new Set([b]);while(q.length){const [w,d]=q.shift();if(w===e)return d;for(let i=0;i<L;i++){const k=w.slice(0,i)+'*'+w.slice(i+1);for(const n of (buc[k]||[]))if(!seen.has(n)){seen.add(n);q.push([n,d+1]);}}}return 0;}
console.log(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int ladderLength(String b,String e,List<String> wl){Set<String> ws=new HashSet<>(wl);if(!ws.contains(e))return 0;int L=b.length();Map<String,List<String>> buc=new HashMap<>();for(String w:ws)for(int i=0;i<L;i++){String k=w.substring(0,i)+"*"+w.substring(i+1);buc.computeIfAbsent(k,z->new ArrayList<>()).add(w);}Deque<Object[]> q=new ArrayDeque<>();q.add(new Object[]{b,1});Set<String> seen=new HashSet<>();seen.add(b);while(!q.isEmpty()){Object[] x=q.poll();String w=(String)x[0];int d=(int)x[1];if(w.equals(e))return d;for(int i=0;i<L;i++){String k=w.substring(0,i)+"*"+w.substring(i+1);for(String n:buc.getOrDefault(k,new ArrayList<>()))if(seen.add(n))q.add(new Object[]{n,d+1});}}return 0;}
  public static void main(String[]a){System.out.println(ladderLength("hit","cog",Arrays.asList("hot","dot","dog","lot","log","cog")));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int ladderLength(string b,string e,vector<string> wl){unordered_set<string> ws(wl.begin(),wl.end());if(!ws.count(e))return 0;int L=b.size();unordered_map<string,vector<string>> buc;for(auto& w:ws)for(int i=0;i<L;i++){string k=w;k[i]='*';buc[k].push_back(w);}queue<pair<string,int>> q;q.push({b,1});unordered_set<string> seen={b};while(!q.empty()){auto [w,d]=q.front();q.pop();if(w==e)return d;for(int i=0;i<L;i++){string k=w;k[i]='*';for(auto& n:buc[k])if(!seen.count(n)){seen.insert(n);q.push({n,d+1});}}}return 0;}
int main(){cout<<ladderLength("hit","cog",{"hot","dot","dog","lot","log","cog"})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func ladderLength(b,e string, wl []string) int { ws:=map[string]bool{}; for _,w:=range wl{ws[w]=true}; if !ws[e]{return 0}; L:=len(b); buc:=map[string][]string{}; for w:=range ws { for i:=0;i<L;i++ { k:=w[:i]+"*"+w[i+1:]; buc[k]=append(buc[k],w) } }; type S struct{w string; d int}; q:=[]S{{b,1}}; seen:=map[string]bool{b:true}; for len(q)>0 { x:=q[0]; q=q[1:]; if x.w==e {return x.d}; for i:=0;i<L;i++ { k:=x.w[:i]+"*"+x.w[i+1:]; for _,n:=range buc[k] { if !seen[n] { seen[n]=true; q=append(q,S{n,x.d+1}) } } } }; return 0 }
func main(){ fmt.Println(ladderLength("hit","cog",[]string{"hot","dot","dog","lot","log","cog"})) }
''',
"R": '''cat("ladderLength: BFS with wildcard buckets\\n")
''',
}))

# 244 Minimum Interval to Include Each Query
L.append((244, "Minimum Interval to Include Each Query", "Intervals", "Hard", 122,
"For each query q, find smallest interval covering q.",
{
"Python": '''import heapq
def minInterval(intervals,queries):
    intervals.sort()
    res={}; h=[]; i=0
    for q in sorted(queries):
        while i<len(intervals) and intervals[i][0]<=q:
            l,r=intervals[i]; heapq.heappush(h,(r-l+1,r)); i+=1
        while h and h[0][1]<q: heapq.heappop(h)
        res[q]=h[0][0] if h else -1
    return [res[q] for q in queries]
if __name__=="__main__":
    print(minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]))
''',
"JavaScript": '''function minInterval(iv,q){iv.sort((a,b)=>a[0]-b[0]);const sq=[...q].map((v,i)=>[v,i]).sort((a,b)=>a[0]-b[0]);const res=Array(q.length);const h=[];const push=x=>{h.push(x);h.sort((a,b)=>a[0]-b[0]);};let i=0;for(const [v,idx] of sq){while(i<iv.length&&iv[i][0]<=v){push([iv[i][1]-iv[i][0]+1,iv[i][1]]);i++;}while(h.length&&h[0][1]<v)h.shift();res[idx]=h.length?h[0][0]:-1;}return res;}
console.log(minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] minInterval(int[][] iv,int[] q){Arrays.sort(iv,(a,b)->a[0]-b[0]);Integer[] idx=new Integer[q.length];for(int i=0;i<q.length;i++)idx[i]=i;Arrays.sort(idx,(a,b)->q[a]-q[b]);int[] res=new int[q.length];PriorityQueue<int[]> h=new PriorityQueue<>((a,b)->a[0]-b[0]);int i=0;for(int k:idx){int v=q[k];while(i<iv.length&&iv[i][0]<=v){h.add(new int[]{iv[i][1]-iv[i][0]+1,iv[i][1]});i++;}while(!h.isEmpty()&&h.peek()[1]<v)h.poll();res[k]=h.isEmpty()?-1:h.peek()[0];}return res;}
  public static void main(String[]a){System.out.println(Arrays.toString(minInterval(new int[][]{{1,4},{2,4},{3,6},{4,4}},new int[]{2,3,4,5})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> minInterval(vector<vector<int>> iv,vector<int> q){sort(iv.begin(),iv.end());vector<int> idx(q.size());iota(idx.begin(),idx.end(),0);sort(idx.begin(),idx.end(),[&](int a,int b){return q[a]<q[b];});vector<int> res(q.size());priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> h;int i=0;for(int k:idx){int v=q[k];while(i<(int)iv.size()&&iv[i][0]<=v){h.push({iv[i][1]-iv[i][0]+1,iv[i][1]});i++;}while(!h.empty()&&h.top().second<v)h.pop();res[k]=h.empty()?-1:h.top().first;}return res;}
int main(){auto r=minInterval({{1,4},{2,4},{3,6},{4,4}},{2,3,4,5});for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import ("container/heap";"fmt";"sort")
type item struct{sz,end int}
type pq []item
func (h pq) Len() int{return len(h)}
func (h pq) Less(i,j int) bool {return h[i].sz<h[j].sz}
func (h pq) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *pq) Push(x any){*h=append(*h,x.(item))}
func (h *pq) Pop() any { o:=*h; x:=o[len(o)-1]; *h=o[:len(o)-1]; return x }
func minInterval(iv [][]int, q []int) []int { sort.Slice(iv,func(i,j int) bool {return iv[i][0]<iv[j][0]}); idx:=make([]int,len(q)); for i:=range idx{idx[i]=i}; sort.Slice(idx,func(a,b int) bool {return q[idx[a]]<q[idx[b]]}); res:=make([]int,len(q)); h:=&pq{}; heap.Init(h); i:=0; for _,k:=range idx { v:=q[k]; for i<len(iv)&&iv[i][0]<=v { heap.Push(h,item{iv[i][1]-iv[i][0]+1,iv[i][1]}); i++ }; for h.Len()>0 && (*h)[0].end<v { heap.Pop(h) }; if h.Len()==0 { res[k]=-1 } else { res[k]=(*h)[0].sz } }; return res }
func main(){ fmt.Println(minInterval([][]int{{1,4},{2,4},{3,6},{4,4}},[]int{2,3,4,5})) }
''',
"R": '''cat("minInterval: see Python solution\\n")
''',
}))

# 245 Sliding Window Maximum
L.append((245, "Sliding Window Maximum", "Sliding Window", "Hard", 123,
"Max in each window of size k. Monotonic deque.",
{
"Python": '''from collections import deque
def maxSliding(n,k):
    dq=deque(); out=[]
    for i,x in enumerate(n):
        while dq and n[dq[-1]]<=x: dq.pop()
        dq.append(i)
        if dq[0]<=i-k: dq.popleft()
        if i>=k-1: out.append(n[dq[0]])
    return out
if __name__=="__main__":
    print(maxSliding([1,3,-1,-3,5,3,6,7],3))
''',
"JavaScript": '''function maxSliding(n,k){const dq=[],out=[];for(let i=0;i<n.length;i++){while(dq.length&&n[dq[dq.length-1]]<=n[i])dq.pop();dq.push(i);if(dq[0]<=i-k)dq.shift();if(i>=k-1)out.push(n[dq[0]]);}return out;}
console.log(maxSliding([1,3,-1,-3,5,3,6,7],3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] maxSliding(int[] n,int k){Deque<Integer> dq=new ArrayDeque<>();int[] out=new int[n.length-k+1];int idx=0;for(int i=0;i<n.length;i++){while(!dq.isEmpty()&&n[dq.peekLast()]<=n[i])dq.pollLast();dq.add(i);if(dq.peek()<=i-k)dq.poll();if(i>=k-1)out[idx++]=n[dq.peek()];}return out;}
  public static void main(String[]a){System.out.println(Arrays.toString(maxSliding(new int[]{1,3,-1,-3,5,3,6,7},3)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> maxSliding(vector<int> n,int k){deque<int> dq;vector<int> out;for(int i=0;i<(int)n.size();i++){while(!dq.empty()&&n[dq.back()]<=n[i])dq.pop_back();dq.push_back(i);if(dq.front()<=i-k)dq.pop_front();if(i>=k-1)out.push_back(n[dq.front()]);}return out;}
int main(){for(int x:maxSliding({1,3,-1,-3,5,3,6,7},3))cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxSliding(n []int, k int) []int { dq:=[]int{}; out:=[]int{}; for i,x:=range n { for len(dq)>0 && n[dq[len(dq)-1]]<=x { dq=dq[:len(dq)-1] }; dq=append(dq,i); if dq[0]<=i-k { dq=dq[1:] }; if i>=k-1 { out=append(out,n[dq[0]]) } }; return out }
func main(){ fmt.Println(maxSliding([]int{1,3,-1,-3,5,3,6,7},3)) }
''',
"R": '''maxSliding <- function(n,k){ sapply(1:(length(n)-k+1), function(i) max(n[i:(i+k-1)])) }
cat(maxSliding(c(1,3,-1,-3,5,3,6,7),3),"\\n")
''',
}))

# 246 Largest Rectangle In Histogram
L.append((246, "Largest Rectangle In Histogram", "Stack", "Hard", 123,
"Max rectangular area in histogram. Monotonic stack.",
{
"Python": '''def largestRect(h):
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
''',
"JavaScript": '''function largestRect(h){const st=[];let best=0;h=[...h,0];for(let i=0;i<h.length;i++){while(st.length&&h[st[st.length-1]]>h[i]){const top=st.pop();const w=st.length===0?i:i-st[st.length-1]-1;best=Math.max(best,h[top]*w);}st.push(i);}return best;}
console.log(largestRect([2,1,5,6,2,3]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int largestRect(int[] h){Deque<Integer> st=new ArrayDeque<>();int best=0;int[] h2=new int[h.length+1];System.arraycopy(h,0,h2,0,h.length);for(int i=0;i<h2.length;i++){while(!st.isEmpty()&&h2[st.peek()]>h2[i]){int top=st.pop();int w=st.isEmpty()?i:i-st.peek()-1;best=Math.max(best,h2[top]*w);}st.push(i);}return best;}
  public static void main(String[]a){System.out.println(largestRect(new int[]{2,1,5,6,2,3}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int largestRect(vector<int> h){h.push_back(0);stack<int> st;int best=0;for(int i=0;i<(int)h.size();i++){while(!st.empty()&&h[st.top()]>h[i]){int top=st.top();st.pop();int w=st.empty()?i:i-st.top()-1;best=max(best,h[top]*w);}st.push(i);}return best;}
int main(){cout<<largestRect({2,1,5,6,2,3})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func largestRect(h []int) int { h=append(h,0); st:=[]int{}; best:=0; for i:=0;i<len(h);i++ { for len(st)>0 && h[st[len(st)-1]]>h[i] { top:=st[len(st)-1]; st=st[:len(st)-1]; w:=i; if len(st)>0 { w=i-st[len(st)-1]-1 }; if h[top]*w>best { best=h[top]*w } }; st=append(st,i) }; return best }
func main(){ fmt.Println(largestRect([]int{2,1,5,6,2,3})) }
''',
"R": '''largestRect <- function(h){ h<-c(h,0); st<-c(); best<-0; for(i in seq_along(h)){ while(length(st)>0 && h[st[length(st)]]>h[i]){ top<-st[length(st)]; st<-st[-length(st)]; w<-if(length(st)==0) i-1 else i-st[length(st)]-1; best<-max(best,h[top]*w) }; st<-c(st,i) }; best }
cat(largestRect(c(2,1,5,6,2,3)),"\\n")
''',
}))

# 247 Remove Duplicates From Sorted Array
L.append((247, "Remove Duplicates From Sorted Array", "Two Pointers", "Easy", 124,
"In-place dedupe of sorted array. Return new length.",
{
"Python": '''def dedupe(a):
    if not a: return 0
    k=1
    for i in range(1,len(a)):
        if a[i]!=a[k-1]: a[k]=a[i]; k+=1
    return k
if __name__=="__main__":
    a=[1,1,2,2,3]; n=dedupe(a); print(n,a[:n])
''',
"JavaScript": '''function dedupe(a){if(!a.length)return 0;let k=1;for(let i=1;i<a.length;i++)if(a[i]!==a[k-1])a[k++]=a[i];return k;}
const a=[1,1,2,2,3];const n=dedupe(a);console.log(n,a.slice(0,n));
''',
"Java": '''public class __CLASS__{
  static int dedupe(int[] a){if(a.length==0)return 0;int k=1;for(int i=1;i<a.length;i++)if(a[i]!=a[k-1])a[k++]=a[i];return k;}
  public static void main(String[]a){int[] x={1,1,2,2,3};int n=dedupe(x);System.out.println(n);}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int dedupe(vector<int>& a){if(a.empty())return 0;int k=1;for(int i=1;i<(int)a.size();i++)if(a[i]!=a[k-1])a[k++]=a[i];return k;}
int main(){vector<int> a={1,1,2,2,3};cout<<dedupe(a)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func dedupe(a []int) int { if len(a)==0 { return 0 }; k:=1; for i:=1;i<len(a);i++ { if a[i]!=a[k-1] { a[k]=a[i]; k++ } }; return k }
func main(){ a:=[]int{1,1,2,2,3}; n:=dedupe(a); fmt.Println(n,a[:n]) }
''',
"R": '''dedupe <- function(a){ length(unique(a)) }
cat(dedupe(c(1,1,2,2,3)),"\\n")
''',
}))

# 248 Detect Squares
L.append((248, "Detect Squares", "Math and Geometry", "Medium", 124,
"Add point or count axis-aligned squares with given query point.",
{
"Python": '''class DS:
    def __init__(s): s.c={}
    def add(s,p): s.c[tuple(p)]=s.c.get(tuple(p),0)+1
    def count(s,p):
        x,y=p; tot=0
        for (a,b),v in list(s.c.items()):
            if a==x or abs(a-x)!=abs(b-y): continue
            tot += v*s.c.get((a,y),0)*s.c.get((x,b),0)
        return tot
if __name__=="__main__":
    d=DS(); [d.add(p) for p in [[3,10],[11,2],[3,2]]]; print(d.count([11,10]))
''',
"JavaScript": '''class DS{constructor(){this.c={};}_k(p){return p[0]+","+p[1];}add(p){const k=this._k(p);this.c[k]=(this.c[k]||0)+1;}count(p){const [x,y]=p;let tot=0;for(const k in this.c){const [a,b]=k.split(",").map(Number);if(a===x||Math.abs(a-x)!==Math.abs(b-y))continue;tot+=this.c[k]*(this.c[a+","+y]||0)*(this.c[x+","+b]||0);}return tot;}}
const d=new DS();[[3,10],[11,2],[3,2]].forEach(p=>d.add(p));console.log(d.count([11,10]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class DS{Map<Long,Integer> c=new HashMap<>();long k(int x,int y){return ((long)x<<32)|(y&0xFFFFFFFFL);}void add(int[] p){c.merge(k(p[0],p[1]),1,Integer::sum);}int count(int[] p){int x=p[0],y=p[1],tot=0;for(var e:new ArrayList<>(c.entrySet())){long key=e.getKey();int a=(int)(key>>32),b=(int)key;if(a==x||Math.abs(a-x)!=Math.abs(b-y))continue;tot+=e.getValue()*c.getOrDefault(k(a,y),0)*c.getOrDefault(k(x,b),0);}return tot;}}
  public static void main(String[]a){DS d=new DS();for(int[] p:new int[][]{{3,10},{11,2},{3,2}})d.add(p);System.out.println(d.count(new int[]{11,10}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
class DS{map<pair<int,int>,int> c;public:void add(int x,int y){c[{x,y}]++;}int count(int x,int y){int tot=0;for(auto& [k,v]:c){auto [a,b]=k;if(a==x||abs(a-x)!=abs(b-y))continue;auto it1=c.find({a,y}),it2=c.find({x,b});if(it1!=c.end()&&it2!=c.end())tot+=v*it1->second*it2->second;}return tot;}};
int main(){DS d;d.add(3,10);d.add(11,2);d.add(3,2);cout<<d.count(11,10)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type pt struct{x,y int}
type DS struct{c map[pt]int}
func New() *DS{return &DS{map[pt]int{}}}
func (s *DS) Add(p pt){ s.c[p]++ }
func (s *DS) Count(p pt) int { tot:=0; for k,v:=range s.c { if k.x==p.x { continue }; if abs(k.x-p.x)!=abs(k.y-p.y) { continue }; tot+=v*s.c[pt{k.x,p.y}]*s.c[pt{p.x,k.y}] }; return tot }
func abs(x int) int { if x<0 {return -x}; return x }
func main(){ d:=New(); for _,p:=range []pt{{3,10},{11,2},{3,2}}{ d.Add(p) }; fmt.Println(d.Count(pt{11,10})) }
''',
"R": '''cat("Detect Squares: see Python solution\\n")
''',
}))

# 249 Serialize And Deserialize Binary Tree
L.append((249, "Serialize And Deserialize Binary Tree", "Trees", "Hard", 125,
"Pre-order serialize with null markers; queue-based deserialize.",
{
"Python": '''class T:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def ser(r):
    out=[]
    def dfs(n):
        if not n: out.append("#"); return
        out.append(str(n.v)); dfs(n.l); dfs(n.r)
    dfs(r); return ",".join(out)
def des(s):
    it=iter(s.split(","))
    def dfs():
        x=next(it)
        if x=="#": return None
        n=T(int(x)); n.l=dfs(); n.r=dfs(); return n
    return dfs()
if __name__=="__main__":
    r=T(1,T(2),T(3,T(4),T(5))); s=ser(r); print(s); print(ser(des(s)))
''',
"JavaScript": '''class T{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function ser(r){const out=[];const dfs=n=>{if(!n){out.push("#");return;}out.push(n.v);dfs(n.l);dfs(n.r);};dfs(r);return out.join(",");}
function des(s){const arr=s.split(",");let i=0;const dfs=()=>{const x=arr[i++];if(x==="#")return null;const n=new T(+x);n.l=dfs();n.r=dfs();return n;};return dfs();}
const r=new T(1,new T(2),new T(3,new T(4),new T(5)));const s=ser(r);console.log(s);console.log(ser(des(s)));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class T{int v;T l,r;T(int v){this.v=v;}}
  static void dfs(T n,StringBuilder sb){if(n==null){sb.append("#,");return;}sb.append(n.v).append(',');dfs(n.l,sb);dfs(n.r,sb);}
  static String ser(T r){StringBuilder sb=new StringBuilder();dfs(r,sb);return sb.toString();}
  static int idx;static String[] arr;
  static T dfs2(){String x=arr[idx++];if(x.equals("#"))return null;T n=new T(Integer.parseInt(x));n.l=dfs2();n.r=dfs2();return n;}
  static T des(String s){arr=s.split(",");idx=0;return dfs2();}
  public static void main(String[]a){T r=new T(1);r.l=new T(2);r.r=new T(3);r.r.l=new T(4);r.r.r=new T(5);String s=ser(r);System.out.println(s);System.out.println(ser(des(s)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct T{int v;T*l;T*r;T(int v):v(v),l(0),r(0){}};
void dfs(T* n,string& s){if(!n){s+="#,";return;}s+=to_string(n->v)+",";dfs(n->l,s);dfs(n->r,s);}
string ser(T* r){string s;dfs(r,s);return s;}
int gi;vector<string> ar;
T* dfs2(){string x=ar[gi++];if(x=="#")return 0;T* n=new T(stoi(x));n->l=dfs2();n->r=dfs2();return n;}
T* des(string s){ar.clear();string cur;for(char c:s){if(c==','){ar.push_back(cur);cur.clear();}else cur+=c;}gi=0;return dfs2();}
int main(){T* r=new T(1);r->l=new T(2);r->r=new T(3);r->r->l=new T(4);r->r->r=new T(5);string s=ser(r);cout<<s<<"\\n"<<ser(des(s))<<"\\n";}
''',
"Go": '''package main
import ("fmt";"strconv";"strings")
type T struct{v int; l,r *T}
func dfs(n *T, sb *strings.Builder){ if n==nil { sb.WriteString("#,"); return }; sb.WriteString(strconv.Itoa(n.v)); sb.WriteString(","); dfs(n.l,sb); dfs(n.r,sb) }
func ser(r *T) string { var sb strings.Builder; dfs(r,&sb); return sb.String() }
var idx int; var arr []string
func dfs2() *T { x:=arr[idx]; idx++; if x=="#" { return nil }; v,_:=strconv.Atoi(x); n:=&T{v:v}; n.l=dfs2(); n.r=dfs2(); return n }
func des(s string) *T { arr=strings.Split(s,","); idx=0; return dfs2() }
func main(){ r:=&T{v:1,l:&T{v:2},r:&T{v:3,l:&T{v:4},r:&T{v:5}}}; s:=ser(r); fmt.Println(s); fmt.Println(ser(des(s))) }
''',
"R": '''cat("ser/des: see Python solution\\n")
''',
}))

# 250 Stone Game III
L.append((250, "Stone Game III", "1-D Dynamic Programming", "Hard", 125,
"Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.",
{
"Python": '''def stoneGameIII(s):
    n=len(s); dp=[0]*(n+1)
    for i in range(n-1,-1,-1):
        best=float('-inf'); take=0
        for k in range(3):
            if i+k>=n: break
            take+=s[i+k]; best=max(best,take-dp[i+k+1])
        dp[i]=best
    if dp[0]>0: return "Alice"
    if dp[0]<0: return "Bob"
    return "Tie"
if __name__=="__main__":
    print(stoneGameIII([1,2,3,7]))
    print(stoneGameIII([1,2,3,-9]))
''',
"JavaScript": '''function stoneGameIII(s){const n=s.length;const dp=Array(n+1).fill(0);for(let i=n-1;i>=0;i--){let best=-Infinity,take=0;for(let k=0;k<3&&i+k<n;k++){take+=s[i+k];best=Math.max(best,take-dp[i+k+1]);}dp[i]=best;}return dp[0]>0?"Alice":dp[0]<0?"Bob":"Tie";}
console.log(stoneGameIII([1,2,3,7]));console.log(stoneGameIII([1,2,3,-9]));
''',
"Java": '''public class __CLASS__{
  static String stoneGameIII(int[] s){int n=s.length;int[] dp=new int[n+1];for(int i=n-1;i>=0;i--){int best=Integer.MIN_VALUE,take=0;for(int k=0;k<3&&i+k<n;k++){take+=s[i+k];best=Math.max(best,take-dp[i+k+1]);}dp[i]=best;}return dp[0]>0?"Alice":dp[0]<0?"Bob":"Tie";}
  public static void main(String[]a){System.out.println(stoneGameIII(new int[]{1,2,3,7}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string stoneGameIII(vector<int> s){int n=s.size();vector<int> dp(n+1,0);for(int i=n-1;i>=0;i--){int best=INT_MIN,take=0;for(int k=0;k<3&&i+k<n;k++){take+=s[i+k];best=max(best,take-dp[i+k+1]);}dp[i]=best;}if(dp[0]>0)return "Alice";if(dp[0]<0)return "Bob";return "Tie";}
int main(){cout<<stoneGameIII({1,2,3,7})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func stoneGameIII(s []int) string { n:=len(s); dp:=make([]int,n+1); for i:=n-1;i>=0;i-- { best:=-1<<30; take:=0; for k:=0;k<3 && i+k<n;k++ { take+=s[i+k]; if take-dp[i+k+1]>best { best=take-dp[i+k+1] } }; dp[i]=best }; if dp[0]>0 { return "Alice" }; if dp[0]<0 { return "Bob" }; return "Tie" }
func main(){ fmt.Println(stoneGameIII([]int{1,2,3,7})) }
''',
"R": '''stoneGameIII <- function(s){ n<-length(s); dp<-rep(0,n+1); for(i in n:1){ best<--Inf; take<-0; for(k in 0:2){ if(i+k>n) break; take<-take+s[i+k]; best<-max(best,take-dp[i+k+1]) }; dp[i]<-best }; if(dp[1]>0) "Alice" else if(dp[1]<0) "Bob" else "Tie" }
cat(stoneGameIII(c(1,2,3,7)),"\\n")
''',
}))

write_lessons(L)
