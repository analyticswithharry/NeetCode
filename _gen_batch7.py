"""Batch 7: lessons 136-160."""
from _lesson_writer import write_lessons

L = []

# 136 Car Pooling
L.append((136, "Car Pooling", "Heap Priority Queue", "Medium", 68,
"Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.",
{
"Python": '''def carPool(t,cap):
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
''',
"JavaScript": '''function carPool(t,cap){const e=new Array(1001).fill(0);for(const [n,a,b] of t){e[a]+=n;e[b]-=n;}let s=0;for(const v of e){s+=v;if(s>cap)return false;}return true;}
console.log(carPool([[2,1,5],[3,3,7]],4));console.log(carPool([[2,1,5],[3,3,7]],5));
''',
"Java": '''public class __CLASS__{
  static boolean carPool(int[][]t,int cap){int[] e=new int[1001];for(int[] x:t){e[x[1]]+=x[0];e[x[2]]-=x[0];}int s=0;for(int v:e){s+=v;if(s>cap)return false;}return true;}
  public static void main(String[]x){System.out.println(carPool(new int[][]{{2,1,5},{3,3,7}},4));System.out.println(carPool(new int[][]{{2,1,5},{3,3,7}},5));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool carPool(vector<vector<int>> t,int cap){vector<int> e(1001,0);for(auto& x:t){e[x[1]]+=x[0];e[x[2]]-=x[0];}int s=0;for(int v:e){s+=v;if(s>cap)return false;}return true;}
int main(){cout<<boolalpha<<carPool({{2,1,5},{3,3,7}},4)<<"\\n"<<carPool({{2,1,5},{3,3,7}},5)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func carPool(t [][]int,cap int) bool { e:=make([]int,1001); for _,x:=range t { e[x[1]]+=x[0]; e[x[2]]-=x[0] }; s:=0; for _,v:=range e { s+=v; if s>cap { return false } }; return true }
func main(){ fmt.Println(carPool([][]int{{2,1,5},{3,3,7}},4)); fmt.Println(carPool([][]int{{2,1,5},{3,3,7}},5)) }
''',
"R": '''carPool <- function(t,cap){ e<-rep(0,1001); for(x in t){ e[x[2]+1]<-e[x[2]+1]+x[1]; e[x[3]+1]<-e[x[3]+1]-x[1] }; s<-0; for(v in e){ s<-s+v; if(s>cap) return(FALSE) }; TRUE }
cat(carPool(list(c(2,1,5),c(3,3,7)),4),"\\n"); cat(carPool(list(c(2,1,5),c(3,3,7)),5),"\\n")
''',
}))

# 137 Letter Combinations of Phone Number
L.append((137, "Letter Combinations of a Phone Number", "Backtracking", "Medium", 69,
"Given digits 2-9, return all possible letter combinations the number could represent.",
{
"Python": '''def letters(d):
    if not d: return []
    m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=['']
    for c in d:
        res=[p+ch for p in res for ch in m[c]]
    return res

if __name__=="__main__":
    print(letters("23"))
''',
"JavaScript": '''function letters(d){if(!d)return [];const m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'};let r=[''];for(const c of d){const n=[];for(const p of r)for(const x of m[c])n.push(p+x);r=n;}return r;}
console.log(letters("23"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<String> letters(String d){if(d.isEmpty())return new ArrayList<>();String[] m={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};List<String> r=new ArrayList<>();r.add("");for(char c:d.toCharArray()){List<String> n=new ArrayList<>();for(String p:r)for(char x:m[c-'0'].toCharArray())n.add(p+x);r=n;}return r;}
  public static void main(String[]x){System.out.println(letters("23"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<string> letters(string d){if(d.empty())return {};vector<string> m={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};vector<string> r={""};for(char c:d){vector<string> n;for(auto& p:r)for(char x:m[c-'0'])n.push_back(p+x);r=n;}return r;}
int main(){auto v=letters("23");for(auto&s:v)cout<<s<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func letters(d string) []string { if d=="" { return nil }; m:=[]string{"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"}; r:=[]string{""}; for _,c:=range d { var n []string; for _,p:=range r { for _,x:=range m[c-'0'] { n=append(n,p+string(x)) } }; r=n }; return r }
func main(){ fmt.Println(letters("23")) }
''',
"R": '''letters_pn <- function(d){ if(nchar(d)==0) return(c()); m<-list("2"="abc","3"="def","4"="ghi","5"="jkl","6"="mno","7"="pqrs","8"="tuv","9"="wxyz"); r<-c(""); for(c in strsplit(d,"")[[1]]){ n<-c(); for(p in r) for(x in strsplit(m[[c]],"")[[1]]) n<-c(n,paste0(p,x)); r<-n }; r }
print(letters_pn("23"))
''',
}))

# 138 Matchsticks to Square
L.append((138, "Matchsticks to Square", "Backtracking", "Medium", 69,
"Use all matchsticks to form a square. Return true if possible.",
{
"Python": '''def square(m):
    s=sum(m)
    if s%4: return False
    side=s//4; m.sort(reverse=True)
    if m[0]>side: return False
    sides=[0]*4
    def rec(i):
        if i==len(m): return sides[0]==sides[1]==sides[2]==side
        for j in range(4):
            if sides[j]+m[i]<=side:
                if j>0 and sides[j]==sides[j-1]: continue
                sides[j]+=m[i]
                if rec(i+1): return True
                sides[j]-=m[i]
        return False
    return rec(0)

if __name__=="__main__":
    print(square([1,1,2,2,2]))
    print(square([3,3,3,3,4]))
''',
"JavaScript": '''function square(m){const s=m.reduce((a,b)=>a+b,0);if(s%4)return false;const side=s/4;m.sort((a,b)=>b-a);if(m[0]>side)return false;const sides=[0,0,0,0];function rec(i){if(i===m.length)return sides[0]===side&&sides[1]===side&&sides[2]===side;for(let j=0;j<4;j++){if(sides[j]+m[i]>side)continue;if(j>0&&sides[j]===sides[j-1])continue;sides[j]+=m[i];if(rec(i+1))return true;sides[j]-=m[i];}return false;}return rec(0);}
console.log(square([1,1,2,2,2]));console.log(square([3,3,3,3,4]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] M; static int SIDE; static int[] S=new int[4];
  static boolean rec(int i){if(i==M.length)return S[0]==SIDE&&S[1]==SIDE&&S[2]==SIDE;for(int j=0;j<4;j++){if(S[j]+M[i]>SIDE)continue;if(j>0&&S[j]==S[j-1])continue;S[j]+=M[i];if(rec(i+1))return true;S[j]-=M[i];}return false;}
  static boolean square(int[]m){int s=0;for(int x:m)s+=x;if(s%4!=0)return false;SIDE=s/4;Arrays.sort(m);for(int i=0,j=m.length-1;i<j;i++,j--){int t=m[i];m[i]=m[j];m[j]=t;}if(m[0]>SIDE)return false;M=m;S=new int[4];return rec(0);}
  public static void main(String[]x){System.out.println(square(new int[]{1,1,2,2,2}));System.out.println(square(new int[]{3,3,3,3,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> M; int SIDE; vector<int> S(4,0);
bool rec(int i){if(i==(int)M.size())return S[0]==SIDE&&S[1]==SIDE&&S[2]==SIDE;for(int j=0;j<4;j++){if(S[j]+M[i]>SIDE)continue;if(j>0&&S[j]==S[j-1])continue;S[j]+=M[i];if(rec(i+1))return true;S[j]-=M[i];}return false;}
bool square(vector<int> m){int s=0;for(int x:m)s+=x;if(s%4)return false;SIDE=s/4;sort(m.rbegin(),m.rend());if(m[0]>SIDE)return false;M=m;S=vector<int>(4,0);return rec(0);}
int main(){cout<<boolalpha<<square({1,1,2,2,2})<<"\\n"<<square({3,3,3,3,4})<<"\\n";}
''',
"Go": '''package main
import ("fmt";"sort")
func square(m []int) bool { s:=0; for _,x:=range m { s+=x }; if s%4!=0 { return false }; side:=s/4; sort.Sort(sort.Reverse(sort.IntSlice(m))); if m[0]>side { return false }; sides:=[4]int{}; var rec func(i int) bool; rec=func(i int) bool { if i==len(m) { return sides[0]==side && sides[1]==side && sides[2]==side }; for j:=0;j<4;j++ { if sides[j]+m[i]>side { continue }; if j>0 && sides[j]==sides[j-1] { continue }; sides[j]+=m[i]; if rec(i+1) { return true }; sides[j]-=m[i] }; return false }; return rec(0) }
func main(){ fmt.Println(square([]int{1,1,2,2,2})); fmt.Println(square([]int{3,3,3,3,4})) }
''',
"R": '''square <- function(m){ s<-sum(m); if(s%%4!=0) return(FALSE); side<-s/4; m<-sort(m,decreasing=TRUE); if(m[1]>side) return(FALSE); sides<-c(0,0,0,0); rec<-function(i){ if(i>length(m)) return(sides[1]==side && sides[2]==side && sides[3]==side); for(j in 1:4){ if(sides[j]+m[i]>side) next; if(j>1 && sides[j]==sides[j-1]) next; sides[j]<<-sides[j]+m[i]; if(rec(i+1)) return(TRUE); sides[j]<<-sides[j]-m[i] }; FALSE }; rec(1) }
cat(square(c(1,1,2,2,2)),"\\n"); cat(square(c(3,3,3,3,4)),"\\n")
''',
}))

# 139 Roman to Integer
L.append((139, "Roman to Integer", "Math and Geometry", "Easy", 70,
"Convert Roman numeral string to integer.",
{
"Python": '''def r2i(s):
    m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; t=0; p=0
    for c in reversed(s):
        v=m[c]
        if v<p: t-=v
        else: t+=v; p=v
    return t

if __name__=="__main__":
    print(r2i("III")); print(r2i("LVIII")); print(r2i("MCMXCIV"))
''',
"JavaScript": '''function r2i(s){const m={I:1,V:5,X:10,L:50,C:100,D:500,M:1000};let t=0,p=0;for(let i=s.length-1;i>=0;i--){const v=m[s[i]];if(v<p)t-=v;else{t+=v;p=v;}}return t;}
console.log(r2i("III"));console.log(r2i("LVIII"));console.log(r2i("MCMXCIV"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int r2i(String s){Map<Character,Integer> m=Map.of('I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000);int t=0,p=0;for(int i=s.length()-1;i>=0;i--){int v=m.get(s.charAt(i));if(v<p)t-=v;else{t+=v;p=v;}}return t;}
  public static void main(String[]x){System.out.println(r2i("III"));System.out.println(r2i("LVIII"));System.out.println(r2i("MCMXCIV"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int r2i(string s){unordered_map<char,int> m={{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};int t=0,p=0;for(int i=s.size()-1;i>=0;i--){int v=m[s[i]];if(v<p)t-=v;else{t+=v;p=v;}}return t;}
int main(){cout<<r2i("III")<<"\\n"<<r2i("LVIII")<<"\\n"<<r2i("MCMXCIV")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func r2i(s string) int { m:=map[byte]int{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; t,p:=0,0; for i:=len(s)-1;i>=0;i-- { v:=m[s[i]]; if v<p { t-=v } else { t+=v; p=v } }; return t }
func main(){ fmt.Println(r2i("III")); fmt.Println(r2i("LVIII")); fmt.Println(r2i("MCMXCIV")) }
''',
"R": '''r2i <- function(s){ m<-c(I=1,V=5,X=10,L=50,C=100,D=500,M=1000); cs<-rev(strsplit(s,"")[[1]]); t<-0; p<-0; for(c in cs){ v<-m[[c]]; if(v<p) t<-t-v else { t<-t+v; p<-v } }; t }
cat(r2i("III"),"\\n"); cat(r2i("LVIII"),"\\n"); cat(r2i("MCMXCIV"),"\\n")
''',
}))

# 140 Set Matrix Zeroes
L.append((140, "Set Matrix Zeroes", "Math and Geometry", "Medium", 70,
"Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.",
{
"Python": '''def setZero(g):
    m,n=len(g),len(g[0]); r0=any(g[0][j]==0 for j in range(n)); c0=any(g[i][0]==0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if g[i][j]==0: g[i][0]=0; g[0][j]=0
    for i in range(1,m):
        for j in range(1,n):
            if g[i][0]==0 or g[0][j]==0: g[i][j]=0
    if r0:
        for j in range(n): g[0][j]=0
    if c0:
        for i in range(m): g[i][0]=0
    return g

if __name__=="__main__":
    print(setZero([[1,1,1],[1,0,1],[1,1,1]]))
''',
"JavaScript": '''function setZero(g){const m=g.length,n=g[0].length;let r0=false,c0=false;for(let j=0;j<n;j++)if(g[0][j]===0)r0=true;for(let i=0;i<m;i++)if(g[i][0]===0)c0=true;for(let i=1;i<m;i++)for(let j=1;j<n;j++)if(g[i][j]===0){g[i][0]=0;g[0][j]=0;}for(let i=1;i<m;i++)for(let j=1;j<n;j++)if(g[i][0]===0||g[0][j]===0)g[i][j]=0;if(r0)for(let j=0;j<n;j++)g[0][j]=0;if(c0)for(let i=0;i<m;i++)g[i][0]=0;return g;}
console.log(setZero([[1,1,1],[1,0,1],[1,1,1]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[][] setZero(int[][]g){int m=g.length,n=g[0].length;boolean r0=false,c0=false;for(int j=0;j<n;j++)if(g[0][j]==0)r0=true;for(int i=0;i<m;i++)if(g[i][0]==0)c0=true;for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][j]==0){g[i][0]=0;g[0][j]=0;}for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][0]==0||g[0][j]==0)g[i][j]=0;if(r0)for(int j=0;j<n;j++)g[0][j]=0;if(c0)for(int i=0;i<m;i++)g[i][0]=0;return g;}
  public static void main(String[]x){System.out.println(Arrays.deepToString(setZero(new int[][]{{1,1,1},{1,0,1},{1,1,1}})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> setZero(vector<vector<int>> g){int m=g.size(),n=g[0].size();bool r0=false,c0=false;for(int j=0;j<n;j++)if(g[0][j]==0)r0=true;for(int i=0;i<m;i++)if(g[i][0]==0)c0=true;for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][j]==0){g[i][0]=0;g[0][j]=0;}for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][0]==0||g[0][j]==0)g[i][j]=0;if(r0)for(int j=0;j<n;j++)g[0][j]=0;if(c0)for(int i=0;i<m;i++)g[i][0]=0;return g;}
int main(){auto r=setZero({{1,1,1},{1,0,1},{1,1,1}});for(auto&row:r){for(int x:row)cout<<x<<" ";cout<<"\\n";}}
''',
"Go": '''package main
import "fmt"
func setZero(g [][]int) [][]int { m,n:=len(g),len(g[0]); r0,c0:=false,false; for j:=0;j<n;j++ { if g[0][j]==0 { r0=true } }; for i:=0;i<m;i++ { if g[i][0]==0 { c0=true } }; for i:=1;i<m;i++ { for j:=1;j<n;j++ { if g[i][j]==0 { g[i][0]=0; g[0][j]=0 } } }; for i:=1;i<m;i++ { for j:=1;j<n;j++ { if g[i][0]==0 || g[0][j]==0 { g[i][j]=0 } } }; if r0 { for j:=0;j<n;j++ { g[0][j]=0 } }; if c0 { for i:=0;i<m;i++ { g[i][0]=0 } }; return g }
func main(){ fmt.Println(setZero([][]int{{1,1,1},{1,0,1},{1,1,1}})) }
''',
"R": '''setZero <- function(g){ m<-nrow(g); n<-ncol(g); r0<-any(g[1,]==0); c0<-any(g[,1]==0); for(i in 2:m) for(j in 2:n) if(g[i,j]==0){ g[i,1]<-0; g[1,j]<-0 }; for(i in 2:m) for(j in 2:n) if(g[i,1]==0 || g[1,j]==0) g[i,j]<-0; if(r0) g[1,]<-0; if(c0) g[,1]<-0; g }
print(setZero(matrix(c(1,1,1,1,0,1,1,1,1),3,3,byrow=TRUE)))
''',
}))

# 141 Binary Tree Level Order Traversal
L.append((141, "Binary Tree Level Order Traversal", "Trees", "Medium", 71,
"Return level-order traversal of a binary tree (values grouped by level).",
{
"Python": '''from collections import deque
class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def levels(root):
    if not root: return []
    q=deque([root]); res=[]
    while q:
        lvl=[]
        for _ in range(len(q)):
            n=q.popleft(); lvl.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(lvl)
    return res

if __name__=="__main__":
    r=TN(3,TN(9),TN(20,TN(15),TN(7)))
    print(levels(r))
''',
"JavaScript": '''class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function levels(root){if(!root)return [];const q=[root],res=[];while(q.length){const lvl=[];const n=q.length;for(let i=0;i<n;i++){const x=q.shift();lvl.push(x.val);if(x.left)q.push(x.left);if(x.right)q.push(x.right);}res.push(lvl);}return res;}
const r=new TN(3,new TN(9),new TN(20,new TN(15),new TN(7)));
console.log(JSON.stringify(levels(r)));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static List<List<Integer>> levels(TN root){List<List<Integer>> res=new ArrayList<>();if(root==null)return res;Queue<TN> q=new ArrayDeque<>();q.add(root);while(!q.isEmpty()){List<Integer> lvl=new ArrayList<>();int n=q.size();for(int i=0;i<n;i++){TN x=q.poll();lvl.add(x.val);if(x.left!=null)q.add(x.left);if(x.right!=null)q.add(x.right);}res.add(lvl);}return res;}
  public static void main(String[]x){TN r=new TN(3,new TN(9,null,null),new TN(20,new TN(15,null,null),new TN(7,null,null)));System.out.println(levels(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct TN{int val;TN*l;TN*r;TN(int v,TN*a=nullptr,TN*b=nullptr):val(v),l(a),r(b){}};
vector<vector<int>> levels(TN* root){vector<vector<int>> res;if(!root)return res;queue<TN*> q;q.push(root);while(!q.empty()){vector<int> lvl;int n=q.size();for(int i=0;i<n;i++){auto x=q.front();q.pop();lvl.push_back(x->val);if(x->l)q.push(x->l);if(x->r)q.push(x->r);}res.push_back(lvl);}return res;}
int main(){TN n15(15),n7(7),n9(9),n20(20,&n15,&n7),n3(3,&n9,&n20);auto r=levels(&n3);for(auto& v:r){for(int x:v)cout<<x<<" ";cout<<"| ";}cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func levels(root *TN) [][]int { var res [][]int; if root==nil { return res }; q:=[]*TN{root}; for len(q)>0 { var lvl []int; n:=len(q); for i:=0;i<n;i++ { x:=q[0]; q=q[1:]; lvl=append(lvl,x.Val); if x.L!=nil { q=append(q,x.L) }; if x.R!=nil { q=append(q,x.R) } }; res=append(res,lvl) }; return res }
func main(){ r:=&TN{3,&TN{9,nil,nil},&TN{20,&TN{15,nil,nil},&TN{7,nil,nil}}}; fmt.Println(levels(r)) }
''',
"R": '''levels <- function(root){ if(is.null(root)) return(list()); q<-list(root); res<-list(); while(length(q)>0){ lvl<-c(); nq<-list(); for(x in q){ lvl<-c(lvl,x$val); if(!is.null(x$l)) nq[[length(nq)+1]]<-x$l; if(!is.null(x$r)) nq[[length(nq)+1]]<-x$r }; q<-nq; res[[length(res)+1]]<-lvl }; res }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
print(levels(TN(3,TN(9),TN(20,TN(15),TN(7)))))
''',
}))

# 142 Right Side View
L.append((142, "Binary Tree Right Side View", "Trees", "Medium", 71,
"Return values seen from the right side of a binary tree.",
{
"Python": '''from collections import deque
class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def view(root):
    if not root: return []
    q=deque([root]); res=[]
    while q:
        n=len(q)
        for i in range(n):
            x=q.popleft()
            if i==n-1: res.append(x.val)
            if x.left: q.append(x.left)
            if x.right: q.append(x.right)
    return res

if __name__=="__main__":
    r=TN(1,TN(2,None,TN(5)),TN(3,None,TN(4)))
    print(view(r))
''',
"JavaScript": '''class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function view(root){if(!root)return [];const q=[root],res=[];while(q.length){const n=q.length;for(let i=0;i<n;i++){const x=q.shift();if(i===n-1)res.push(x.val);if(x.left)q.push(x.left);if(x.right)q.push(x.right);}}return res;}
const r=new TN(1,new TN(2,null,new TN(5)),new TN(3,null,new TN(4)));
console.log(view(r));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static List<Integer> view(TN root){List<Integer> res=new ArrayList<>();if(root==null)return res;Queue<TN> q=new ArrayDeque<>();q.add(root);while(!q.isEmpty()){int n=q.size();for(int i=0;i<n;i++){TN x=q.poll();if(i==n-1)res.add(x.val);if(x.left!=null)q.add(x.left);if(x.right!=null)q.add(x.right);}}return res;}
  public static void main(String[]x){TN r=new TN(1,new TN(2,null,new TN(5,null,null)),new TN(3,null,new TN(4,null,null)));System.out.println(view(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct TN{int val;TN*l;TN*r;TN(int v,TN*a=nullptr,TN*b=nullptr):val(v),l(a),r(b){}};
vector<int> view(TN* root){vector<int> res;if(!root)return res;queue<TN*> q;q.push(root);while(!q.empty()){int n=q.size();for(int i=0;i<n;i++){auto x=q.front();q.pop();if(i==n-1)res.push_back(x->val);if(x->l)q.push(x->l);if(x->r)q.push(x->r);}}return res;}
int main(){TN n5(5),n4(4),n2(2,nullptr,&n5),n3(3,nullptr,&n4),n1(1,&n2,&n3);auto r=view(&n1);for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func view(root *TN) []int { if root==nil { return nil }; q:=[]*TN{root}; var res []int; for len(q)>0 { n:=len(q); for i:=0;i<n;i++ { x:=q[0]; q=q[1:]; if i==n-1 { res=append(res,x.Val) }; if x.L!=nil { q=append(q,x.L) }; if x.R!=nil { q=append(q,x.R) } } }; return res }
func main(){ r:=&TN{1,&TN{2,nil,&TN{5,nil,nil}},&TN{3,nil,&TN{4,nil,nil}}}; fmt.Println(view(r)) }
''',
"R": '''view <- function(root){ if(is.null(root)) return(c()); q<-list(root); res<-c(); while(length(q)>0){ n<-length(q); nq<-list(); for(i in 1:n){ x<-q[[i]]; if(i==n) res<-c(res,x$val); if(!is.null(x$l)) nq[[length(nq)+1]]<-x$l; if(!is.null(x$r)) nq[[length(nq)+1]]<-x$r }; q<-nq }; res }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
print(view(TN(1,TN(2,NULL,TN(5)),TN(3,NULL,TN(4)))))
''',
}))

# 143 Palindromic Substrings
L.append((143, "Palindromic Substrings", "1-D Dynamic Programming", "Medium", 72,
"Count number of palindromic substrings in s.",
{
"Python": '''def count(s):
    c=0
    for i in range(len(s)):
        for a,b in [(i,i),(i,i+1)]:
            while a>=0 and b<len(s) and s[a]==s[b]: c+=1; a-=1; b+=1
    return c

if __name__=="__main__":
    print(count("abc")); print(count("aaa"))
''',
"JavaScript": '''function count(s){let c=0;for(let i=0;i<s.length;i++){for(const [a0,b0] of [[i,i],[i,i+1]]){let a=a0,b=b0;while(a>=0&&b<s.length&&s[a]===s[b]){c++;a--;b++;}}}return c;}
console.log(count("abc"));console.log(count("aaa"));
''',
"Java": '''public class __CLASS__{
  static int count(String s){int c=0;for(int i=0;i<s.length();i++){c+=ex(s,i,i)+ex(s,i,i+1);}return c;}
  static int ex(String s,int a,int b){int c=0;while(a>=0&&b<s.length()&&s.charAt(a)==s.charAt(b)){c++;a--;b++;}return c;}
  public static void main(String[]x){System.out.println(count("abc"));System.out.println(count("aaa"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int ex(string& s,int a,int b){int c=0;while(a>=0&&b<(int)s.size()&&s[a]==s[b]){c++;a--;b++;}return c;}
int count(string s){int c=0;for(int i=0;i<(int)s.size();i++){c+=ex(s,i,i)+ex(s,i,i+1);}return c;}
int main(){cout<<count("abc")<<"\\n"<<count("aaa")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func count(s string) int { c:=0; ex:=func(a,b int){ for a>=0 && b<len(s) && s[a]==s[b] { c++; a--; b++ } }; for i:=0;i<len(s);i++ { ex(i,i); ex(i,i+1) }; return c }
func main(){ fmt.Println(count("abc")); fmt.Println(count("aaa")) }
''',
"R": '''count <- function(s){ n<-nchar(s); c<-0; ex<-function(a,b){ while(a>=1 && b<=n && substr(s,a,a)==substr(s,b,b)){ c<<-c+1; a<-a-1; b<-b+1 } }; for(i in 1:n){ ex(i,i); ex(i,i+1) }; c }
cat(count("abc"),"\\n"); cat(count("aaa"),"\\n")
''',
}))

# 144 Decode Ways
L.append((144, "Decode Ways", "1-D Dynamic Programming", "Medium", 72,
"Number of ways to decode digit string s where '1'->A, ..., '26'->Z.",
{
"Python": '''def ways(s):
    if not s or s[0]=='0': return 0
    n=len(s); dp=[0]*(n+1); dp[0]=dp[1]=1
    for i in range(2,n+1):
        if s[i-1]!='0': dp[i]+=dp[i-1]
        x=int(s[i-2:i])
        if 10<=x<=26: dp[i]+=dp[i-2]
    return dp[n]

if __name__=="__main__":
    print(ways("12")); print(ways("226")); print(ways("06"))
''',
"JavaScript": '''function ways(s){if(!s||s[0]==='0')return 0;const n=s.length;const dp=new Array(n+1).fill(0);dp[0]=1;dp[1]=1;for(let i=2;i<=n;i++){if(s[i-1]!=='0')dp[i]+=dp[i-1];const x=+s.slice(i-2,i);if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
console.log(ways("12"));console.log(ways("226"));console.log(ways("06"));
''',
"Java": '''public class __CLASS__{
  static int ways(String s){if(s==null||s.charAt(0)=='0')return 0;int n=s.length();int[] dp=new int[n+1];dp[0]=1;dp[1]=1;for(int i=2;i<=n;i++){if(s.charAt(i-1)!='0')dp[i]+=dp[i-1];int x=Integer.parseInt(s.substring(i-2,i));if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
  public static void main(String[]x){System.out.println(ways("12"));System.out.println(ways("226"));System.out.println(ways("06"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int ways(string s){if(s.empty()||s[0]=='0')return 0;int n=s.size();vector<int> dp(n+1,0);dp[0]=1;dp[1]=1;for(int i=2;i<=n;i++){if(s[i-1]!='0')dp[i]+=dp[i-1];int x=stoi(s.substr(i-2,2));if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
int main(){cout<<ways("12")<<"\\n"<<ways("226")<<"\\n"<<ways("06")<<"\\n";}
''',
"Go": '''package main
import ("fmt";"strconv")
func ways(s string) int { if s=="" || s[0]=='0' { return 0 }; n:=len(s); dp:=make([]int,n+1); dp[0]=1; dp[1]=1; for i:=2;i<=n;i++ { if s[i-1]!='0' { dp[i]+=dp[i-1] }; x,_:=strconv.Atoi(s[i-2:i]); if x>=10 && x<=26 { dp[i]+=dp[i-2] } }; return dp[n] }
func main(){ fmt.Println(ways("12")); fmt.Println(ways("226")); fmt.Println(ways("06")) }
''',
"R": '''ways <- function(s){ if(nchar(s)==0 || substr(s,1,1)=="0") return(0); n<-nchar(s); dp<-rep(0,n+1); dp[1]<-1; dp[2]<-1; if(n>=2) for(i in 2:n){ if(substr(s,i,i)!="0") dp[i+1]<-dp[i+1]+dp[i]; x<-as.integer(substr(s,i-1,i)); if(x>=10 && x<=26) dp[i+1]<-dp[i+1]+dp[i-1] }; dp[n+1] }
cat(ways("12"),"\\n"); cat(ways("226"),"\\n"); cat(ways("06"),"\\n")
''',
}))

# 145 Construct Quad Tree
L.append((145, "Construct Quad Tree", "Trees", "Medium", 73,
"Given an n x n grid of 0/1, build a quad tree representation. Return root.",
{
"Python": '''class QN:
    def __init__(self,v,leaf,tl=None,tr=None,bl=None,br=None):
        self.val=v; self.isLeaf=leaf; self.tl=tl; self.tr=tr; self.bl=bl; self.br=br
def build(g):
    def rec(r,c,n):
        if all(g[i][j]==g[r][c] for i in range(r,r+n) for j in range(c,c+n)):
            return QN(g[r][c]==1,True)
        h=n//2
        return QN(True,False,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h))
    return rec(0,0,len(g))

def serialize(n):
    if n.isLeaf: return [int(n.val)]
    return ['#']+serialize(n.tl)+serialize(n.tr)+serialize(n.bl)+serialize(n.br)

if __name__=="__main__":
    g=[[0,1],[1,0]]
    print(serialize(build(g)))
''',
"JavaScript": '''class QN{constructor(v,leaf,tl=null,tr=null,bl=null,br=null){this.val=v;this.isLeaf=leaf;this.tl=tl;this.tr=tr;this.bl=bl;this.br=br;}}
function build(g){function rec(r,c,n){let same=true;for(let i=r;i<r+n;i++)for(let j=c;j<c+n;j++)if(g[i][j]!==g[r][c])same=false;if(same)return new QN(g[r][c]===1,true);const h=n/2;return new QN(true,false,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h));}return rec(0,0,g.length);}
function ser(n){if(n.isLeaf)return [+n.val];return ['#',...ser(n.tl),...ser(n.tr),...ser(n.bl),...ser(n.br)];}
console.log(ser(build([[0,1],[1,0]])));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class QN{boolean val,isLeaf;QN tl,tr,bl,br;QN(boolean v,boolean l){val=v;isLeaf=l;}}
  static int[][] G;
  static QN rec(int r,int c,int n){boolean same=true;for(int i=r;i<r+n;i++)for(int j=c;j<c+n;j++)if(G[i][j]!=G[r][c])same=false;if(same)return new QN(G[r][c]==1,true);int h=n/2;QN q=new QN(true,false);q.tl=rec(r,c,h);q.tr=rec(r,c+h,h);q.bl=rec(r+h,c,h);q.br=rec(r+h,c+h,h);return q;}
  static List<String> ser(QN n){List<String> r=new ArrayList<>();if(n.isLeaf){r.add(n.val?"1":"0");return r;}r.add("#");r.addAll(ser(n.tl));r.addAll(ser(n.tr));r.addAll(ser(n.bl));r.addAll(ser(n.br));return r;}
  public static void main(String[]x){G=new int[][]{{0,1},{1,0}};QN root=rec(0,0,2);System.out.println(ser(root));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct QN{bool val,isLeaf;QN *tl=nullptr,*tr=nullptr,*bl=nullptr,*br=nullptr;QN(bool v,bool l):val(v),isLeaf(l){}};
vector<vector<int>> G;
QN* rec(int r,int c,int n){bool same=true;for(int i=r;i<r+n;i++)for(int j=c;j<c+n;j++)if(G[i][j]!=G[r][c])same=false;if(same)return new QN(G[r][c]==1,true);int h=n/2;QN* q=new QN(true,false);q->tl=rec(r,c,h);q->tr=rec(r,c+h,h);q->bl=rec(r+h,c,h);q->br=rec(r+h,c+h,h);return q;}
void ser(QN* n,vector<string>& out){if(n->isLeaf){out.push_back(n->val?"1":"0");return;}out.push_back("#");ser(n->tl,out);ser(n->tr,out);ser(n->bl,out);ser(n->br,out);}
int main(){G={{0,1},{1,0}};auto r=rec(0,0,2);vector<string> o;ser(r,o);for(auto&s:o)cout<<s<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type QN struct{ Val,IsLeaf bool; TL,TR,BL,BR *QN }
var G [][]int
func rec(r,c,n int) *QN { same:=true; for i:=r;i<r+n;i++ { for j:=c;j<c+n;j++ { if G[i][j]!=G[r][c] { same=false } } }; if same { return &QN{G[r][c]==1,true,nil,nil,nil,nil} }; h:=n/2; return &QN{true,false,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h)} }
func ser(n *QN) []string { if n.IsLeaf { if n.Val { return []string{"1"} }; return []string{"0"} }; r:=[]string{"#"}; r=append(r,ser(n.TL)...); r=append(r,ser(n.TR)...); r=append(r,ser(n.BL)...); r=append(r,ser(n.BR)...); return r }
func main(){ G=[][]int{{0,1},{1,0}}; fmt.Println(ser(rec(0,0,2))) }
''',
"R": '''build <- function(g){ rec <- function(r,c,n){ sub<-g[r:(r+n-1),c:(c+n-1),drop=FALSE]; if(length(unique(as.vector(sub)))==1) return(list(val=g[r,c],leaf=TRUE)); h<-n/2; list(leaf=FALSE,tl=rec(r,c,h),tr=rec(r,c+h,h),bl=rec(r+h,c,h),br=rec(r+h,c+h,h)) }; rec(1,1,nrow(g)) }
ser <- function(n){ if(isTRUE(n$leaf)) return(as.character(n$val)); c("#",ser(n$tl),ser(n$tr),ser(n$bl),ser(n$br)) }
print(ser(build(matrix(c(0,1,1,0),2,2,byrow=TRUE))))
''',
}))

# 146 Count Good Nodes
L.append((146, "Count Good Nodes In Binary Tree", "Trees", "Medium", 73,
"A node is good if no node on the root-to-node path has a value greater. Count good nodes.",
{
"Python": '''class TN:
    def __init__(self,v,l=None,r=None): self.val=v; self.left=l; self.right=r
def good(root):
    def rec(n,m):
        if not n: return 0
        c=1 if n.val>=m else 0
        m=max(m,n.val)
        return c+rec(n.left,m)+rec(n.right,m)
    return rec(root,float('-inf'))

if __name__=="__main__":
    r=TN(3,TN(1,TN(3)),TN(4,TN(1),TN(5)))
    print(good(r))
''',
"JavaScript": '''class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function good(root){function rec(n,m){if(!n)return 0;const c=n.val>=m?1:0;return c+rec(n.left,Math.max(m,n.val))+rec(n.right,Math.max(m,n.val));}return rec(root,-Infinity);}
const r=new TN(3,new TN(1,new TN(3)),new TN(4,new TN(1),new TN(5)));
console.log(good(r));
''',
"Java": '''public class __CLASS__{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static int rec(TN n,int m){if(n==null)return 0;int c=n.val>=m?1:0;int nm=Math.max(m,n.val);return c+rec(n.left,nm)+rec(n.right,nm);}
  static int good(TN r){return rec(r,Integer.MIN_VALUE);}
  public static void main(String[]x){TN r=new TN(3,new TN(1,new TN(3,null,null),null),new TN(4,new TN(1,null,null),new TN(5,null,null)));System.out.println(good(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct TN{int val;TN*l;TN*r;TN(int v,TN*a=nullptr,TN*b=nullptr):val(v),l(a),r(b){}};
int rec(TN* n,int m){if(!n)return 0;int c=n->val>=m?1:0;int nm=max(m,n->val);return c+rec(n->l,nm)+rec(n->r,nm);}
int good(TN* r){return rec(r,INT_MIN);}
int main(){TN n3a(3),n1a(1,&n3a,nullptr),n1b(1),n5(5),n4(4,&n1b,&n5),root(3,&n1a,&n4);cout<<good(&root)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func good(root *TN) int { var rec func(n *TN,m int) int; rec=func(n *TN,m int) int { if n==nil { return 0 }; c:=0; if n.Val>=m { c=1 }; nm:=m; if n.Val>nm { nm=n.Val }; return c+rec(n.L,nm)+rec(n.R,nm) }; return rec(root,-1<<31) }
func main(){ r:=&TN{3,&TN{1,&TN{3,nil,nil},nil},&TN{4,&TN{1,nil,nil},&TN{5,nil,nil}}}; fmt.Println(good(r)) }
''',
"R": '''good <- function(root){ rec<-function(n,m){ if(is.null(n)) return(0); c<-if(n$val>=m) 1 else 0; nm<-max(m,n$val); c+rec(n$l,nm)+rec(n$r,nm) }; rec(root,-Inf) }
TN <- function(v,l=NULL,r=NULL) list(val=v,l=l,r=r)
cat(good(TN(3,TN(1,TN(3)),TN(4,TN(1),TN(5)))),"\\n")
''',
}))

# 147 Last Stone Weight II
L.append((147, "Last Stone Weight II", "2-D Dynamic Programming", "Medium", 74,
"Given stones, smash to minimize remaining weight (subset partition).",
{
"Python": '''def lsw2(s):
    t=sum(s); cap=t//2
    dp=[False]*(cap+1); dp[0]=True
    for x in s:
        for j in range(cap,x-1,-1): dp[j]=dp[j] or dp[j-x]
    for j in range(cap,-1,-1):
        if dp[j]: return t-2*j

if __name__=="__main__":
    print(lsw2([2,7,4,1,8,1])); print(lsw2([31,26,33,21,40]))
''',
"JavaScript": '''function lsw2(s){const t=s.reduce((a,b)=>a+b,0),cap=Math.floor(t/2);const dp=new Array(cap+1).fill(false);dp[0]=true;for(const x of s)for(let j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(let j=cap;j>=0;j--)if(dp[j])return t-2*j;}
console.log(lsw2([2,7,4,1,8,1]));console.log(lsw2([31,26,33,21,40]));
''',
"Java": '''public class __CLASS__{
  static int lsw2(int[]s){int t=0;for(int x:s)t+=x;int cap=t/2;boolean[] dp=new boolean[cap+1];dp[0]=true;for(int x:s)for(int j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(int j=cap;j>=0;j--)if(dp[j])return t-2*j;return 0;}
  public static void main(String[]x){System.out.println(lsw2(new int[]{2,7,4,1,8,1}));System.out.println(lsw2(new int[]{31,26,33,21,40}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int lsw2(vector<int> s){int t=accumulate(s.begin(),s.end(),0);int cap=t/2;vector<int> dp(cap+1,0);dp[0]=1;for(int x:s)for(int j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(int j=cap;j>=0;j--)if(dp[j])return t-2*j;return 0;}
int main(){cout<<lsw2({2,7,4,1,8,1})<<"\\n"<<lsw2({31,26,33,21,40})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func lsw2(s []int) int { t:=0; for _,x:=range s { t+=x }; cap:=t/2; dp:=make([]bool,cap+1); dp[0]=true; for _,x:=range s { for j:=cap;j>=x;j-- { if dp[j-x] { dp[j]=true } } }; for j:=cap;j>=0;j-- { if dp[j] { return t-2*j } }; return 0 }
func main(){ fmt.Println(lsw2([]int{2,7,4,1,8,1})); fmt.Println(lsw2([]int{31,26,33,21,40})) }
''',
"R": '''lsw2 <- function(s){ t<-sum(s); cap<-t %/% 2; dp<-rep(FALSE,cap+1); dp[1]<-TRUE; for(x in s) for(j in (cap+1):(x+1)) if(j-x>=1 && dp[j-x]) dp[j]<-TRUE; for(j in (cap+1):1) if(dp[j]) return(t-2*(j-1)); 0 }
cat(lsw2(c(2,7,4,1,8,1)),"\\n"); cat(lsw2(c(31,26,33,21,40)),"\\n")
''',
}))

# 148 BTBSWC
L.append((148, "Best Time to Buy And Sell Stock With Cooldown", "2-D Dynamic Programming", "Medium", 74,
"Stock prices; can do unlimited transactions but after selling must cooldown 1 day. Max profit.",
{
"Python": '''def maxP(p):
    hold=-p[0]; sold=0; rest=0
    for i in range(1,len(p)):
        h=max(hold,rest-p[i])
        s=hold+p[i]
        r=max(rest,sold)
        hold,sold,rest=h,s,r
    return max(sold,rest)

if __name__=="__main__":
    print(maxP([1,2,3,0,2]))
''',
"JavaScript": '''function maxP(p){let hold=-p[0],sold=0,rest=0;for(let i=1;i<p.length;i++){const h=Math.max(hold,rest-p[i]);const s=hold+p[i];const r=Math.max(rest,sold);hold=h;sold=s;rest=r;}return Math.max(sold,rest);}
console.log(maxP([1,2,3,0,2]));
''',
"Java": '''public class __CLASS__{
  static int maxP(int[]p){int hold=-p[0],sold=0,rest=0;for(int i=1;i<p.length;i++){int h=Math.max(hold,rest-p[i]);int s=hold+p[i];int r=Math.max(rest,sold);hold=h;sold=s;rest=r;}return Math.max(sold,rest);}
  public static void main(String[]x){System.out.println(maxP(new int[]{1,2,3,0,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxP(vector<int>&p){int hold=-p[0],sold=0,rest=0;for(int i=1;i<(int)p.size();i++){int h=max(hold,rest-p[i]);int s=hold+p[i];int r=max(rest,sold);hold=h;sold=s;rest=r;}return max(sold,rest);}
int main(){vector<int> v={1,2,3,0,2};cout<<maxP(v)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxP(p []int) int { hold:=-p[0]; sold:=0; rest:=0; for i:=1;i<len(p);i++ { h:=hold; if rest-p[i]>h { h=rest-p[i] }; s:=hold+p[i]; r:=rest; if sold>r { r=sold }; hold=h; sold=s; rest=r }; if sold>rest { return sold }; return rest }
func main(){ fmt.Println(maxP([]int{1,2,3,0,2})) }
''',
"R": '''maxP <- function(p){ hold<- -p[1]; sold<-0; rest<-0; for(i in 2:length(p)){ h<-max(hold,rest-p[i]); s<-hold+p[i]; r<-max(rest,sold); hold<-h; sold<-s; rest<-r }; max(sold,rest) }
cat(maxP(c(1,2,3,0,2)),"\\n")
''',
}))

# 149 Daily Temperatures
L.append((149, "Daily Temperatures", "Stack", "Medium", 75,
"For each day, return number of days until a warmer temperature, or 0.",
{
"Python": '''def dailyT(t):
    res=[0]*len(t); st=[]
    for i,x in enumerate(t):
        while st and t[st[-1]]<x:
            j=st.pop(); res[j]=i-j
        st.append(i)
    return res

if __name__=="__main__":
    print(dailyT([73,74,75,71,69,72,76,73]))
''',
"JavaScript": '''function dailyT(t){const r=new Array(t.length).fill(0);const st=[];for(let i=0;i<t.length;i++){while(st.length&&t[st[st.length-1]]<t[i]){const j=st.pop();r[j]=i-j;}st.push(i);}return r;}
console.log(dailyT([73,74,75,71,69,72,76,73]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] dailyT(int[]t){int[] r=new int[t.length];Deque<Integer> st=new ArrayDeque<>();for(int i=0;i<t.length;i++){while(!st.isEmpty()&&t[st.peek()]<t[i]){int j=st.pop();r[j]=i-j;}st.push(i);}return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(dailyT(new int[]{73,74,75,71,69,72,76,73})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> dailyT(vector<int> t){vector<int> r(t.size(),0);stack<int> st;for(int i=0;i<(int)t.size();i++){while(!st.empty()&&t[st.top()]<t[i]){int j=st.top();st.pop();r[j]=i-j;}st.push(i);}return r;}
int main(){auto v=dailyT({73,74,75,71,69,72,76,73});for(int x:v)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func dailyT(t []int) []int { r:=make([]int,len(t)); var st []int; for i,x:=range t { for len(st)>0 && t[st[len(st)-1]]<x { j:=st[len(st)-1]; st=st[:len(st)-1]; r[j]=i-j }; st=append(st,i) }; return r }
func main(){ fmt.Println(dailyT([]int{73,74,75,71,69,72,76,73})) }
''',
"R": '''dailyT <- function(t){ r<-rep(0,length(t)); st<-c(); for(i in seq_along(t)){ while(length(st)>0 && t[st[length(st)]]<t[i]){ j<-st[length(st)]; st<-st[-length(st)]; r[j]<-i-j }; st<-c(st,i) }; r }
print(dailyT(c(73,74,75,71,69,72,76,73)))
''',
}))

# 150 Online Stock Span
L.append((150, "Online Stock Span", "Stack", "Medium", 75,
"Implement StockSpanner.next(price): consecutive days <= today's price (including today).",
{
"Python": '''class StockSpanner:
    def __init__(self): self.st=[]
    def next(self,p):
        s=1
        while self.st and self.st[-1][0]<=p: _,k=self.st.pop(); s+=k
        self.st.append((p,s)); return s

if __name__=="__main__":
    s=StockSpanner()
    print([s.next(x) for x in [100,80,60,70,60,75,85]])
''',
"JavaScript": '''class StockSpanner{constructor(){this.st=[];}next(p){let s=1;while(this.st.length&&this.st[this.st.length-1][0]<=p)s+=this.st.pop()[1];this.st.push([p,s]);return s;}}
const s=new StockSpanner();
console.log([100,80,60,70,60,75,85].map(x=>s.next(x)));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class StockSpanner{Deque<int[]> st=new ArrayDeque<>();int next(int p){int s=1;while(!st.isEmpty()&&st.peek()[0]<=p)s+=st.pop()[1];st.push(new int[]{p,s});return s;}}
  public static void main(String[]x){StockSpanner s=new StockSpanner();int[] arr={100,80,60,70,60,75,85};StringBuilder sb=new StringBuilder("[");for(int v:arr){sb.append(s.next(v)).append(" ");}sb.append("]");System.out.println(sb);}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct StockSpanner{vector<pair<int,int>> st; int next(int p){int s=1;while(!st.empty()&&st.back().first<=p){s+=st.back().second;st.pop_back();}st.push_back({p,s});return s;}};
int main(){StockSpanner s;for(int v:{100,80,60,70,60,75,85})cout<<s.next(v)<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type Pr struct{ P,S int }
type StockSpanner struct{ st []Pr }
func (s *StockSpanner) Next(p int) int { v:=1; for len(s.st)>0 && s.st[len(s.st)-1].P<=p { v+=s.st[len(s.st)-1].S; s.st=s.st[:len(s.st)-1] }; s.st=append(s.st,Pr{p,v}); return v }
func main(){ s:=&StockSpanner{}; for _,v:=range []int{100,80,60,70,60,75,85} { fmt.Print(s.Next(v)," ") }; fmt.Println() }
''',
"R": '''StockSpanner <- function(){ st<-list(); next_ <- function(p){ s<-1; while(length(st)>0 && st[[length(st)]][1]<=p){ s<-s+st[[length(st)]][2]; st[[length(st)]]<<-NULL }; st[[length(st)+1]]<<-c(p,s); s }; list(next_=next_) }
s<-StockSpanner(); print(sapply(c(100,80,60,70,60,75,85),s$next_))
''',
}))

# 151 Add Two Numbers (linked list)
L.append((151, "Add Two Numbers", "Linked List", "Medium", 76,
"Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.",
{
"Python": '''class LN:
    def __init__(self,v,n=None): self.val=v; self.next=n
def add(a,b):
    d=LN(0); cur=d; c=0
    while a or b or c:
        v=c+(a.val if a else 0)+(b.val if b else 0)
        c,v=divmod(v,10)
        cur.next=LN(v); cur=cur.next
        a=a.next if a else None; b=b.next if b else None
    return d.next

def to_list(n):
    o=[]
    while n: o.append(n.val); n=n.next
    return o
def from_list(a):
    d=LN(0); cur=d
    for x in a: cur.next=LN(x); cur=cur.next
    return d.next

if __name__=="__main__":
    print(to_list(add(from_list([2,4,3]),from_list([5,6,4]))))
''',
"JavaScript": '''class LN{constructor(v,n=null){this.val=v;this.next=n;}}
function add(a,b){const d=new LN(0);let cur=d,c=0;while(a||b||c){let v=c+(a?a.val:0)+(b?b.val:0);c=Math.floor(v/10);v%=10;cur.next=new LN(v);cur=cur.next;a=a?a.next:null;b=b?b.next:null;}return d.next;}
function fromArr(a){const d=new LN(0);let c=d;for(const x of a){c.next=new LN(x);c=c.next;}return d.next;}
function toArr(n){const r=[];while(n){r.push(n.val);n=n.next;}return r;}
console.log(toArr(add(fromArr([2,4,3]),fromArr([5,6,4]))));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class LN{int val;LN next;LN(int v){val=v;}}
  static LN add(LN a,LN b){LN d=new LN(0);LN cur=d;int c=0;while(a!=null||b!=null||c!=0){int v=c+(a!=null?a.val:0)+(b!=null?b.val:0);c=v/10;cur.next=new LN(v%10);cur=cur.next;if(a!=null)a=a.next;if(b!=null)b=b.next;}return d.next;}
  static LN fromArr(int[]x){LN d=new LN(0);LN c=d;for(int v:x){c.next=new LN(v);c=c.next;}return d.next;}
  static List<Integer> toList(LN n){List<Integer> r=new ArrayList<>();while(n!=null){r.add(n.val);n=n.next;}return r;}
  public static void main(String[]x){System.out.println(toList(add(fromArr(new int[]{2,4,3}),fromArr(new int[]{5,6,4}))));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct LN{int val;LN* next;LN(int v):val(v),next(nullptr){}};
LN* add(LN* a,LN* b){LN* d=new LN(0);LN* cur=d;int c=0;while(a||b||c){int v=c+(a?a->val:0)+(b?b->val:0);c=v/10;cur->next=new LN(v%10);cur=cur->next;if(a)a=a->next;if(b)b=b->next;}return d->next;}
LN* fromArr(vector<int> x){LN* d=new LN(0);LN* c=d;for(int v:x){c->next=new LN(v);c=c->next;}return d->next;}
int main(){auto r=add(fromArr({2,4,3}),fromArr({5,6,4}));while(r){cout<<r->val<<" ";r=r->next;}cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type LN struct{ Val int; Next *LN }
func add(a,b *LN) *LN { d:=&LN{}; cur:=d; c:=0; for a!=nil || b!=nil || c!=0 { v:=c; if a!=nil { v+=a.Val; a=a.Next }; if b!=nil { v+=b.Val; b=b.Next }; c=v/10; cur.Next=&LN{Val:v%10}; cur=cur.Next }; return d.Next }
func fromArr(x []int) *LN { d:=&LN{}; c:=d; for _,v:=range x { c.Next=&LN{Val:v}; c=c.Next }; return d.Next }
func main(){ r:=add(fromArr([]int{2,4,3}),fromArr([]int{5,6,4})); for r!=nil { fmt.Print(r.Val," "); r=r.Next }; fmt.Println() }
''',
"R": '''add <- function(a,b){ res<-c(); c<-0; i<-1; while(i<=max(length(a),length(b)) || c>0){ v<-c+if(i<=length(a)) a[i] else 0+if(i<=length(b)) b[i] else 0; res<-c(res,v%%10); c<-v%/%10; i<-i+1 }; res }
print(add(c(2,4,3),c(5,6,4)))
''',
}))

# 152 Find The Duplicate Number
L.append((152, "Find The Duplicate Number", "Linked List", "Medium", 76,
"Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.",
{
"Python": '''def dup(a):
    s=f=a[0]
    while True:
        s=a[s]; f=a[a[f]]
        if s==f: break
    s=a[0]
    while s!=f: s=a[s]; f=a[f]
    return s

if __name__=="__main__":
    print(dup([1,3,4,2,2])); print(dup([3,1,3,4,2]))
''',
"JavaScript": '''function dup(a){let s=a[0],f=a[0];do{s=a[s];f=a[a[f]];}while(s!==f);s=a[0];while(s!==f){s=a[s];f=a[f];}return s;}
console.log(dup([1,3,4,2,2]));console.log(dup([3,1,3,4,2]));
''',
"Java": '''public class __CLASS__{
  static int dup(int[]a){int s=a[0],f=a[0];do{s=a[s];f=a[a[f]];}while(s!=f);s=a[0];while(s!=f){s=a[s];f=a[f];}return s;}
  public static void main(String[]x){System.out.println(dup(new int[]{1,3,4,2,2}));System.out.println(dup(new int[]{3,1,3,4,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int dup(vector<int> a){int s=a[0],f=a[0];do{s=a[s];f=a[a[f]];}while(s!=f);s=a[0];while(s!=f){s=a[s];f=a[f];}return s;}
int main(){cout<<dup({1,3,4,2,2})<<"\\n"<<dup({3,1,3,4,2})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func dup(a []int) int { s:=a[0]; f:=a[0]; for { s=a[s]; f=a[a[f]]; if s==f { break } }; s=a[0]; for s!=f { s=a[s]; f=a[f] }; return s }
func main(){ fmt.Println(dup([]int{1,3,4,2,2})); fmt.Println(dup([]int{3,1,3,4,2})) }
''',
"R": '''dup <- function(a){ s<-a[1]; f<-a[1]; repeat { s<-a[s+1]; f<-a[a[f+1]+1]; if(s==f) break }; s<-a[1]; while(s!=f){ s<-a[s+1]; f<-a[f+1] }; s }
cat(dup(c(1,3,4,2,2)),"\\n"); cat(dup(c(3,1,3,4,2)),"\\n")
''',
}))

# 153 Walls and Gates
L.append((153, "Walls And Gates", "Graphs", "Medium", 77,
"Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.",
{
"Python": '''from collections import deque
INF=2**31-1
def walls(g):
    if not g: return g
    m,n=len(g),len(g[0]); q=deque()
    for i in range(m):
        for j in range(n):
            if g[i][j]==0: q.append((i,j))
    while q:
        i,j=q.popleft()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<m and 0<=nj<n and g[ni][nj]==INF:
                g[ni][nj]=g[i][j]+1; q.append((ni,nj))
    return g

if __name__=="__main__":
    g=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    print(walls(g))
''',
"JavaScript": '''const INF=2**31-1;
function walls(g){if(!g.length)return g;const m=g.length,n=g[0].length;const q=[];for(let i=0;i<m;i++)for(let j=0;j<n;j++)if(g[i][j]===0)q.push([i,j]);while(q.length){const [i,j]=q.shift();for(const [di,dj] of [[-1,0],[1,0],[0,-1],[0,1]]){const ni=i+di,nj=j+dj;if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]===INF){g[ni][nj]=g[i][j]+1;q.push([ni,nj]);}}}return g;}
const g=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]];
console.log(walls(g));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static final int INF=Integer.MAX_VALUE;
  static int[][] walls(int[][]g){if(g.length==0)return g;int m=g.length,n=g[0].length;Queue<int[]> q=new ArrayDeque<>();for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(g[i][j]==0)q.add(new int[]{i,j});int[][] D={{-1,0},{1,0},{0,-1},{0,1}};while(!q.isEmpty()){int[] p=q.poll();for(int[] d:D){int ni=p[0]+d[0],nj=p[1]+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==INF){g[ni][nj]=g[p[0]][p[1]]+1;q.add(new int[]{ni,nj});}}}return g;}
  public static void main(String[]x){int[][] g={{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}};System.out.println(Arrays.deepToString(walls(g)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
const int INF=INT_MAX;
vector<vector<int>> walls(vector<vector<int>> g){if(g.empty())return g;int m=g.size(),n=g[0].size();queue<pair<int,int>> q;for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(g[i][j]==0)q.push({i,j});int D[4][2]={{-1,0},{1,0},{0,-1},{0,1}};while(!q.empty()){auto [i,j]=q.front();q.pop();for(auto& d:D){int ni=i+d[0],nj=j+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==INF){g[ni][nj]=g[i][j]+1;q.push({ni,nj});}}}return g;}
int main(){auto r=walls({{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}});for(auto&row:r){for(int x:row)cout<<(x==INF?-9:x)<<" ";cout<<"\\n";}}
''',
"Go": '''package main
import "fmt"
const INF = 2147483647
func walls(g [][]int) [][]int { if len(g)==0 { return g }; m,n:=len(g),len(g[0]); var q [][2]int; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==0 { q=append(q,[2]int{i,j}) } } }; D:=[4][2]int{{-1,0},{1,0},{0,-1},{0,1}}; for len(q)>0 { p:=q[0]; q=q[1:]; for _,d:=range D { ni,nj:=p[0]+d[0],p[1]+d[1]; if ni>=0 && nj>=0 && ni<m && nj<n && g[ni][nj]==INF { g[ni][nj]=g[p[0]][p[1]]+1; q=append(q,[2]int{ni,nj}) } } }; return g }
func main(){ g:=[][]int{{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}}; fmt.Println(walls(g)) }
''',
"R": '''INF <- 2^31-1
walls <- function(g){ m<-nrow(g); n<-ncol(g); q<-list(); for(i in 1:m) for(j in 1:n) if(g[i,j]==0) q[[length(q)+1]]<-c(i,j); D<-list(c(-1,0),c(1,0),c(0,-1),c(0,1)); while(length(q)>0){ p<-q[[1]]; q<-q[-1]; for(d in D){ ni<-p[1]+d[1]; nj<-p[2]+d[2]; if(ni>=1 && nj>=1 && ni<=m && nj<=n && g[ni,nj]==INF){ g[ni,nj]<-g[p[1],p[2]]+1; q[[length(q)+1]]<-c(ni,nj) } } }; g }
g<-matrix(c(INF,-1,0,INF,INF,INF,INF,-1,INF,-1,INF,-1,0,-1,INF,INF),4,4,byrow=TRUE); print(walls(g))
''',
}))

# 154 Rotting Oranges
L.append((154, "Rotting Oranges", "Graphs", "Medium", 77,
"0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.",
{
"Python": '''from collections import deque
def rot(g):
    m,n=len(g),len(g[0]); q=deque(); fresh=0
    for i in range(m):
        for j in range(n):
            if g[i][j]==2: q.append((i,j,0))
            elif g[i][j]==1: fresh+=1
    t=0
    while q:
        i,j,k=q.popleft(); t=k
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<m and 0<=nj<n and g[ni][nj]==1:
                g[ni][nj]=2; fresh-=1; q.append((ni,nj,k+1))
    return -1 if fresh else t

if __name__=="__main__":
    print(rot([[2,1,1],[1,1,0],[0,1,1]]))
    print(rot([[2,1,1],[0,1,1],[1,0,1]]))
''',
"JavaScript": '''function rot(g){const m=g.length,n=g[0].length;const q=[];let fresh=0;for(let i=0;i<m;i++)for(let j=0;j<n;j++){if(g[i][j]===2)q.push([i,j,0]);else if(g[i][j]===1)fresh++;}let t=0;while(q.length){const [i,j,k]=q.shift();t=k;for(const [di,dj] of [[-1,0],[1,0],[0,-1],[0,1]]){const ni=i+di,nj=j+dj;if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]===1){g[ni][nj]=2;fresh--;q.push([ni,nj,k+1]);}}}return fresh?-1:t;}
console.log(rot([[2,1,1],[1,1,0],[0,1,1]]));console.log(rot([[2,1,1],[0,1,1],[1,0,1]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int rot(int[][]g){int m=g.length,n=g[0].length;Queue<int[]> q=new ArrayDeque<>();int fresh=0;for(int i=0;i<m;i++)for(int j=0;j<n;j++){if(g[i][j]==2)q.add(new int[]{i,j,0});else if(g[i][j]==1)fresh++;}int t=0;int[][] D={{-1,0},{1,0},{0,-1},{0,1}};while(!q.isEmpty()){int[] p=q.poll();t=p[2];for(int[] d:D){int ni=p[0]+d[0],nj=p[1]+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==1){g[ni][nj]=2;fresh--;q.add(new int[]{ni,nj,p[2]+1});}}}return fresh>0?-1:t;}
  public static void main(String[]x){System.out.println(rot(new int[][]{{2,1,1},{1,1,0},{0,1,1}}));System.out.println(rot(new int[][]{{2,1,1},{0,1,1},{1,0,1}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int rot(vector<vector<int>> g){int m=g.size(),n=g[0].size();queue<tuple<int,int,int>> q;int fresh=0;for(int i=0;i<m;i++)for(int j=0;j<n;j++){if(g[i][j]==2)q.push({i,j,0});else if(g[i][j]==1)fresh++;}int t=0,D[4][2]={{-1,0},{1,0},{0,-1},{0,1}};while(!q.empty()){auto [i,j,k]=q.front();q.pop();t=k;for(auto& d:D){int ni=i+d[0],nj=j+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==1){g[ni][nj]=2;fresh--;q.push({ni,nj,k+1});}}}return fresh?-1:t;}
int main(){cout<<rot({{2,1,1},{1,1,0},{0,1,1}})<<"\\n"<<rot({{2,1,1},{0,1,1},{1,0,1}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func rot(g [][]int) int { m,n:=len(g),len(g[0]); var q [][3]int; fresh:=0; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==2 { q=append(q,[3]int{i,j,0}) } else if g[i][j]==1 { fresh++ } } }; t:=0; D:=[4][2]int{{-1,0},{1,0},{0,-1},{0,1}}; for len(q)>0 { p:=q[0]; q=q[1:]; t=p[2]; for _,d:=range D { ni,nj:=p[0]+d[0],p[1]+d[1]; if ni>=0 && nj>=0 && ni<m && nj<n && g[ni][nj]==1 { g[ni][nj]=2; fresh--; q=append(q,[3]int{ni,nj,p[2]+1}) } } }; if fresh>0 { return -1 }; return t }
func main(){ fmt.Println(rot([][]int{{2,1,1},{1,1,0},{0,1,1}})); fmt.Println(rot([][]int{{2,1,1},{0,1,1},{1,0,1}})) }
''',
"R": '''rot <- function(g){ m<-nrow(g); n<-ncol(g); q<-list(); fresh<-0; for(i in 1:m) for(j in 1:n){ if(g[i,j]==2) q[[length(q)+1]]<-c(i,j,0) else if(g[i,j]==1) fresh<-fresh+1 }; t<-0; D<-list(c(-1,0),c(1,0),c(0,-1),c(0,1)); while(length(q)>0){ p<-q[[1]]; q<-q[-1]; t<-p[3]; for(d in D){ ni<-p[1]+d[1]; nj<-p[2]+d[2]; if(ni>=1 && nj>=1 && ni<=m && nj<=n && g[ni,nj]==1){ g[ni,nj]<-2; fresh<-fresh-1; q[[length(q)+1]]<-c(ni,nj,p[3]+1) } } }; if(fresh>0) -1 else t }
cat(rot(matrix(c(2,1,1,1,1,0,0,1,1),3,3,byrow=TRUE)),"\\n"); cat(rot(matrix(c(2,1,1,0,1,1,1,0,1),3,3,byrow=TRUE)),"\\n")
''',
}))

# 155 Build Matrix With Conditions
L.append((155, "Build a Matrix With Conditions", "Advanced Graphs", "Hard", 78,
"Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].",
{
"Python": '''from collections import defaultdict, deque
def topo(k, conds):
    adj=defaultdict(list); ind=[0]*(k+1)
    for a,b in conds:
        adj[a].append(b); ind[b]+=1
    q=deque([i for i in range(1,k+1) if ind[i]==0]); o=[]
    while q:
        x=q.popleft(); o.append(x)
        for y in adj[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return o if len(o)==k else []
def build(k, rowC, colC):
    r=topo(k,rowC); c=topo(k,colC)
    if not r or not c: return []
    pos={v:i for i,v in enumerate(c)}
    g=[[0]*k for _ in range(k)]
    for i,v in enumerate(r): g[i][pos[v]]=v
    return g

if __name__=="__main__":
    print(build(3,[[1,2],[3,2]],[[2,1],[3,2]]))
''',
"JavaScript": '''function topo(k,conds){const adj=Array.from({length:k+1},()=>[]);const ind=new Array(k+1).fill(0);for(const [a,b] of conds){adj[a].push(b);ind[b]++;}const q=[];for(let i=1;i<=k;i++)if(ind[i]===0)q.push(i);const o=[];while(q.length){const x=q.shift();o.push(x);for(const y of adj[x]){if(--ind[y]===0)q.push(y);}}return o.length===k?o:[];}
function build(k,rC,cC){const r=topo(k,rC),c=topo(k,cC);if(!r.length||!c.length)return [];const pos={};c.forEach((v,i)=>pos[v]=i);const g=Array.from({length:k},()=>new Array(k).fill(0));r.forEach((v,i)=>g[i][pos[v]]=v);return g;}
console.log(build(3,[[1,2],[3,2]],[[2,1],[3,2]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] topo(int k,int[][] conds){List<List<Integer>> adj=new ArrayList<>();for(int i=0;i<=k;i++)adj.add(new ArrayList<>());int[] ind=new int[k+1];for(int[] c:conds){adj.get(c[0]).add(c[1]);ind[c[1]]++;}Queue<Integer> q=new ArrayDeque<>();for(int i=1;i<=k;i++)if(ind[i]==0)q.add(i);int[] o=new int[k];int idx=0;while(!q.isEmpty()){int x=q.poll();o[idx++]=x;for(int y:adj.get(x))if(--ind[y]==0)q.add(y);}return idx==k?o:new int[0];}
  static int[][] build(int k,int[][] rC,int[][] cC){int[] r=topo(k,rC),c=topo(k,cC);if(r.length==0||c.length==0)return new int[0][0];int[] pos=new int[k+1];for(int i=0;i<k;i++)pos[c[i]]=i;int[][] g=new int[k][k];for(int i=0;i<k;i++)g[i][pos[r[i]]]=r[i];return g;}
  public static void main(String[]x){System.out.println(Arrays.deepToString(build(3,new int[][]{{1,2},{3,2}},new int[][]{{2,1},{3,2}})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> topo(int k,vector<vector<int>> conds){vector<vector<int>> adj(k+1);vector<int> ind(k+1,0);for(auto& c:conds){adj[c[0]].push_back(c[1]);ind[c[1]]++;}queue<int> q;for(int i=1;i<=k;i++)if(ind[i]==0)q.push(i);vector<int> o;while(!q.empty()){int x=q.front();q.pop();o.push_back(x);for(int y:adj[x])if(--ind[y]==0)q.push(y);}return (int)o.size()==k?o:vector<int>{};}
vector<vector<int>> build(int k,vector<vector<int>> rC,vector<vector<int>> cC){auto r=topo(k,rC),c=topo(k,cC);if(r.empty()||c.empty())return {};vector<int> pos(k+1);for(int i=0;i<k;i++)pos[c[i]]=i;vector<vector<int>> g(k,vector<int>(k,0));for(int i=0;i<k;i++)g[i][pos[r[i]]]=r[i];return g;}
int main(){auto m=build(3,{{1,2},{3,2}},{{2,1},{3,2}});for(auto&r:m){for(int x:r)cout<<x<<" ";cout<<"\\n";}}
''',
"Go": '''package main
import "fmt"
func topo(k int, conds [][]int) []int { adj:=make([][]int,k+1); ind:=make([]int,k+1); for _,c:=range conds { adj[c[0]]=append(adj[c[0]],c[1]); ind[c[1]]++ }; var q []int; for i:=1;i<=k;i++ { if ind[i]==0 { q=append(q,i) } }; var o []int; for len(q)>0 { x:=q[0]; q=q[1:]; o=append(o,x); for _,y:=range adj[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; if len(o)==k { return o }; return nil }
func build(k int, rC,cC [][]int) [][]int { r,c:=topo(k,rC),topo(k,cC); if r==nil || c==nil { return nil }; pos:=make([]int,k+1); for i,v:=range c { pos[v]=i }; g:=make([][]int,k); for i:=range g { g[i]=make([]int,k) }; for i,v:=range r { g[i][pos[v]]=v }; return g }
func main(){ fmt.Println(build(3,[][]int{{1,2},{3,2}},[][]int{{2,1},{3,2}})) }
''',
"R": '''topo <- function(k,conds){ adj<-vector("list",k); ind<-rep(0,k); for(c in conds){ adj[[c[1]]]<-c(adj[[c[1]]],c[2]); ind[c[2]]<-ind[c[2]]+1 }; q<-which(ind==0); o<-c(); while(length(q)>0){ x<-q[1]; q<-q[-1]; o<-c(o,x); for(y in adj[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; if(length(o)==k) o else c() }
build <- function(k,rC,cC){ r<-topo(k,rC); c<-topo(k,cC); if(length(r)==0 || length(c)==0) return(matrix(0,0,0)); pos<-rep(0,k); for(i in seq_along(c)) pos[c[i]]<-i; g<-matrix(0,k,k); for(i in seq_along(r)) g[i,pos[r[i]]]<-r[i]; g }
print(build(3,list(c(1,2),c(3,2)),list(c(2,1),c(3,2))))
''',
}))

# 156 Greatest Common Divisor Traversal
L.append((156, "Greatest Common Divisor Traversal", "Advanced Graphs", "Hard", 78,
"You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.",
{
"Python": '''from math import gcd
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
''',
"JavaScript": '''function primes(x){const r=[];let d=2;while(d*d<=x){if(x%d===0){r.push(d);while(x%d===0)x=Math.floor(x/d);}d++;}if(x>1)r.push(x);return r;}
function can(a){const n=a.length;const par=Array.from({length:n},(_,i)=>i);function f(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}function u(x,y){x=f(x);y=f(y);if(x!==y)par[x]=y;}const pm=new Map();for(let i=0;i<n;i++)for(const p of primes(a[i])){if(pm.has(p))u(i,pm.get(p));else pm.set(p,i);}const r=f(0);for(let i=0;i<n;i++)if(f(i)!==r)return false;return true;}
console.log(can([2,3,6]));console.log(can([3,9,5]));console.log(can([4,3,12,8]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] par;
  static int f(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
  static void u(int x,int y){x=f(x);y=f(y);if(x!=y)par[x]=y;}
  static List<Integer> primes(int x){List<Integer> r=new ArrayList<>();for(int d=2;1L*d*d<=x;d++)if(x%d==0){r.add(d);while(x%d==0)x/=d;}if(x>1)r.add(x);return r;}
  static boolean can(int[]a){int n=a.length;par=new int[n];for(int i=0;i<n;i++)par[i]=i;Map<Integer,Integer> pm=new HashMap<>();for(int i=0;i<n;i++)for(int p:primes(a[i])){if(pm.containsKey(p))u(i,pm.get(p));else pm.put(p,i);}int r=f(0);for(int i=0;i<n;i++)if(f(i)!=r)return false;return true;}
  public static void main(String[]x){System.out.println(can(new int[]{2,3,6}));System.out.println(can(new int[]{3,9,5}));System.out.println(can(new int[]{4,3,12,8}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> par;
int f(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
void u(int x,int y){x=f(x);y=f(y);if(x!=y)par[x]=y;}
vector<int> primes(int x){vector<int> r;for(int d=2;1LL*d*d<=x;d++)if(x%d==0){r.push_back(d);while(x%d==0)x/=d;}if(x>1)r.push_back(x);return r;}
bool can(vector<int> a){int n=a.size();par.assign(n,0);iota(par.begin(),par.end(),0);unordered_map<int,int> pm;for(int i=0;i<n;i++)for(int p:primes(a[i])){auto it=pm.find(p);if(it!=pm.end())u(i,it->second);else pm[p]=i;}int r=f(0);for(int i=0;i<n;i++)if(f(i)!=r)return false;return true;}
int main(){cout<<boolalpha<<can({2,3,6})<<"\\n"<<can({3,9,5})<<"\\n"<<can({4,3,12,8})<<"\\n";}
''',
"Go": '''package main
import "fmt"
var par []int
func f(x int) int { for par[x]!=x { par[x]=par[par[x]]; x=par[x] }; return x }
func u(x,y int){ x=f(x); y=f(y); if x!=y { par[x]=y } }
func primes(x int) []int { var r []int; for d:=2;d*d<=x;d++ { if x%d==0 { r=append(r,d); for x%d==0 { x/=d } } }; if x>1 { r=append(r,x) }; return r }
func can(a []int) bool { n:=len(a); par=make([]int,n); for i:=range par { par[i]=i }; pm:=map[int]int{}; for i:=0;i<n;i++ { for _,p:=range primes(a[i]) { if v,ok:=pm[p]; ok { u(i,v) } else { pm[p]=i } } }; r:=f(0); for i:=0;i<n;i++ { if f(i)!=r { return false } }; return true }
func main(){ fmt.Println(can([]int{2,3,6})); fmt.Println(can([]int{3,9,5})); fmt.Println(can([]int{4,3,12,8})) }
''',
"R": '''par <- NULL
f <- function(x){ while(par[x]!=x){ par[x]<<-par[par[x]]; x<-par[x] }; x }
u <- function(x,y){ x<-f(x); y<-f(y); if(x!=y) par[x]<<-y }
primes <- function(x){ r<-c(); d<-2; while(d*d<=x){ if(x%%d==0){ r<-c(r,d); while(x%%d==0) x<-x%/%d }; d<-d+1 }; if(x>1) r<-c(r,x); r }
can <- function(a){ n<-length(a); par<<-1:n; pm<-list(); for(i in 1:n) for(p in primes(a[i])){ k<-as.character(p); if(!is.null(pm[[k]])) u(i,pm[[k]]) else pm[[k]]<-i }; r<-f(1); all(sapply(1:n,f)==r) }
cat(can(c(2,3,6)),"\\n"); cat(can(c(3,9,5)),"\\n"); cat(can(c(4,3,12,8)),"\\n")
''',
}))

# 157 Add Binary
L.append((157, "Add Binary", "Bit Manipulation", "Easy", 79,
"Given two binary strings, return their sum as a binary string.",
{
"Python": '''def addBin(a,b):
    return bin(int(a,2)+int(b,2))[2:]

if __name__=="__main__":
    print(addBin("11","1")); print(addBin("1010","1011"))
''',
"JavaScript": '''function addBin(a,b){let i=a.length-1,j=b.length-1,c=0;const r=[];while(i>=0||j>=0||c){const s=c+(i>=0?+a[i--]:0)+(j>=0?+b[j--]:0);r.push(s%2);c=s>>1;}return r.reverse().join("");}
console.log(addBin("11","1"));console.log(addBin("1010","1011"));
''',
"Java": '''public class __CLASS__{
  static String addBin(String a,String b){int i=a.length()-1,j=b.length()-1,c=0;StringBuilder sb=new StringBuilder();while(i>=0||j>=0||c>0){int s=c+(i>=0?a.charAt(i--)-'0':0)+(j>=0?b.charAt(j--)-'0':0);sb.append(s%2);c=s/2;}return sb.reverse().toString();}
  public static void main(String[]x){System.out.println(addBin("11","1"));System.out.println(addBin("1010","1011"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string addBin(string a,string b){int i=a.size()-1,j=b.size()-1,c=0;string r;while(i>=0||j>=0||c){int s=c+(i>=0?a[i--]-'0':0)+(j>=0?b[j--]-'0':0);r+=char('0'+s%2);c=s/2;}reverse(r.begin(),r.end());return r;}
int main(){cout<<addBin("11","1")<<"\\n"<<addBin("1010","1011")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func addBin(a,b string) string { i,j,c:=len(a)-1,len(b)-1,0; var r []byte; for i>=0 || j>=0 || c>0 { s:=c; if i>=0 { s+=int(a[i]-'0'); i-- }; if j>=0 { s+=int(b[j]-'0'); j-- }; r=append(r,byte('0'+s%2)); c=s/2 }; for x,y:=0,len(r)-1; x<y; x,y=x+1,y-1 { r[x],r[y]=r[y],r[x] }; return string(r) }
func main(){ fmt.Println(addBin("11","1")); fmt.Println(addBin("1010","1011")) }
''',
"R": '''addBin <- function(a,b){ i<-nchar(a); j<-nchar(b); c<-0; r<-c(); while(i>=1 || j>=1 || c>0){ s<-c; if(i>=1){ s<-s+as.integer(substr(a,i,i)); i<-i-1 }; if(j>=1){ s<-s+as.integer(substr(b,j,j)); j<-j-1 }; r<-c(s%%2,r); c<-s%/%2 }; paste(r,collapse="") }
cat(addBin("11","1"),"\\n"); cat(addBin("1010","1011"),"\\n")
''',
}))

# 158 Minimum Array End
L.append((158, "Minimum Array End", "Bit Manipulation", "Medium", 79,
"Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.",
{
"Python": '''def minEnd(n,x):
    n-=1; r=x; bit=1; nb=1
    while nb<=n:
        if not (x & bit):
            if n & nb: r |= bit
            nb<<=1
        bit<<=1
    return r

if __name__=="__main__":
    print(minEnd(3,4)); print(minEnd(2,7))
''',
"JavaScript": '''function minEnd(n,x){n--;let r=BigInt(x),bit=1n,nb=1n,nn=BigInt(n),X=BigInt(x);while(nb<=nn){if((X&bit)===0n){if((nn&nb)!==0n)r|=bit;nb<<=1n;}bit<<=1n;}return r.toString();}
console.log(minEnd(3,4));console.log(minEnd(2,7));
''',
"Java": '''public class __CLASS__{
  static long minEnd(long n,long x){n--;long r=x,bit=1,nb=1;while(nb<=n){if((x&bit)==0){if((n&nb)!=0)r|=bit;nb<<=1;}bit<<=1;}return r;}
  public static void main(String[]a){System.out.println(minEnd(3,4));System.out.println(minEnd(2,7));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
long long minEnd(long long n,long long x){n--;long long r=x,bit=1,nb=1;while(nb<=n){if((x&bit)==0){if(n&nb)r|=bit;nb<<=1;}bit<<=1;}return r;}
int main(){cout<<minEnd(3,4)<<"\\n"<<minEnd(2,7)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func minEnd(n,x int64) int64 { n--; r:=x; var bit,nb int64=1,1; for nb<=n { if x&bit==0 { if n&nb!=0 { r|=bit }; nb<<=1 }; bit<<=1 }; return r }
func main(){ fmt.Println(minEnd(3,4)); fmt.Println(minEnd(2,7)) }
''',
"R": '''minEnd <- function(n,x){ n<-n-1; r<-x; bit<-1; nb<-1; while(nb<=n){ if(bitwAnd(x,bit)==0){ if(bitwAnd(n,nb)!=0) r<-bitwOr(r,bit); nb<-bitwShiftL(nb,1) }; bit<-bitwShiftL(bit,1) }; r }
cat(minEnd(3,4),"\\n"); cat(minEnd(2,7),"\\n")
''',
}))

# 159 Find Median From Data Stream
L.append((159, "Find Median From Data Stream", "Heap Priority Queue", "Hard", 80,
"Design MedianFinder: addNum, findMedian.",
{
"Python": '''import heapq
class MedianFinder:
    def __init__(self): self.lo=[]; self.hi=[]
    def addNum(self,x):
        heapq.heappush(self.lo,-x)
        heapq.heappush(self.hi,-heapq.heappop(self.lo))
        if len(self.hi)>len(self.lo): heapq.heappush(self.lo,-heapq.heappop(self.hi))
    def findMedian(self):
        if len(self.lo)>len(self.hi): return -self.lo[0]
        return (-self.lo[0]+self.hi[0])/2

if __name__=="__main__":
    m=MedianFinder()
    for x in [1,2,3]: m.addNum(x); print(m.findMedian())
''',
"JavaScript": '''class MedianFinder{constructor(){this.lo=[];this.hi=[];}_pushMax(h,x){h.push(x);let i=h.length-1;while(i>0){const p=(i-1)>>1;if(h[p]<h[i]){[h[p],h[i]]=[h[i],h[p]];i=p;}else break;}}_popMax(h){const t=h[0],l=h.pop();if(h.length){h[0]=l;let i=0;for(;;){const a=2*i+1,b=a+1;let m=i;if(a<h.length&&h[a]>h[m])m=a;if(b<h.length&&h[b]>h[m])m=b;if(m===i)break;[h[i],h[m]]=[h[m],h[i]];i=m;}}return t;}_pushMin(h,x){h.push(x);let i=h.length-1;while(i>0){const p=(i-1)>>1;if(h[p]>h[i]){[h[p],h[i]]=[h[i],h[p]];i=p;}else break;}}_popMin(h){const t=h[0],l=h.pop();if(h.length){h[0]=l;let i=0;for(;;){const a=2*i+1,b=a+1;let m=i;if(a<h.length&&h[a]<h[m])m=a;if(b<h.length&&h[b]<h[m])m=b;if(m===i)break;[h[i],h[m]]=[h[m],h[i]];i=m;}}return t;}addNum(x){this._pushMax(this.lo,x);this._pushMin(this.hi,this._popMax(this.lo));if(this.hi.length>this.lo.length)this._pushMax(this.lo,this._popMin(this.hi));}findMedian(){if(this.lo.length>this.hi.length)return this.lo[0];return (this.lo[0]+this.hi[0])/2;}}
const m=new MedianFinder();for(const x of [1,2,3]){m.addNum(x);console.log(m.findMedian());}
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class MedianFinder{PriorityQueue<Integer> lo=new PriorityQueue<>(Comparator.reverseOrder());PriorityQueue<Integer> hi=new PriorityQueue<>();void addNum(int x){lo.add(x);hi.add(lo.poll());if(hi.size()>lo.size())lo.add(hi.poll());}double findMedian(){if(lo.size()>hi.size())return lo.peek();return (lo.peek()+hi.peek())/2.0;}}
  public static void main(String[]x){MedianFinder m=new MedianFinder();for(int v:new int[]{1,2,3}){m.addNum(v);System.out.println(m.findMedian());}}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct MedianFinder{ priority_queue<int> lo; priority_queue<int,vector<int>,greater<int>> hi; void addNum(int x){lo.push(x);hi.push(lo.top());lo.pop();if(hi.size()>lo.size()){lo.push(hi.top());hi.pop();}} double findMedian(){if(lo.size()>hi.size())return lo.top();return (lo.top()+hi.top())/2.0;}};
int main(){MedianFinder m;for(int x:{1,2,3}){m.addNum(x);cout<<m.findMedian()<<"\\n";}}
''',
"Go": '''package main
import ("fmt";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
type MaxH struct{ IH }
func (h MaxH) Less(i,j int) bool{ return h.IH[i]>h.IH[j] }
type MedianFinder struct{ lo *MaxH; hi *IH }
func New() *MedianFinder { return &MedianFinder{&MaxH{}, &IH{}} }
func (m *MedianFinder) AddNum(x int){ heap.Push(m.lo,x); heap.Push(m.hi,heap.Pop(m.lo)); if m.hi.Len()>m.lo.Len() { heap.Push(m.lo,heap.Pop(m.hi)) } }
func (m *MedianFinder) FindMedian() float64 { if m.lo.Len()>m.hi.Len() { return float64(m.lo.IH[0]) }; return float64(m.lo.IH[0]+(*m.hi)[0])/2 }
func main(){ m:=New(); for _,x:=range []int{1,2,3}{ m.AddNum(x); fmt.Println(m.FindMedian()) } }
''',
"R": '''MedianFinder <- function(){ lo<-c(); hi<-c(); add<-function(x){ lo<<-c(lo,x); lo<<-sort(lo,decreasing=TRUE); hi<<-c(hi,lo[1]); hi<<-sort(hi); lo<<-lo[-1]; if(length(hi)>length(lo)){ lo<<-c(hi[1],lo); lo<<-sort(lo,decreasing=TRUE); hi<<-hi[-1] } }; med<-function(){ if(length(lo)>length(hi)) lo[1] else (lo[1]+hi[1])/2 }; list(add=add,med=med) }
m<-MedianFinder(); for(x in c(1,2,3)){ m$add(x); cat(m$med(),"\\n") }
''',
}))

# 160 IPO
L.append((160, "IPO", "Heap Priority Queue", "Hard", 80,
"Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.",
{
"Python": '''import heapq
def ipo(k,w,profits,capital):
    proj=sorted(zip(capital,profits)); h=[]; i=0; n=len(profits)
    for _ in range(k):
        while i<n and proj[i][0]<=w: heapq.heappush(h,-proj[i][1]); i+=1
        if not h: break
        w-=heapq.heappop(h)
    return w

if __name__=="__main__":
    print(ipo(2,0,[1,2,3],[0,1,1]))
    print(ipo(3,0,[1,2,3],[0,1,2]))
''',
"JavaScript": '''function ipo(k,w,profits,capital){const proj=capital.map((c,i)=>[c,profits[i]]).sort((a,b)=>a[0]-b[0]);const h=[];let i=0;const popMax=()=>{let mi=0;for(let j=1;j<h.length;j++)if(h[j]>h[mi])mi=j;return h.splice(mi,1)[0];};for(let s=0;s<k;s++){while(i<proj.length&&proj[i][0]<=w)h.push(proj[i++][1]);if(!h.length)break;w+=popMax();}return w;}
console.log(ipo(2,0,[1,2,3],[0,1,1]));console.log(ipo(3,0,[1,2,3],[0,1,2]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int ipo(int k,int w,int[]p,int[]c){int n=p.length;int[][] proj=new int[n][2];for(int i=0;i<n;i++){proj[i][0]=c[i];proj[i][1]=p[i];}Arrays.sort(proj,(a,b)->a[0]-b[0]);PriorityQueue<Integer> h=new PriorityQueue<>(Comparator.reverseOrder());int i=0;for(int s=0;s<k;s++){while(i<n&&proj[i][0]<=w)h.add(proj[i++][1]);if(h.isEmpty())break;w+=h.poll();}return w;}
  public static void main(String[]x){System.out.println(ipo(2,0,new int[]{1,2,3},new int[]{0,1,1}));System.out.println(ipo(3,0,new int[]{1,2,3},new int[]{0,1,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int ipo(int k,int w,vector<int> p,vector<int> c){int n=p.size();vector<pair<int,int>> proj;for(int i=0;i<n;i++)proj.push_back({c[i],p[i]});sort(proj.begin(),proj.end());priority_queue<int> h;int i=0;for(int s=0;s<k;s++){while(i<n&&proj[i].first<=w){h.push(proj[i].second);i++;}if(h.empty())break;w+=h.top();h.pop();}return w;}
int main(){cout<<ipo(2,0,{1,2,3},{0,1,1})<<"\\n"<<ipo(3,0,{1,2,3},{0,1,2})<<"\\n";}
''',
"Go": '''package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]>h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func ipo(k,w int, p,c []int) int { n:=len(p); proj:=make([][2]int,n); for i:=0;i<n;i++ { proj[i]=[2]int{c[i],p[i]} }; sort.Slice(proj,func(i,j int) bool{return proj[i][0]<proj[j][0]}); h:=&IH{}; i:=0; for s:=0;s<k;s++ { for i<n && proj[i][0]<=w { heap.Push(h,proj[i][1]); i++ }; if h.Len()==0 { break }; w+=heap.Pop(h).(int) }; return w }
func main(){ fmt.Println(ipo(2,0,[]int{1,2,3},[]int{0,1,1})); fmt.Println(ipo(3,0,[]int{1,2,3},[]int{0,1,2})) }
''',
"R": '''ipo <- function(k,w,profits,capital){ n<-length(profits); ord<-order(capital); cap<-capital[ord]; pr<-profits[ord]; h<-c(); i<-1; for(s in 1:k){ while(i<=n && cap[i]<=w){ h<-c(h,pr[i]); i<-i+1 }; if(length(h)==0) break; idx<-which.max(h); w<-w+h[idx]; h<-h[-idx] }; w }
cat(ipo(2,0,c(1,2,3),c(0,1,1)),"\\n"); cat(ipo(3,0,c(1,2,3),c(0,1,2)),"\\n")
''',
}))

write_lessons(L)
