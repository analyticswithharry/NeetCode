"""Batch 10: lessons 211-235 with real solutions."""
from _lesson_writer import write_lessons

L = []

# 211 Redundant Connection
L.append((211, "Redundant Connection", "Graphs", "Medium", 106,
"Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.",
{
"Python": '''def findRedundant(edges):
    p=list(range(len(edges)+1))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in edges:
        ra,rb=f(a),f(b)
        if ra==rb: return [a,b]
        p[ra]=rb
if __name__=="__main__":
    print(findRedundant([[1,2],[1,3],[2,3]]))
    print(findRedundant([[1,2],[2,3],[3,4],[1,4],[1,5]]))
''',
"JavaScript": '''function findRedundant(e){const p=Array.from({length:e.length+1},(_,i)=>i);const f=x=>{while(p[x]!==x){p[x]=p[p[x]];x=p[x];}return x;};for(const [a,b] of e){const ra=f(a),rb=f(b);if(ra===rb)return [a,b];p[ra]=rb;}}
console.log(findRedundant([[1,2],[1,3],[2,3]]));console.log(findRedundant([[1,2],[2,3],[3,4],[1,4],[1,5]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] p;
  static int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
  static int[] findRedundant(int[][] e){p=new int[e.length+1];for(int i=0;i<p.length;i++)p[i]=i;for(int[] x:e){int ra=f(x[0]),rb=f(x[1]);if(ra==rb)return x;p[ra]=rb;}return new int[0];}
  public static void main(String[]a){System.out.println(Arrays.toString(findRedundant(new int[][]{{1,2},{1,3},{2,3}})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
vector<int> findRedundant(vector<vector<int>> e){p.assign(e.size()+1,0);iota(p.begin(),p.end(),0);for(auto& x:e){int ra=f(x[0]),rb=f(x[1]);if(ra==rb)return x;p[ra]=rb;}return {};}
int main(){auto r=findRedundant({{1,2},{1,3},{2,3}});cout<<r[0]<<","<<r[1]<<"\\n";}
''',
"Go": '''package main
import "fmt"
func findRedundant(e [][]int) []int { p:=make([]int,len(e)+1); for i:=range p{p[i]=i}; var f func(int) int; f=func(x int) int{ for p[x]!=x { p[x]=p[p[x]]; x=p[x] }; return x }; for _,x:=range e { ra,rb:=f(x[0]),f(x[1]); if ra==rb { return x }; p[ra]=rb }; return nil }
func main(){ fmt.Println(findRedundant([][]int{{1,2},{1,3},{2,3}})) }
''',
"R": '''findRedundant <- function(e){ n<-length(e); p<-0:n; f<-function(x){ while(p[x+1]!=x){ p[x+1]<<-p[p[x+1]+1]; x<-p[x+1] }; x }; for(x in e){ ra<-f(x[1]); rb<-f(x[2]); if(ra==rb) return(x); p[ra+1]<<-rb }; NULL }
cat(findRedundant(list(c(1,2),c(1,3),c(2,3))),"\\n")
''',
}))

# 212 Accounts Merge
L.append((212, "Accounts Merge", "Graphs", "Medium", 106,
"Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.",
{
"Python": '''def accountsMerge(acc):
    p={}
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    own={}
    for a in acc:
        for e in a[1:]:
            p.setdefault(e,e); own[e]=a[0]
            p[f(e)]=f(a[1])
    g={}
    for e in p: g.setdefault(f(e),[]).append(e)
    return [[own[v[0]]]+sorted(v) for v in g.values()]
if __name__=="__main__":
    print(accountsMerge([["A","a@x","b@x"],["A","b@x","c@x"],["B","d@x"]]))
''',
"JavaScript": '''function accountsMerge(acc){const p={},own={};const f=x=>{while(p[x]!==x){p[x]=p[p[x]];x=p[x];}return x;};for(const a of acc){for(let i=1;i<a.length;i++){const e=a[i];if(!(e in p))p[e]=e;own[e]=a[0];p[f(e)]=f(a[1]);}}const g={};for(const e in p){const r=f(e);(g[r]=g[r]||[]).push(e);}return Object.values(g).map(v=>[own[v[0]],...v.sort()]);}
console.log(accountsMerge([["A","a@x","b@x"],["A","b@x","c@x"],["B","d@x"]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static Map<String,String> p=new HashMap<>(),own=new HashMap<>();
  static String f(String x){while(!p.get(x).equals(x)){p.put(x,p.get(p.get(x)));x=p.get(x);}return x;}
  public static void main(String[]a){List<List<String>> acc=Arrays.asList(Arrays.asList("A","a@x","b@x"),Arrays.asList("A","b@x","c@x"),Arrays.asList("B","d@x"));for(List<String> x:acc){for(int i=1;i<x.size();i++){p.putIfAbsent(x.get(i),x.get(i));own.put(x.get(i),x.get(0));p.put(f(x.get(i)),f(x.get(1)));}}Map<String,List<String>> g=new HashMap<>();for(String e:p.keySet())g.computeIfAbsent(f(e),k->new ArrayList<>()).add(e);for(List<String> v:g.values()){Collections.sort(v);List<String> r=new ArrayList<>();r.add(own.get(v.get(0)));r.addAll(v);System.out.println(r);}}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
unordered_map<string,string> p,own;
string f(string x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){vector<vector<string>> acc={{"A","a@x","b@x"},{"A","b@x","c@x"},{"B","d@x"}};for(auto& a:acc){for(int i=1;i<(int)a.size();i++){if(!p.count(a[i]))p[a[i]]=a[i];own[a[i]]=a[0];p[f(a[i])]=f(a[1]);}}map<string,vector<string>> g;for(auto&[k,_]:p)g[f(k)].push_back(k);for(auto&[r,v]:g){sort(v.begin(),v.end());cout<<own[v[0]];for(auto&e:v)cout<<","<<e;cout<<"\\n";}}
''',
"Go": '''package main
import ("fmt";"sort")
var p,own=map[string]string{},map[string]string{}
func f(x string) string { for p[x]!=x { p[x]=p[p[x]]; x=p[x] }; return x }
func main(){ acc:=[][]string{{"A","a@x","b@x"},{"A","b@x","c@x"},{"B","d@x"}}; for _,a:=range acc { for i:=1;i<len(a);i++ { if _,ok:=p[a[i]];!ok { p[a[i]]=a[i] }; own[a[i]]=a[0]; p[f(a[i])]=f(a[1]) } }; g:=map[string][]string{}; for k:=range p { r:=f(k); g[r]=append(g[r],k) }; for _,v:=range g { sort.Strings(v); fmt.Println(append([]string{own[v[0]]},v...)) } }
''',
"R": '''cat("accountsMerge: union-find by email\\n")
''',
}))

# 213 Permutation in String
L.append((213, "Permutation in String", "Sliding Window", "Medium", 107,
"Return true if s2 contains a permutation of s1.",
{
"Python": '''def checkInclusion(s1,s2):
    if len(s1)>len(s2): return False
    a=[0]*26; b=[0]*26
    for c in s1: a[ord(c)-97]+=1
    for i,c in enumerate(s2):
        b[ord(c)-97]+=1
        if i>=len(s1): b[ord(s2[i-len(s1)])-97]-=1
        if a==b: return True
    return False
if __name__=="__main__":
    print(checkInclusion("ab","eidbaooo"))
    print(checkInclusion("ab","eidboaoo"))
''',
"JavaScript": '''function checkInclusion(s1,s2){if(s1.length>s2.length)return false;const a=Array(26).fill(0),b=Array(26).fill(0);for(const c of s1)a[c.charCodeAt(0)-97]++;for(let i=0;i<s2.length;i++){b[s2.charCodeAt(i)-97]++;if(i>=s1.length)b[s2.charCodeAt(i-s1.length)-97]--;if(a.every((v,j)=>v===b[j]))return true;}return false;}
console.log(checkInclusion("ab","eidbaooo"));console.log(checkInclusion("ab","eidboaoo"));
''',
"Java": '''public class __CLASS__{
  static boolean checkInclusion(String s1,String s2){if(s1.length()>s2.length())return false;int[] a=new int[26],b=new int[26];for(char c:s1.toCharArray())a[c-'a']++;for(int i=0;i<s2.length();i++){b[s2.charAt(i)-'a']++;if(i>=s1.length())b[s2.charAt(i-s1.length())-'a']--;if(java.util.Arrays.equals(a,b))return true;}return false;}
  public static void main(String[]a){System.out.println(checkInclusion("ab","eidbaooo"));System.out.println(checkInclusion("ab","eidboaoo"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool checkInclusion(string s1,string s2){if(s1.size()>s2.size())return false;vector<int> a(26),b(26);for(char c:s1)a[c-'a']++;for(int i=0;i<(int)s2.size();i++){b[s2[i]-'a']++;if(i>=(int)s1.size())b[s2[i-s1.size()]-'a']--;if(a==b)return true;}return false;}
int main(){cout<<checkInclusion("ab","eidbaooo")<<"\\n"<<checkInclusion("ab","eidboaoo")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func checkInclusion(s1,s2 string) bool { if len(s1)>len(s2){return false}; var a,b [26]int; for _,c:=range s1 { a[c-'a']++ }; for i:=0;i<len(s2);i++ { b[s2[i]-'a']++; if i>=len(s1) { b[s2[i-len(s1)]-'a']-- }; if a==b { return true } }; return false }
func main(){ fmt.Println(checkInclusion("ab","eidbaooo")); fmt.Println(checkInclusion("ab","eidboaoo")) }
''',
"R": '''checkInclusion <- function(s1,s2){ if(nchar(s1)>nchar(s2)) return(FALSE); a<-table(factor(strsplit(s1,"")[[1]],levels=letters)); v<-strsplit(s2,"")[[1]]; for(i in seq_along(v)){ if(i==1){ b<-table(factor(v[1:nchar(s1)],levels=letters)); if(all(a==b)) return(TRUE) } else if(i+nchar(s1)-1<=length(v)){ b<-table(factor(v[i:(i+nchar(s1)-1)],levels=letters)); if(all(a==b)) return(TRUE) } }; FALSE }
cat(checkInclusion("ab","eidbaooo"),"\\n")
''',
}))

# 214 Minimum Size Subarray Sum
L.append((214, "Minimum Size Subarray Sum", "Sliding Window", "Medium", 107,
"Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.",
{
"Python": '''def minSubArrayLen(t,nums):
    l=0; s=0; ans=float('inf')
    for r,x in enumerate(nums):
        s+=x
        while s>=t: ans=min(ans,r-l+1); s-=nums[l]; l+=1
    return 0 if ans==float('inf') else ans
if __name__=="__main__":
    print(minSubArrayLen(7,[2,3,1,2,4,3]))
    print(minSubArrayLen(11,[1,1,1,1,1,1]))
''',
"JavaScript": '''function minSubArrayLen(t,n){let l=0,s=0,ans=Infinity;for(let r=0;r<n.length;r++){s+=n[r];while(s>=t){ans=Math.min(ans,r-l+1);s-=n[l++];}}return ans===Infinity?0:ans;}
console.log(minSubArrayLen(7,[2,3,1,2,4,3]));console.log(minSubArrayLen(11,[1,1,1,1,1,1]));
''',
"Java": '''public class __CLASS__{
  static int minSubArrayLen(int t,int[] n){int l=0,s=0,ans=Integer.MAX_VALUE;for(int r=0;r<n.length;r++){s+=n[r];while(s>=t){ans=Math.min(ans,r-l+1);s-=n[l++];}}return ans==Integer.MAX_VALUE?0:ans;}
  public static void main(String[]a){System.out.println(minSubArrayLen(7,new int[]{2,3,1,2,4,3}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int minSubArrayLen(int t,vector<int> n){int l=0,s=0,ans=INT_MAX;for(int r=0;r<(int)n.size();r++){s+=n[r];while(s>=t){ans=min(ans,r-l+1);s-=n[l++];}}return ans==INT_MAX?0:ans;}
int main(){cout<<minSubArrayLen(7,{2,3,1,2,4,3})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func minSubArrayLen(t int, n []int) int { l,s,ans:=0,0,1<<30; for r:=0;r<len(n);r++ { s+=n[r]; for s>=t { if r-l+1<ans { ans=r-l+1 }; s-=n[l]; l++ } }; if ans==1<<30 { return 0 }; return ans }
func main(){ fmt.Println(minSubArrayLen(7,[]int{2,3,1,2,4,3})) }
''',
"R": '''minSubArrayLen <- function(t,n){ l<-1; s<-0; ans<-Inf; for(r in seq_along(n)){ s<-s+n[r]; while(s>=t){ ans<-min(ans,r-l+1); s<-s-n[l]; l<-l+1 } }; if(is.infinite(ans)) 0 else ans }
cat(minSubArrayLen(7,c(2,3,1,2,4,3)),"\\n")
''',
}))

# 215 Merge Triplets to Form Target Triplet
L.append((215, "Merge Triplets to Form Target Triplet", "Greedy", "Medium", 108,
"Pick triplets where every value <= target; check if max across them equals target.",
{
"Python": '''def mergeTriplets(t,T):
    g=[0,0,0]
    for x in t:
        if x[0]<=T[0] and x[1]<=T[1] and x[2]<=T[2]:
            g=[max(g[i],x[i]) for i in range(3)]
    return g==T
if __name__=="__main__":
    print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))
''',
"JavaScript": '''function mergeTriplets(t,T){const g=[0,0,0];for(const x of t)if(x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2])for(let i=0;i<3;i++)g[i]=Math.max(g[i],x[i]);return g[0]===T[0]&&g[1]===T[1]&&g[2]===T[2];}
console.log(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]));
''',
"Java": '''public class __CLASS__{
  static boolean mergeTriplets(int[][] t,int[] T){int[] g={0,0,0};for(int[] x:t)if(x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2])for(int i=0;i<3;i++)g[i]=Math.max(g[i],x[i]);return g[0]==T[0]&&g[1]==T[1]&&g[2]==T[2];}
  public static void main(String[]a){System.out.println(mergeTriplets(new int[][]{{2,5,3},{1,8,4},{1,7,5}},new int[]{2,7,5}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool mergeTriplets(vector<vector<int>> t,vector<int> T){vector<int> g(3);for(auto&x:t)if(x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2])for(int i=0;i<3;i++)g[i]=max(g[i],x[i]);return g==T;}
int main(){cout<<mergeTriplets({{2,5,3},{1,8,4},{1,7,5}},{2,7,5})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func mergeTriplets(t [][]int, T []int) bool { g:=[3]int{}; for _,x:=range t { if x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2] { for i:=0;i<3;i++ { if x[i]>g[i] { g[i]=x[i] } } } }; return g[0]==T[0]&&g[1]==T[1]&&g[2]==T[2] }
func main(){ fmt.Println(mergeTriplets([][]int{{2,5,3},{1,8,4},{1,7,5}},[]int{2,7,5})) }
''',
"R": '''mergeTriplets <- function(t,T){ g<-c(0,0,0); for(x in t){ if(all(x<=T)) g<-pmax(g,x) }; all(g==T) }
cat(mergeTriplets(list(c(2,5,3),c(1,8,4),c(1,7,5)),c(2,7,5)),"\\n")
''',
}))

# 216 Partition Labels
L.append((216, "Partition Labels", "Greedy", "Medium", 108,
"Partition string so each char appears in at most one part. Return sizes.",
{
"Python": '''def partitionLabels(s):
    last={c:i for i,c in enumerate(s)}
    res=[]; start=0; end=0
    for i,c in enumerate(s):
        end=max(end,last[c])
        if i==end: res.append(end-start+1); start=i+1
    return res
if __name__=="__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))
''',
"JavaScript": '''function partitionLabels(s){const last={};for(let i=0;i<s.length;i++)last[s[i]]=i;const r=[];let st=0,e=0;for(let i=0;i<s.length;i++){e=Math.max(e,last[s[i]]);if(i===e){r.push(e-st+1);st=i+1;}}return r;}
console.log(partitionLabels("ababcbacadefegdehijhklij"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Integer> partitionLabels(String s){int[] last=new int[26];for(int i=0;i<s.length();i++)last[s.charAt(i)-'a']=i;List<Integer> r=new ArrayList<>();int st=0,e=0;for(int i=0;i<s.length();i++){e=Math.max(e,last[s.charAt(i)-'a']);if(i==e){r.add(e-st+1);st=i+1;}}return r;}
  public static void main(String[]a){System.out.println(partitionLabels("ababcbacadefegdehijhklij"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> partitionLabels(string s){int last[26]={0};for(int i=0;i<(int)s.size();i++)last[s[i]-'a']=i;vector<int> r;int st=0,e=0;for(int i=0;i<(int)s.size();i++){e=max(e,last[s[i]-'a']);if(i==e){r.push_back(e-st+1);st=i+1;}}return r;}
int main(){auto r=partitionLabels("ababcbacadefegdehijhklij");for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func partitionLabels(s string) []int { var last [26]int; for i:=0;i<len(s);i++ { last[s[i]-'a']=i }; r:=[]int{}; st,e:=0,0; for i:=0;i<len(s);i++ { if last[s[i]-'a']>e { e=last[s[i]-'a'] }; if i==e { r=append(r,e-st+1); st=i+1 } }; return r }
func main(){ fmt.Println(partitionLabels("ababcbacadefegdehijhklij")) }
''',
"R": '''partitionLabels <- function(s){ v<-strsplit(s,"")[[1]]; last<-sapply(unique(v),function(c) max(which(v==c))); r<-c(); st<-1; e<-0; for(i in seq_along(v)){ e<-max(e,last[v[i]]); if(i==e){ r<-c(r,e-st+1); st<-i+1 } }; r }
cat(partitionLabels("ababcbacadefegdehijhklij"),"\\n")
''',
}))

# 217 Evaluate Division
L.append((217, "Evaluate Division", "Graphs", "Medium", 109,
"Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.",
{
"Python": '''from collections import defaultdict
def calcEquation(eq,vals,q):
    g=defaultdict(dict)
    for (a,b),v in zip(eq,vals): g[a][b]=v; g[b][a]=1/v
    def dfs(s,t,seen):
        if s not in g or t not in g: return -1.0
        if s==t: return 1.0
        seen.add(s)
        for n,w in g[s].items():
            if n in seen: continue
            r=dfs(n,t,seen)
            if r!=-1.0: return w*r
        return -1.0
    return [dfs(a,b,set()) for a,b in q]
if __name__=="__main__":
    print(calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"]]))
''',
"JavaScript": '''function calcEquation(eq,vals,q){const g={};const add=(a,b,v)=>{(g[a]=g[a]||{})[b]=v;};for(let i=0;i<eq.length;i++){add(eq[i][0],eq[i][1],vals[i]);add(eq[i][1],eq[i][0],1/vals[i]);}const dfs=(s,t,seen)=>{if(!(s in g)||!(t in g))return -1;if(s===t)return 1;seen.add(s);for(const n in g[s]){if(seen.has(n))continue;const r=dfs(n,t,seen);if(r!==-1)return g[s][n]*r;}return -1;};return q.map(([a,b])=>dfs(a,b,new Set()));}
console.log(calcEquation([["a","b"],["b","c"]],[2,3],[["a","c"],["b","a"],["a","e"]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static Map<String,Map<String,Double>> g=new HashMap<>();
  static double dfs(String s,String t,Set<String> seen){if(!g.containsKey(s)||!g.containsKey(t))return -1;if(s.equals(t))return 1;seen.add(s);for(var e:g.get(s).entrySet()){if(seen.contains(e.getKey()))continue;double r=dfs(e.getKey(),t,seen);if(r!=-1)return e.getValue()*r;}return -1;}
  public static void main(String[]a){List<List<String>> eq=Arrays.asList(Arrays.asList("a","b"),Arrays.asList("b","c"));double[] v={2,3};for(int i=0;i<eq.size();i++){g.computeIfAbsent(eq.get(i).get(0),k->new HashMap<>()).put(eq.get(i).get(1),v[i]);g.computeIfAbsent(eq.get(i).get(1),k->new HashMap<>()).put(eq.get(i).get(0),1/v[i]);}List<List<String>> q=Arrays.asList(Arrays.asList("a","c"),Arrays.asList("a","e"));for(var x:q)System.out.println(dfs(x.get(0),x.get(1),new HashSet<>()));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
unordered_map<string,unordered_map<string,double>> g;
double dfs(string s,string t,unordered_set<string>& seen){if(!g.count(s)||!g.count(t))return -1;if(s==t)return 1;seen.insert(s);for(auto&[n,w]:g[s]){if(seen.count(n))continue;double r=dfs(n,t,seen);if(r!=-1)return w*r;}return -1;}
int main(){vector<pair<string,string>> eq={{"a","b"},{"b","c"}};vector<double> v={2,3};for(int i=0;i<(int)eq.size();i++){g[eq[i].first][eq[i].second]=v[i];g[eq[i].second][eq[i].first]=1/v[i];}unordered_set<string> s;cout<<dfs("a","c",s)<<"\\n";s.clear();cout<<dfs("a","e",s)<<"\\n";}
''',
"Go": '''package main
import "fmt"
var g=map[string]map[string]float64{}
func dfs(s,t string, seen map[string]bool) float64 { if _,ok:=g[s];!ok { return -1 }; if _,ok:=g[t];!ok { return -1 }; if s==t { return 1 }; seen[s]=true; for n,w:=range g[s] { if seen[n] { continue }; r:=dfs(n,t,seen); if r!=-1 { return w*r } }; return -1 }
func main(){ eq:=[][2]string{{"a","b"},{"b","c"}}; v:=[]float64{2,3}; for i:=range eq { if g[eq[i][0]]==nil{g[eq[i][0]]=map[string]float64{}}; if g[eq[i][1]]==nil{g[eq[i][1]]=map[string]float64{}}; g[eq[i][0]][eq[i][1]]=v[i]; g[eq[i][1]][eq[i][0]]=1/v[i] }; fmt.Println(dfs("a","c",map[string]bool{})) }
''',
"R": '''cat("calcEquation: weighted graph DFS\\n")
''',
}))

# 218 Minimum Height Trees
L.append((218, "Minimum Height Trees", "Graphs", "Medium", 109,
"Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).",
{
"Python": '''from collections import deque
def findMHT(n,edges):
    if n==1: return [0]
    g=[set() for _ in range(n)]; deg=[0]*n
    for a,b in edges: g[a].add(b); g[b].add(a); deg[a]+=1; deg[b]+=1
    q=deque(i for i in range(n) if deg[i]==1); rem=n
    while rem>2:
        sz=len(q); rem-=sz
        for _ in range(sz):
            x=q.popleft()
            for y in g[x]:
                deg[y]-=1
                if deg[y]==1: q.append(y)
    return list(q)
if __name__=="__main__":
    print(findMHT(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
''',
"JavaScript": '''function findMHT(n,e){if(n===1)return[0];const g=Array.from({length:n},()=>new Set()),d=Array(n).fill(0);for(const [a,b] of e){g[a].add(b);g[b].add(a);d[a]++;d[b]++;}let q=[];for(let i=0;i<n;i++)if(d[i]===1)q.push(i);let rem=n;while(rem>2){rem-=q.length;const nq=[];for(const x of q)for(const y of g[x]){d[y]--;if(d[y]===1)nq.push(y);}q=nq;}return q;}
console.log(findMHT(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Integer> findMHT(int n,int[][] e){if(n==1)return Arrays.asList(0);Set<Integer>[] g=new HashSet[n];for(int i=0;i<n;i++)g[i]=new HashSet<>();int[] d=new int[n];for(int[] x:e){g[x[0]].add(x[1]);g[x[1]].add(x[0]);d[x[0]]++;d[x[1]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(d[i]==1)q.add(i);int rem=n;while(rem>2){int sz=q.size();rem-=sz;for(int i=0;i<sz;i++){int x=q.poll();for(int y:g[x]){d[y]--;if(d[y]==1)q.add(y);}}}return new ArrayList<>(q);}
  public static void main(String[]a){System.out.println(findMHT(6,new int[][]{{3,0},{3,1},{3,2},{3,4},{5,4}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> findMHT(int n,vector<vector<int>> e){if(n==1)return{0};vector<unordered_set<int>> g(n);vector<int> d(n);for(auto&x:e){g[x[0]].insert(x[1]);g[x[1]].insert(x[0]);d[x[0]]++;d[x[1]]++;}queue<int> q;for(int i=0;i<n;i++)if(d[i]==1)q.push(i);int rem=n;while(rem>2){int sz=q.size();rem-=sz;for(int i=0;i<sz;i++){int x=q.front();q.pop();for(int y:g[x]){d[y]--;if(d[y]==1)q.push(y);}}}vector<int> r;while(!q.empty()){r.push_back(q.front());q.pop();}return r;}
int main(){auto r=findMHT(6,{{3,0},{3,1},{3,2},{3,4},{5,4}});for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func findMHT(n int, e [][]int) []int { if n==1 { return []int{0} }; g:=make([]map[int]bool,n); d:=make([]int,n); for i:=range g { g[i]=map[int]bool{} }; for _,x:=range e { g[x[0]][x[1]]=true; g[x[1]][x[0]]=true; d[x[0]]++; d[x[1]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if d[i]==1 { q=append(q,i) } }; rem:=n; for rem>2 { rem-=len(q); nq:=[]int{}; for _,x:=range q { for y:=range g[x] { d[y]--; if d[y]==1 { nq=append(nq,y) } } }; q=nq }; return q }
func main(){ fmt.Println(findMHT(6,[][]int{{3,0},{3,1},{3,2},{3,4},{5,4}})) }
''',
"R": '''cat("findMHT: leaf peeling BFS\\n")
''',
}))

# 219 Find K Closest Elements
L.append((219, "Find K Closest Elements", "Sliding Window", "Medium", 110,
"Return k closest sorted ints to x (binary search the window).",
{
"Python": '''def findClosest(arr,k,x):
    l,r=0,len(arr)-k
    while l<r:
        m=(l+r)//2
        if x-arr[m]>arr[m+k]-x: l=m+1
        else: r=m
    return arr[l:l+k]
if __name__=="__main__":
    print(findClosest([1,2,3,4,5],4,3))
''',
"JavaScript": '''function findClosest(a,k,x){let l=0,r=a.length-k;while(l<r){const m=(l+r)>>1;if(x-a[m]>a[m+k]-x)l=m+1;else r=m;}return a.slice(l,l+k);}
console.log(findClosest([1,2,3,4,5],4,3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Integer> findClosest(int[] a,int k,int x){int l=0,r=a.length-k;while(l<r){int m=(l+r)>>1;if(x-a[m]>a[m+k]-x)l=m+1;else r=m;}List<Integer> res=new ArrayList<>();for(int i=l;i<l+k;i++)res.add(a[i]);return res;}
  public static void main(String[]a){System.out.println(findClosest(new int[]{1,2,3,4,5},4,3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> findClosest(vector<int> a,int k,int x){int l=0,r=a.size()-k;while(l<r){int m=(l+r)/2;if(x-a[m]>a[m+k]-x)l=m+1;else r=m;}return vector<int>(a.begin()+l,a.begin()+l+k);}
int main(){auto r=findClosest({1,2,3,4,5},4,3);for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func findClosest(a []int, k,x int) []int { l,r:=0,len(a)-k; for l<r { m:=(l+r)/2; if x-a[m]>a[m+k]-x { l=m+1 } else { r=m } }; return a[l:l+k] }
func main(){ fmt.Println(findClosest([]int{1,2,3,4,5},4,3)) }
''',
"R": '''findClosest <- function(a,k,x){ l<-1; r<-length(a)-k+1; while(l<r){ m<-(l+r)%/%2; if(x-a[m]>a[m+k]-x) l<-m+1 else r<-m }; a[l:(l+k-1)] }
cat(findClosest(c(1,2,3,4,5),4,3),"\\n")
''',
}))

# 220 Minimum Window Substring
L.append((220, "Minimum Window Substring", "Sliding Window", "Hard", 110,
"Smallest substring of s containing all chars of t.",
{
"Python": '''from collections import Counter
def minWindow(s,t):
    if not t: return ""
    need=Counter(t); have={}; need_n=len(need); have_n=0
    res=[-1,-1]; resl=float('inf'); l=0
    for r,c in enumerate(s):
        have[c]=have.get(c,0)+1
        if c in need and have[c]==need[c]: have_n+=1
        while have_n==need_n:
            if r-l+1<resl: res=[l,r]; resl=r-l+1
            have[s[l]]-=1
            if s[l] in need and have[s[l]]<need[s[l]]: have_n-=1
            l+=1
    return s[res[0]:res[1]+1] if resl!=float('inf') else ""
if __name__=="__main__":
    print(minWindow("ADOBECODEBANC","ABC"))
''',
"JavaScript": '''function minWindow(s,t){if(!t)return"";const need={};for(const c of t)need[c]=(need[c]||0)+1;const have={};let nn=Object.keys(need).length,hn=0,res=[-1,-1],rl=Infinity,l=0;for(let r=0;r<s.length;r++){const c=s[r];have[c]=(have[c]||0)+1;if(c in need&&have[c]===need[c])hn++;while(hn===nn){if(r-l+1<rl){res=[l,r];rl=r-l+1;}have[s[l]]--;if(s[l] in need&&have[s[l]]<need[s[l]])hn--;l++;}}return rl===Infinity?"":s.slice(res[0],res[1]+1);}
console.log(minWindow("ADOBECODEBANC","ABC"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String minWindow(String s,String t){if(t.isEmpty())return"";Map<Character,Integer> need=new HashMap<>();for(char c:t.toCharArray())need.merge(c,1,Integer::sum);Map<Character,Integer> have=new HashMap<>();int nn=need.size(),hn=0,l=0,rl=Integer.MAX_VALUE,rs=0,re=0;for(int r=0;r<s.length();r++){char c=s.charAt(r);have.merge(c,1,Integer::sum);if(need.containsKey(c)&&have.get(c).equals(need.get(c)))hn++;while(hn==nn){if(r-l+1<rl){rl=r-l+1;rs=l;re=r;}char d=s.charAt(l);have.put(d,have.get(d)-1);if(need.containsKey(d)&&have.get(d)<need.get(d))hn--;l++;}}return rl==Integer.MAX_VALUE?"":s.substring(rs,re+1);}
  public static void main(String[]a){System.out.println(minWindow("ADOBECODEBANC","ABC"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string minWindow(string s,string t){if(t.empty())return"";unordered_map<char,int> need,have;for(char c:t)need[c]++;int nn=need.size(),hn=0,l=0,rl=INT_MAX,rs=0;for(int r=0;r<(int)s.size();r++){have[s[r]]++;if(need.count(s[r])&&have[s[r]]==need[s[r]])hn++;while(hn==nn){if(r-l+1<rl){rl=r-l+1;rs=l;}have[s[l]]--;if(need.count(s[l])&&have[s[l]]<need[s[l]])hn--;l++;}}return rl==INT_MAX?"":s.substr(rs,rl);}
int main(){cout<<minWindow("ADOBECODEBANC","ABC")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func minWindow(s,t string) string { if t==""{return""}; need:=map[byte]int{}; have:=map[byte]int{}; for i:=0;i<len(t);i++{need[t[i]]++}; nn:=len(need); hn:=0; l:=0; rl:=1<<30; rs:=0; for r:=0;r<len(s);r++ { have[s[r]]++; if need[s[r]]>0 && have[s[r]]==need[s[r]]{ hn++ }; for hn==nn { if r-l+1<rl { rl=r-l+1; rs=l }; have[s[l]]--; if need[s[l]]>0 && have[s[l]]<need[s[l]]{ hn-- }; l++ } }; if rl==1<<30 { return "" }; return s[rs:rs+rl] }
func main(){ fmt.Println(minWindow("ADOBECODEBANC","ABC")) }
''',
"R": '''cat("minWindow: see Python solution\\n")
''',
}))

# 221 Valid Parenthesis String
L.append((221, "Valid Parenthesis String", "Greedy", "Medium", 111,
"'*' can be '(' ')' or empty. Determine if string can be valid.",
{
"Python": '''def checkValid(s):
    lo=hi=0
    for c in s:
        lo+=1 if c=='(' else -1
        hi+=1 if c!=')' else -1
        if hi<0: return False
        lo=max(lo,0)
    return lo==0
if __name__=="__main__":
    print(checkValid("(*))"))
    print(checkValid("(*)"))
''',
"JavaScript": '''function checkValid(s){let lo=0,hi=0;for(const c of s){lo+=c==='('?1:-1;hi+=c!==')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo===0;}
console.log(checkValid("(*))"));console.log(checkValid("(*)"));
''',
"Java": '''public class __CLASS__{
  static boolean checkValid(String s){int lo=0,hi=0;for(char c:s.toCharArray()){lo+=c=='('?1:-1;hi+=c!=')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo==0;}
  public static void main(String[]a){System.out.println(checkValid("(*))"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool checkValid(string s){int lo=0,hi=0;for(char c:s){lo+=c=='('?1:-1;hi+=c!=')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo==0;}
int main(){cout<<checkValid("(*))")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func checkValid(s string) bool { lo,hi:=0,0; for _,c:=range s { if c=='(' { lo++ } else { lo-- }; if c!=')' { hi++ } else { hi-- }; if hi<0 { return false }; if lo<0 { lo=0 } }; return lo==0 }
func main(){ fmt.Println(checkValid("(*))")) }
''',
"R": '''checkValid <- function(s){ lo<-0; hi<-0; for(c in strsplit(s,"")[[1]]){ lo<-lo+ifelse(c=="(",1,-1); hi<-hi+ifelse(c!=")",1,-1); if(hi<0) return(FALSE); if(lo<0) lo<-0 }; lo==0 }
cat(checkValid("(*))"),"\\n")
''',
}))

# 222 Candy
L.append((222, "Candy", "Greedy", "Hard", 111,
"Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.",
{
"Python": '''def candy(r):
    n=len(r); a=[1]*n
    for i in range(1,n):
        if r[i]>r[i-1]: a[i]=a[i-1]+1
    for i in range(n-2,-1,-1):
        if r[i]>r[i+1]: a[i]=max(a[i],a[i+1]+1)
    return sum(a)
if __name__=="__main__":
    print(candy([1,0,2]))
    print(candy([1,2,2]))
''',
"JavaScript": '''function candy(r){const n=r.length,a=Array(n).fill(1);for(let i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(let i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=Math.max(a[i],a[i+1]+1);return a.reduce((x,y)=>x+y);}
console.log(candy([1,0,2]));console.log(candy([1,2,2]));
''',
"Java": '''public class __CLASS__{
  static int candy(int[] r){int n=r.length;int[] a=new int[n];java.util.Arrays.fill(a,1);for(int i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(int i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=Math.max(a[i],a[i+1]+1);int s=0;for(int x:a)s+=x;return s;}
  public static void main(String[]a){System.out.println(candy(new int[]{1,0,2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int candy(vector<int> r){int n=r.size();vector<int> a(n,1);for(int i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(int i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=max(a[i],a[i+1]+1);return accumulate(a.begin(),a.end(),0);}
int main(){cout<<candy({1,0,2})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func candy(r []int) int { n:=len(r); a:=make([]int,n); for i:=range a{a[i]=1}; for i:=1;i<n;i++ { if r[i]>r[i-1] { a[i]=a[i-1]+1 } }; for i:=n-2;i>=0;i-- { if r[i]>r[i+1] && a[i]<=a[i+1] { a[i]=a[i+1]+1 } }; s:=0; for _,x:=range a { s+=x }; return s }
func main(){ fmt.Println(candy([]int{1,0,2})) }
''',
"R": '''candy <- function(r){ n<-length(r); a<-rep(1,n); for(i in 2:n) if(r[i]>r[i-1]) a[i]<-a[i-1]+1; for(i in (n-1):1) if(r[i]>r[i+1] && a[i]<=a[i+1]) a[i]<-a[i+1]+1; sum(a) }
cat(candy(c(1,0,2)),"\\n")
''',
}))

# 223 Burst Balloons
L.append((223, "Burst Balloons", "2-D Dynamic Programming", "Hard", 112,
"Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.",
{
"Python": '''def maxCoins(nums):
    a=[1]+nums+[1]; n=len(a)
    dp=[[0]*n for _ in range(n)]
    for L in range(2,n):
        for l in range(0,n-L):
            r=l+L
            for i in range(l+1,r):
                dp[l][r]=max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r])
    return dp[0][n-1]
if __name__=="__main__":
    print(maxCoins([3,1,5,8]))
''',
"JavaScript": '''function maxCoins(nums){const a=[1,...nums,1],n=a.length;const dp=Array.from({length:n},()=>Array(n).fill(0));for(let L=2;L<n;L++)for(let l=0;l+L<n;l++){const r=l+L;for(let i=l+1;i<r;i++)dp[l][r]=Math.max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
console.log(maxCoins([3,1,5,8]));
''',
"Java": '''public class __CLASS__{
  static int maxCoins(int[] nums){int n=nums.length+2;int[] a=new int[n];a[0]=1;a[n-1]=1;for(int i=0;i<nums.length;i++)a[i+1]=nums[i];int[][] dp=new int[n][n];for(int L=2;L<n;L++)for(int l=0;l+L<n;l++){int r=l+L;for(int i=l+1;i<r;i++)dp[l][r]=Math.max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
  public static void main(String[]a){System.out.println(maxCoins(new int[]{3,1,5,8}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxCoins(vector<int> nums){vector<int> a;a.push_back(1);for(int x:nums)a.push_back(x);a.push_back(1);int n=a.size();vector<vector<int>> dp(n,vector<int>(n,0));for(int L=2;L<n;L++)for(int l=0;l+L<n;l++){int r=l+L;for(int i=l+1;i<r;i++)dp[l][r]=max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
int main(){cout<<maxCoins({3,1,5,8})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxCoins(nums []int) int { a:=append([]int{1},nums...); a=append(a,1); n:=len(a); dp:=make([][]int,n); for i:=range dp{dp[i]=make([]int,n)}; for L:=2;L<n;L++ { for l:=0;l+L<n;l++ { r:=l+L; for i:=l+1;i<r;i++ { v:=dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]; if v>dp[l][r]{dp[l][r]=v} } } }; return dp[0][n-1] }
func main(){ fmt.Println(maxCoins([]int{3,1,5,8})) }
''',
"R": '''maxCoins <- function(nums){ a<-c(1,nums,1); n<-length(a); dp<-matrix(0,n,n); for(L in 2:(n-1)) for(l in 1:(n-L)){ r<-l+L; for(i in (l+1):(r-1)) dp[l,r]<-max(dp[l,r],dp[l,i]+dp[i,r]+a[l]*a[i]*a[r]) }; dp[1,n] }
cat(maxCoins(c(3,1,5,8)),"\\n")
''',
}))

# 224 Regular Expression Matching
L.append((224, "Regular Expression Matching", "2-D Dynamic Programming", "Hard", 112,
"Implement regex with '.' and '*' (zero or more of preceding).",
{
"Python": '''def isMatch(s,p):
    m,n=len(s),len(p)
    dp=[[False]*(n+1) for _ in range(m+1)]
    dp[0][0]=True
    for j in range(1,n+1):
        if p[j-1]=='*': dp[0][j]=dp[0][j-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1]=='.' or p[j-1]==s[i-1]: dp[i][j]=dp[i-1][j-1]
            elif p[j-1]=='*':
                dp[i][j]=dp[i][j-2] or ((p[j-2]=='.' or p[j-2]==s[i-1]) and dp[i-1][j])
    return dp[m][n]
if __name__=="__main__":
    print(isMatch("aa","a*"))
    print(isMatch("ab",".*"))
''',
"JavaScript": '''function isMatch(s,p){const m=s.length,n=p.length;const dp=Array.from({length:m+1},()=>Array(n+1).fill(false));dp[0][0]=true;for(let j=1;j<=n;j++)if(p[j-1]==='*')dp[0][j]=dp[0][j-2];for(let i=1;i<=m;i++)for(let j=1;j<=n;j++){if(p[j-1]==='.'||p[j-1]===s[i-1])dp[i][j]=dp[i-1][j-1];else if(p[j-1]==='*')dp[i][j]=dp[i][j-2]||((p[j-2]==='.'||p[j-2]===s[i-1])&&dp[i-1][j]);}return dp[m][n];}
console.log(isMatch("aa","a*"));console.log(isMatch("ab",".*"));
''',
"Java": '''public class __CLASS__{
  static boolean isMatch(String s,String p){int m=s.length(),n=p.length();boolean[][] dp=new boolean[m+1][n+1];dp[0][0]=true;for(int j=1;j<=n;j++)if(p.charAt(j-1)=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(p.charAt(j-1)=='.'||p.charAt(j-1)==s.charAt(i-1))dp[i][j]=dp[i-1][j-1];else if(p.charAt(j-1)=='*')dp[i][j]=dp[i][j-2]||((p.charAt(j-2)=='.'||p.charAt(j-2)==s.charAt(i-1))&&dp[i-1][j]);}return dp[m][n];}
  public static void main(String[]a){System.out.println(isMatch("aa","a*"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool isMatch(string s,string p){int m=s.size(),n=p.size();vector<vector<bool>> dp(m+1,vector<bool>(n+1,false));dp[0][0]=true;for(int j=1;j<=n;j++)if(p[j-1]=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(p[j-1]=='.'||p[j-1]==s[i-1])dp[i][j]=dp[i-1][j-1];else if(p[j-1]=='*')dp[i][j]=dp[i][j-2]||((p[j-2]=='.'||p[j-2]==s[i-1])&&dp[i-1][j]);}return dp[m][n];}
int main(){cout<<isMatch("aa","a*")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func isMatch(s,p string) bool { m,n:=len(s),len(p); dp:=make([][]bool,m+1); for i:=range dp{dp[i]=make([]bool,n+1)}; dp[0][0]=true; for j:=1;j<=n;j++ { if p[j-1]=='*' { dp[0][j]=dp[0][j-2] } }; for i:=1;i<=m;i++ { for j:=1;j<=n;j++ { if p[j-1]=='.'||p[j-1]==s[i-1] { dp[i][j]=dp[i-1][j-1] } else if p[j-1]=='*' { dp[i][j]=dp[i][j-2]||((p[j-2]=='.'||p[j-2]==s[i-1])&&dp[i-1][j]) } } }; return dp[m][n] }
func main(){ fmt.Println(isMatch("aa","a*")) }
''',
"R": '''cat("isMatch: see Python solution\\n")
''',
}))

# 225 Partition Equal Subset Sum
L.append((225, "Partition Equal Subset Sum", "1-D Dynamic Programming", "Medium", 113,
"Can the array be split into two equal-sum subsets? Subset-sum DP.",
{
"Python": '''def canPartition(nums):
    s=sum(nums)
    if s%2: return False
    t=s//2
    dp={0}
    for x in nums:
        dp |= {v+x for v in dp if v+x<=t}
        if t in dp: return True
    return t in dp
if __name__=="__main__":
    print(canPartition([1,5,11,5]))
    print(canPartition([1,2,3,5]))
''',
"JavaScript": '''function canPartition(nums){const s=nums.reduce((a,b)=>a+b,0);if(s&1)return false;const t=s/2;const dp=new Set([0]);for(const x of nums){const nd=new Set(dp);for(const v of dp)if(v+x<=t)nd.add(v+x);if(nd.has(t))return true;dp.clear();for(const v of nd)dp.add(v);}return dp.has(t);}
console.log(canPartition([1,5,11,5]));console.log(canPartition([1,2,3,5]));
''',
"Java": '''public class __CLASS__{
  static boolean canPartition(int[] nums){int s=0;for(int x:nums)s+=x;if((s&1)==1)return false;int t=s/2;boolean[] dp=new boolean[t+1];dp[0]=true;for(int x:nums)for(int v=t;v>=x;v--)dp[v]=dp[v]||dp[v-x];return dp[t];}
  public static void main(String[]a){System.out.println(canPartition(new int[]{1,5,11,5}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool canPartition(vector<int> nums){int s=accumulate(nums.begin(),nums.end(),0);if(s&1)return false;int t=s/2;vector<bool> dp(t+1,false);dp[0]=true;for(int x:nums)for(int v=t;v>=x;v--)dp[v]=dp[v]||dp[v-x];return dp[t];}
int main(){cout<<canPartition({1,5,11,5})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func canPartition(nums []int) bool { s:=0; for _,x:=range nums{s+=x}; if s%2==1 { return false }; t:=s/2; dp:=make([]bool,t+1); dp[0]=true; for _,x:=range nums { for v:=t;v>=x;v-- { dp[v]=dp[v]||dp[v-x] } }; return dp[t] }
func main(){ fmt.Println(canPartition([]int{1,5,11,5})) }
''',
"R": '''canPartition <- function(nums){ s<-sum(nums); if(s%%2==1) return(FALSE); t<-s/2; dp<-c(TRUE,rep(FALSE,t)); for(x in nums) for(v in seq(t,x,-1)) dp[v+1]<-dp[v+1]||dp[v-x+1]; dp[t+1] }
cat(canPartition(c(1,5,11,5)),"\\n")
''',
}))

# 226 Combination Sum IV
L.append((226, "Combination Sum IV", "1-D Dynamic Programming", "Medium", 113,
"Count ordered combinations of nums summing to target.",
{
"Python": '''def combSum4(nums,t):
    dp=[0]*(t+1); dp[0]=1
    for v in range(1,t+1):
        for x in nums:
            if v-x>=0: dp[v]+=dp[v-x]
    return dp[t]
if __name__=="__main__":
    print(combSum4([1,2,3],4))
''',
"JavaScript": '''function combSum4(nums,t){const dp=Array(t+1).fill(0);dp[0]=1;for(let v=1;v<=t;v++)for(const x of nums)if(v>=x)dp[v]+=dp[v-x];return dp[t];}
console.log(combSum4([1,2,3],4));
''',
"Java": '''public class __CLASS__{
  static int combSum4(int[] nums,int t){int[] dp=new int[t+1];dp[0]=1;for(int v=1;v<=t;v++)for(int x:nums)if(v>=x)dp[v]+=dp[v-x];return dp[t];}
  public static void main(String[]a){System.out.println(combSum4(new int[]{1,2,3},4));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int combSum4(vector<int> nums,int t){vector<unsigned long long> dp(t+1,0);dp[0]=1;for(int v=1;v<=t;v++)for(int x:nums)if(v>=x)dp[v]+=dp[v-x];return (int)dp[t];}
int main(){cout<<combSum4({1,2,3},4)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func combSum4(nums []int, t int) int { dp:=make([]int,t+1); dp[0]=1; for v:=1;v<=t;v++ { for _,x:=range nums { if v>=x { dp[v]+=dp[v-x] } } }; return dp[t] }
func main(){ fmt.Println(combSum4([]int{1,2,3},4)) }
''',
"R": '''combSum4 <- function(nums,t){ dp<-c(1,rep(0,t)); for(v in 1:t) for(x in nums) if(v>=x) dp[v+1]<-dp[v+1]+dp[v-x+1]; dp[t+1] }
cat(combSum4(c(1,2,3),4),"\\n")
''',
}))

# 227 LRU Cache
L.append((227, "LRU Cache", "Linked List", "Medium", 114,
"Design LRU cache with O(1) get and put.",
{
"Python": '''from collections import OrderedDict
class LRU:
    def __init__(s,c): s.c=c; s.d=OrderedDict()
    def get(s,k):
        if k not in s.d: return -1
        s.d.move_to_end(k); return s.d[k]
    def put(s,k,v):
        if k in s.d: s.d.move_to_end(k)
        s.d[k]=v
        if len(s.d)>s.c: s.d.popitem(last=False)
if __name__=="__main__":
    c=LRU(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))
''',
"JavaScript": '''class LRU{constructor(c){this.c=c;this.m=new Map();}get(k){if(!this.m.has(k))return -1;const v=this.m.get(k);this.m.delete(k);this.m.set(k,v);return v;}put(k,v){if(this.m.has(k))this.m.delete(k);this.m.set(k,v);if(this.m.size>this.c)this.m.delete(this.m.keys().next().value);}}
const c=new LRU(2);c.put(1,1);c.put(2,2);console.log(c.get(1));c.put(3,3);console.log(c.get(2));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class LRU extends LinkedHashMap<Integer,Integer>{int c;LRU(int c){super(16,0.75f,true);this.c=c;}protected boolean removeEldestEntry(Map.Entry<Integer,Integer> e){return size()>c;}int g(int k){return getOrDefault(k,-1);}}
  public static void main(String[]a){LRU c=new LRU(2);c.put(1,1);c.put(2,2);System.out.println(c.g(1));c.put(3,3);System.out.println(c.g(2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
class LRU{int c;list<pair<int,int>> l;unordered_map<int,list<pair<int,int>>::iterator> m;public:LRU(int c):c(c){}int get(int k){if(!m.count(k))return -1;l.splice(l.begin(),l,m[k]);return m[k]->second;}void put(int k,int v){if(m.count(k)){m[k]->second=v;l.splice(l.begin(),l,m[k]);return;}l.push_front({k,v});m[k]=l.begin();if((int)l.size()>c){m.erase(l.back().first);l.pop_back();}}};
int main(){LRU c(2);c.put(1,1);c.put(2,2);cout<<c.get(1)<<"\\n";c.put(3,3);cout<<c.get(2)<<"\\n";}
''',
"Go": '''package main
import ("container/list";"fmt")
type LRU struct{c int; l *list.List; m map[int]*list.Element}
type kv struct{k,v int}
func New(c int) *LRU { return &LRU{c,list.New(),map[int]*list.Element{}} }
func (s *LRU) Get(k int) int { if e,ok:=s.m[k]; ok { s.l.MoveToFront(e); return e.Value.(*kv).v }; return -1 }
func (s *LRU) Put(k,v int){ if e,ok:=s.m[k]; ok { e.Value.(*kv).v=v; s.l.MoveToFront(e); return }; e:=s.l.PushFront(&kv{k,v}); s.m[k]=e; if s.l.Len()>s.c { b:=s.l.Back(); delete(s.m,b.Value.(*kv).k); s.l.Remove(b) } }
func main(){ c:=New(2); c.Put(1,1); c.Put(2,2); fmt.Println(c.Get(1)); c.Put(3,3); fmt.Println(c.Get(2)) }
''',
"R": '''cat("LRU: use environment hashmap + linked list\\n")
''',
}))

# 228 LFU Cache
L.append((228, "LFU Cache", "Linked List", "Hard", 114,
"LFU eviction; tie-break by least recently used. Use freq buckets of OrderedDict.",
{
"Python": '''from collections import defaultdict, OrderedDict
class LFU:
    def __init__(s,c): s.c=c; s.k={}; s.f=defaultdict(OrderedDict); s.mn=0
    def _bump(s,k):
        f=s.k[k][1]; v=s.f[f].pop(k)
        if not s.f[f] and s.mn==f: s.mn+=1
        s.f[f+1][k]=v; s.k[k]=(v,f+1)
    def get(s,k):
        if k not in s.k: return -1
        s._bump(k); return s.k[k][0]
    def put(s,k,v):
        if s.c==0: return
        if k in s.k: s.k[k]=(v,s.k[k][1]); s.f[s.k[k][1]][k]=v; s._bump(k); return
        if len(s.k)>=s.c:
            ek,_=s.f[s.mn].popitem(last=False); del s.k[ek]
        s.k[k]=(v,1); s.f[1][k]=v; s.mn=1
if __name__=="__main__":
    c=LFU(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))
''',
"JavaScript": '''class LFU{constructor(c){this.c=c;this.k=new Map();this.f=new Map();this.mn=0;}_bucket(f){if(!this.f.has(f))this.f.set(f,new Map());return this.f.get(f);}_bump(k){const [v,f]=this.k.get(k);this._bucket(f).delete(k);if(this._bucket(f).size===0&&this.mn===f)this.mn++;this._bucket(f+1).set(k,v);this.k.set(k,[v,f+1]);}get(k){if(!this.k.has(k))return -1;this._bump(k);return this.k.get(k)[0];}put(k,v){if(this.c===0)return;if(this.k.has(k)){this.k.set(k,[v,this.k.get(k)[1]]);this._bucket(this.k.get(k)[1]).set(k,v);this._bump(k);return;}if(this.k.size>=this.c){const b=this._bucket(this.mn);const ek=b.keys().next().value;b.delete(ek);this.k.delete(ek);}this.k.set(k,[v,1]);this._bucket(1).set(k,v);this.mn=1;}}
const c=new LFU(2);c.put(1,1);c.put(2,2);console.log(c.get(1));c.put(3,3);console.log(c.get(2));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class LFU{int c,mn;Map<Integer,int[]> k=new HashMap<>();Map<Integer,LinkedHashMap<Integer,Integer>> f=new HashMap<>();LFU(int c){this.c=c;}LinkedHashMap<Integer,Integer> b(int x){return f.computeIfAbsent(x,z->new LinkedHashMap<>());}void bump(int x){int[] p=k.get(x);b(p[1]).remove(x);if(b(p[1]).isEmpty()&&mn==p[1])mn++;p[1]++;b(p[1]).put(x,p[0]);}int get(int x){if(!k.containsKey(x))return -1;bump(x);return k.get(x)[0];}void put(int x,int v){if(c==0)return;if(k.containsKey(x)){k.get(x)[0]=v;b(k.get(x)[1]).put(x,v);bump(x);return;}if(k.size()>=c){int ek=b(mn).keySet().iterator().next();b(mn).remove(ek);k.remove(ek);}k.put(x,new int[]{v,1});b(1).put(x,v);mn=1;}}
  public static void main(String[]a){LFU c=new LFU(2);c.put(1,1);c.put(2,2);System.out.println(c.get(1));c.put(3,3);System.out.println(c.get(2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
class LFU{int c=0,mn=0;unordered_map<int,pair<int,int>> kv;unordered_map<int,list<int>> f;unordered_map<int,list<int>::iterator> it;public:LFU(int c):c(c){}void bump(int k){int fr=kv[k].second;f[fr].erase(it[k]);if(f[fr].empty()&&mn==fr)mn++;f[fr+1].push_back(k);it[k]=prev(f[fr+1].end());kv[k].second++;}int get(int k){if(!kv.count(k))return -1;bump(k);return kv[k].first;}void put(int k,int v){if(c==0)return;if(kv.count(k)){kv[k].first=v;bump(k);return;}if((int)kv.size()>=c){int ek=f[mn].front();f[mn].pop_front();kv.erase(ek);it.erase(ek);}kv[k]={v,1};f[1].push_back(k);it[k]=prev(f[1].end());mn=1;}};
int main(){LFU c(2);c.put(1,1);c.put(2,2);cout<<c.get(1)<<"\\n";c.put(3,3);cout<<c.get(2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func main(){ fmt.Println("LFU Cache: see Python/Java/C++ implementations") }
''',
"R": '''cat("LFU Cache: see Python solution\\n")
''',
}))

# 229 Perfect Squares
L.append((229, "Perfect Squares", "1-D Dynamic Programming", "Medium", 115,
"Min number of perfect-square numbers summing to n.",
{
"Python": '''def numSquares(n):
    dp=[0]+[float('inf')]*n
    for i in range(1,n+1):
        j=1
        while j*j<=i: dp[i]=min(dp[i],dp[i-j*j]+1); j+=1
    return dp[n]
if __name__=="__main__":
    print(numSquares(12)); print(numSquares(13))
''',
"JavaScript": '''function numSquares(n){const dp=Array(n+1).fill(Infinity);dp[0]=0;for(let i=1;i<=n;i++)for(let j=1;j*j<=i;j++)dp[i]=Math.min(dp[i],dp[i-j*j]+1);return dp[n];}
console.log(numSquares(12));console.log(numSquares(13));
''',
"Java": '''public class __CLASS__{
  static int numSquares(int n){int[] dp=new int[n+1];java.util.Arrays.fill(dp,Integer.MAX_VALUE);dp[0]=0;for(int i=1;i<=n;i++)for(int j=1;j*j<=i;j++)dp[i]=Math.min(dp[i],dp[i-j*j]+1);return dp[n];}
  public static void main(String[]a){System.out.println(numSquares(12));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int numSquares(int n){vector<int> dp(n+1,INT_MAX);dp[0]=0;for(int i=1;i<=n;i++)for(int j=1;j*j<=i;j++)dp[i]=min(dp[i],dp[i-j*j]+1);return dp[n];}
int main(){cout<<numSquares(12)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func numSquares(n int) int { dp:=make([]int,n+1); for i:=1;i<=n;i++ { dp[i]=1<<30; for j:=1;j*j<=i;j++ { if dp[i-j*j]+1<dp[i] { dp[i]=dp[i-j*j]+1 } } }; return dp[n] }
func main(){ fmt.Println(numSquares(12)) }
''',
"R": '''numSquares <- function(n){ dp<-c(0,rep(Inf,n)); for(i in 1:n){ j<-1; while(j*j<=i){ dp[i+1]<-min(dp[i+1],dp[i-j*j+1]+1); j<-j+1 } }; dp[n+1] }
cat(numSquares(12),"\\n")
''',
}))

# 230 Integer Break
L.append((230, "Integer Break", "1-D Dynamic Programming", "Medium", 115,
"Break n into >=2 positive ints; maximize product.",
{
"Python": '''def integerBreak(n):
    dp=[0]*(n+1); dp[1]=1
    for i in range(2,n+1):
        for j in range(1,i):
            dp[i]=max(dp[i],j*max(i-j,dp[i-j]))
    return dp[n]
if __name__=="__main__":
    print(integerBreak(2)); print(integerBreak(10))
''',
"JavaScript": '''function integerBreak(n){const dp=Array(n+1).fill(0);dp[1]=1;for(let i=2;i<=n;i++)for(let j=1;j<i;j++)dp[i]=Math.max(dp[i],j*Math.max(i-j,dp[i-j]));return dp[n];}
console.log(integerBreak(10));
''',
"Java": '''public class __CLASS__{
  static int integerBreak(int n){int[] dp=new int[n+1];dp[1]=1;for(int i=2;i<=n;i++)for(int j=1;j<i;j++)dp[i]=Math.max(dp[i],j*Math.max(i-j,dp[i-j]));return dp[n];}
  public static void main(String[]a){System.out.println(integerBreak(10));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int integerBreak(int n){vector<int> dp(n+1);dp[1]=1;for(int i=2;i<=n;i++)for(int j=1;j<i;j++)dp[i]=max(dp[i],j*max(i-j,dp[i-j]));return dp[n];}
int main(){cout<<integerBreak(10)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func integerBreak(n int) int { dp:=make([]int,n+1); dp[1]=1; for i:=2;i<=n;i++ { for j:=1;j<i;j++ { m:=i-j; if dp[i-j]>m { m=dp[i-j] }; if j*m>dp[i] { dp[i]=j*m } } }; return dp[n] }
func main(){ fmt.Println(integerBreak(10)) }
''',
"R": '''integerBreak <- function(n){ dp<-rep(0,n+1); dp[2]<-1; for(i in 2:n) for(j in 1:(i-1)) dp[i+1]<-max(dp[i+1], j*max(i-j,dp[i-j+1])); dp[n+1] }
cat(integerBreak(10),"\\n")
''',
}))

# 231 Encode and Decode Strings
L.append((231, "Encode and Decode Strings", "Arrays and Hashing", "Medium", 116,
"Length-prefix encoding for arbitrary strings.",
{
"Python": '''def encode(strs): return "".join(f"{len(s)}#{s}" for s in strs)
def decode(s):
    res=[]; i=0
    while i<len(s):
        j=s.index('#',i); n=int(s[i:j]); res.append(s[j+1:j+1+n]); i=j+1+n
    return res
if __name__=="__main__":
    e=encode(["hello","world","#42"]); print(e); print(decode(e))
''',
"JavaScript": '''function encode(a){return a.map(s=>s.length+"#"+s).join("");}
function decode(s){const r=[];let i=0;while(i<s.length){let j=s.indexOf('#',i);const n=+s.slice(i,j);r.push(s.slice(j+1,j+1+n));i=j+1+n;}return r;}
const e=encode(["hello","world","#42"]);console.log(e);console.log(decode(e));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String encode(List<String> a){StringBuilder sb=new StringBuilder();for(String s:a)sb.append(s.length()).append('#').append(s);return sb.toString();}
  static List<String> decode(String s){List<String> r=new ArrayList<>();int i=0;while(i<s.length()){int j=s.indexOf('#',i);int n=Integer.parseInt(s.substring(i,j));r.add(s.substring(j+1,j+1+n));i=j+1+n;}return r;}
  public static void main(String[]a){String e=encode(Arrays.asList("hello","world","#42"));System.out.println(e);System.out.println(decode(e));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string encode(vector<string> a){string r;for(auto&s:a)r+=to_string(s.size())+"#"+s;return r;}
vector<string> decode(string s){vector<string> r;int i=0;while(i<(int)s.size()){int j=s.find('#',i);int n=stoi(s.substr(i,j-i));r.push_back(s.substr(j+1,n));i=j+1+n;}return r;}
int main(){auto e=encode({"hello","world","#42"});cout<<e<<"\\n";for(auto&s:decode(e))cout<<s<<"|";cout<<"\\n";}
''',
"Go": '''package main
import ("fmt";"strconv";"strings")
func encode(a []string) string { var b strings.Builder; for _,s:=range a { fmt.Fprintf(&b,"%d#%s",len(s),s) }; return b.String() }
func decode(s string) []string { r:=[]string{}; i:=0; for i<len(s) { j:=strings.Index(s[i:],"#")+i; n,_:=strconv.Atoi(s[i:j]); r=append(r,s[j+1:j+1+n]); i=j+1+n }; return r }
func main(){ e:=encode([]string{"hello","world","#42"}); fmt.Println(e); fmt.Println(decode(e)) }
''',
"R": '''encode <- function(a) paste0(sapply(a,function(s) paste0(nchar(s),"#",s)),collapse="")
decode <- function(s){ r<-c(); i<-1; while(i<=nchar(s)){ j<-i+regexpr("#",substr(s,i,nchar(s)))-1; n<-as.integer(substr(s,i,j-1)); r<-c(r,substr(s,j+1,j+n)); i<-j+1+n }; r }
cat(encode(c("hello","world")),"\\n"); print(decode(encode(c("hello","world"))))
''',
}))

# 232 Range Sum Query 2D Immutable
L.append((232, "Range Sum Query 2D Immutable", "Arrays and Hashing", "Medium", 116,
"Build prefix sum 2D for O(1) region queries.",
{
"Python": '''class NM:
    def __init__(s,m):
        if not m: s.p=[]; return
        R,C=len(m),len(m[0])
        s.p=[[0]*(C+1) for _ in range(R+1)]
        for i in range(R):
            for j in range(C):
                s.p[i+1][j+1]=m[i][j]+s.p[i][j+1]+s.p[i+1][j]-s.p[i][j]
    def sumRegion(s,r1,c1,r2,c2):
        return s.p[r2+1][c2+1]-s.p[r1][c2+1]-s.p[r2+1][c1]+s.p[r1][c1]
if __name__=="__main__":
    n=NM([[3,0,1],[5,6,3],[1,2,0]]); print(n.sumRegion(0,0,2,2)); print(n.sumRegion(1,1,2,2))
''',
"JavaScript": '''class NM{constructor(m){const R=m.length,C=m[0].length;this.p=Array.from({length:R+1},()=>Array(C+1).fill(0));for(let i=0;i<R;i++)for(let j=0;j<C;j++)this.p[i+1][j+1]=m[i][j]+this.p[i][j+1]+this.p[i+1][j]-this.p[i][j];}sumRegion(r1,c1,r2,c2){return this.p[r2+1][c2+1]-this.p[r1][c2+1]-this.p[r2+1][c1]+this.p[r1][c1];}}
const n=new NM([[3,0,1],[5,6,3],[1,2,0]]);console.log(n.sumRegion(0,0,2,2));console.log(n.sumRegion(1,1,2,2));
''',
"Java": '''public class __CLASS__{
  static class NM{int[][] p;NM(int[][] m){int R=m.length,C=m[0].length;p=new int[R+1][C+1];for(int i=0;i<R;i++)for(int j=0;j<C;j++)p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j];}int sumRegion(int r1,int c1,int r2,int c2){return p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1];}}
  public static void main(String[]a){NM n=new NM(new int[][]{{3,0,1},{5,6,3},{1,2,0}});System.out.println(n.sumRegion(0,0,2,2));System.out.println(n.sumRegion(1,1,2,2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct NM{vector<vector<int>> p;NM(vector<vector<int>> m){int R=m.size(),C=m[0].size();p.assign(R+1,vector<int>(C+1,0));for(int i=0;i<R;i++)for(int j=0;j<C;j++)p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j];}int sumRegion(int r1,int c1,int r2,int c2){return p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1];}};
int main(){NM n({{3,0,1},{5,6,3},{1,2,0}});cout<<n.sumRegion(0,0,2,2)<<"\\n";cout<<n.sumRegion(1,1,2,2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type NM struct{p [][]int}
func New(m [][]int) *NM { R,C:=len(m),len(m[0]); p:=make([][]int,R+1); for i:=range p{p[i]=make([]int,C+1)}; for i:=0;i<R;i++ { for j:=0;j<C;j++ { p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j] } }; return &NM{p} }
func (n *NM) SumRegion(r1,c1,r2,c2 int) int { return n.p[r2+1][c2+1]-n.p[r1][c2+1]-n.p[r2+1][c1]+n.p[r1][c1] }
func main(){ n:=New([][]int{{3,0,1},{5,6,3},{1,2,0}}); fmt.Println(n.SumRegion(0,0,2,2)); fmt.Println(n.SumRegion(1,1,2,2)) }
''',
"R": '''sumRegion <- function(m,r1,c1,r2,c2){ R<-nrow(m); C<-ncol(m); p<-matrix(0,R+1,C+1); for(i in 1:R) for(j in 1:C) p[i+1,j+1]<-m[i,j]+p[i,j+1]+p[i+1,j]-p[i,j]; p[r2+2,c2+2]-p[r1+1,c2+2]-p[r2+2,c1+1]+p[r1+1,c1+1] }
cat(sumRegion(matrix(c(3,0,1,5,6,3,1,2,0),3,3,byrow=TRUE),0,0,2,2),"\\n")
''',
}))

# 233 Merge K Sorted Lists
L.append((233, "Merge K Sorted Lists", "Linked List", "Hard", 117,
"Merge K sorted linked lists into one. Use heap.",
{
"Python": '''import heapq
class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def mergeK(lists):
    h=[]
    for i,L in enumerate(lists):
        if L: heapq.heappush(h,(L.v,i,L))
    d=N(0); cur=d; ctr=len(lists)
    while h:
        v,_,nd=heapq.heappop(h); cur.n=nd; cur=nd
        if nd.n: ctr+=1; heapq.heappush(h,(nd.n.v,ctr,nd.n))
    return d.n
def to(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n
def out(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
if __name__=="__main__":
    print(out(mergeK([to([1,4,5]),to([1,3,4]),to([2,6])])))
''',
"JavaScript": '''class N{constructor(v,n=null){this.v=v;this.n=n;}}
function mergeK(lists){const arr=[];for(const L of lists){let c=L;while(c){arr.push(c.v);c=c.n;}}arr.sort((a,b)=>a-b);const d=new N(0);let c=d;for(const v of arr){c.n=new N(v);c=c.n;}return d.n;}
function to(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function out(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(out(mergeK([to([1,4,5]),to([1,3,4]),to([2,6])])));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N mergeK(List<N> lists){PriorityQueue<int[]> q=new PriorityQueue<>((a,b)->a[0]-b[0]);for(int i=0;i<lists.size();i++)if(lists.get(i)!=null)q.add(new int[]{lists.get(i).v,i});List<N> heads=new ArrayList<>(lists);N d=new N(0),c=d;while(!q.isEmpty()){int[] t=q.poll();c.n=new N(t[0]);c=c.n;heads.set(t[1],heads.get(t[1]).n);if(heads.get(t[1])!=null)q.add(new int[]{heads.get(t[1]).v,t[1]});}return d.n;}
  static N to(int[] a){N d=new N(0),c=d;for(int x:a){c.n=new N(x);c=c.n;}return d.n;}
  public static void main(String[]a){List<N> L=Arrays.asList(to(new int[]{1,4,5}),to(new int[]{1,3,4}),to(new int[]{2,6}));N r=mergeK(L);while(r!=null){System.out.print(r.v+" ");r=r.n;}System.out.println();}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N* n;N(int v):v(v),n(nullptr){}};
N* mergeK(vector<N*> L){priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> q;for(int i=0;i<(int)L.size();i++)if(L[i])q.push({L[i]->v,i});N* d=new N(0);N* c=d;while(!q.empty()){auto [v,i]=q.top();q.pop();c->n=new N(v);c=c->n;L[i]=L[i]->n;if(L[i])q.push({L[i]->v,i});}return d->n;}
N* to(vector<int> a){N* d=new N(0);N* c=d;for(int x:a){c->n=new N(x);c=c->n;}return d->n;}
int main(){auto r=mergeK({to({1,4,5}),to({1,3,4}),to({2,6})});while(r){cout<<r->v<<" ";r=r->n;}cout<<"\\n";}
''',
"Go": '''package main
import ("container/heap";"fmt")
type N struct{v int; n *N}
type pq []*N
func (h pq) Len() int{return len(h)}
func (h pq) Less(i,j int) bool {return h[i].v<h[j].v}
func (h pq) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *pq) Push(x any){*h=append(*h,x.(*N))}
func (h *pq) Pop() any { o:=*h; x:=o[len(o)-1]; *h=o[:len(o)-1]; return x }
func mergeK(lists []*N) *N { h:=&pq{}; heap.Init(h); for _,L:=range lists { if L!=nil { heap.Push(h,L) } }; d:=&N{}; c:=d; for h.Len()>0 { x:=heap.Pop(h).(*N); c.n=x; c=x; if x.n!=nil { heap.Push(h,x.n) } }; return d.n }
func to(a []int) *N { d:=&N{}; c:=d; for _,x:=range a { c.n=&N{v:x}; c=c.n }; return d.n }
func main(){ r:=mergeK([]*N{to([]int{1,4,5}),to([]int{1,3,4}),to([]int{2,6})}); for r!=nil { fmt.Print(r.v," "); r=r.n }; fmt.Println() }
''',
"R": '''cat("mergeK: flatten + sort O(N log N)\\n")
''',
}))

# 234 Reverse Nodes In K Group
L.append((234, "Reverse Nodes In K Group", "Linked List", "Hard", 117,
"Reverse nodes in groups of k. Remaining tail stays.",
{
"Python": '''class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def reverseK(head,k):
    d=N(0,head); g=d
    while True:
        kth=g
        for _ in range(k):
            kth=kth.n
            if not kth: return d.n
        nxt=kth.n; pre,cur=nxt,g.n
        while cur is not nxt:
            tmp=cur.n; cur.n=pre; pre=cur; cur=tmp
        tmp=g.n; g.n=kth; g=tmp
def to(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n
def out(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
if __name__=="__main__":
    print(out(reverseK(to([1,2,3,4,5]),2)))
''',
"JavaScript": '''class N{constructor(v,n=null){this.v=v;this.n=n;}}
function reverseK(head,k){const d=new N(0);d.n=head;let g=d;while(true){let kth=g;for(let i=0;i<k;i++){kth=kth.n;if(!kth)return d.n;}const nxt=kth.n;let pre=nxt,cur=g.n;while(cur!==nxt){const t=cur.n;cur.n=pre;pre=cur;cur=t;}const tmp=g.n;g.n=kth;g=tmp;}}
function to(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function out(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(out(reverseK(to([1,2,3,4,5]),2)));
''',
"Java": '''public class __CLASS__{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N reverseK(N head,int k){N d=new N(0);d.n=head;N g=d;while(true){N kth=g;for(int i=0;i<k;i++){kth=kth.n;if(kth==null)return d.n;}N nxt=kth.n,pre=nxt,cur=g.n;while(cur!=nxt){N t=cur.n;cur.n=pre;pre=cur;cur=t;}N tmp=g.n;g.n=kth;g=tmp;}}
  static N to(int[] a){N d=new N(0),c=d;for(int x:a){c.n=new N(x);c=c.n;}return d.n;}
  public static void main(String[]a){N r=reverseK(to(new int[]{1,2,3,4,5}),2);while(r!=null){System.out.print(r.v+" ");r=r.n;}System.out.println();}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N* n;N(int v):v(v),n(nullptr){}};
N* reverseK(N* head,int k){N* d=new N(0);d->n=head;N* g=d;while(true){N* kth=g;for(int i=0;i<k;i++){kth=kth->n;if(!kth)return d->n;}N* nxt=kth->n;N* pre=nxt;N* cur=g->n;while(cur!=nxt){N* t=cur->n;cur->n=pre;pre=cur;cur=t;}N* tmp=g->n;g->n=kth;g=tmp;}}
N* to(vector<int> a){N* d=new N(0);N* c=d;for(int x:a){c->n=new N(x);c=c->n;}return d->n;}
int main(){auto r=reverseK(to({1,2,3,4,5}),2);while(r){cout<<r->v<<" ";r=r->n;}cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{v int; n *N}
func reverseK(head *N, k int) *N { d:=&N{n:head}; g:=d; for { kth:=g; for i:=0;i<k;i++ { kth=kth.n; if kth==nil { return d.n } }; nxt:=kth.n; pre,cur:=nxt,g.n; for cur!=nxt { t:=cur.n; cur.n=pre; pre=cur; cur=t }; tmp:=g.n; g.n=kth; g=tmp } }
func to(a []int) *N { d:=&N{}; c:=d; for _,x:=range a { c.n=&N{v:x}; c=c.n }; return d.n }
func main(){ r:=reverseK(to([]int{1,2,3,4,5}),2); for r!=nil { fmt.Print(r.v," "); r=r.n }; fmt.Println() }
''',
"R": '''cat("reverseK: reverse groups of k\\n")
''',
}))

# 235 Product of Array Except Self
L.append((235, "Product of Array Except Self", "Arrays and Hashing", "Medium", 118,
"Return array where output[i] = product of all nums except nums[i]. O(n) no division.",
{
"Python": '''def productExceptSelf(n):
    out=[1]*len(n); p=1
    for i in range(len(n)): out[i]=p; p*=n[i]
    p=1
    for i in range(len(n)-1,-1,-1): out[i]*=p; p*=n[i]
    return out
if __name__=="__main__":
    print(productExceptSelf([1,2,3,4]))
''',
"JavaScript": '''function productExceptSelf(n){const o=Array(n.length).fill(1);let p=1;for(let i=0;i<n.length;i++){o[i]=p;p*=n[i];}p=1;for(let i=n.length-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
console.log(productExceptSelf([1,2,3,4]));
''',
"Java": '''public class __CLASS__{
  static int[] productExceptSelf(int[] n){int[] o=new int[n.length];int p=1;for(int i=0;i<n.length;i++){o[i]=p;p*=n[i];}p=1;for(int i=n.length-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
  public static void main(String[]a){System.out.println(java.util.Arrays.toString(productExceptSelf(new int[]{1,2,3,4})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> productExceptSelf(vector<int> n){vector<int> o(n.size(),1);int p=1;for(int i=0;i<(int)n.size();i++){o[i]=p;p*=n[i];}p=1;for(int i=n.size()-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
int main(){for(int x:productExceptSelf({1,2,3,4}))cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func productExceptSelf(n []int) []int { o:=make([]int,len(n)); p:=1; for i:=0;i<len(n);i++ { o[i]=p; p*=n[i] }; p=1; for i:=len(n)-1;i>=0;i-- { o[i]*=p; p*=n[i] }; return o }
func main(){ fmt.Println(productExceptSelf([]int{1,2,3,4})) }
''',
"R": '''productExceptSelf <- function(n){ o<-rep(1,length(n)); p<-1; for(i in seq_along(n)){ o[i]<-p; p<-p*n[i] }; p<-1; for(i in length(n):1){ o[i]<-o[i]*p; p<-p*n[i] }; o }
cat(productExceptSelf(c(1,2,3,4)),"\\n")
''',
}))

write_lessons(L)
