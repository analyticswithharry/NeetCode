"""Batch 4: NeetCode lessons 61-85 with embedded question + working solution."""
from _lesson_writer import write_lessons

LESSONS = []

# ---- 061 Contains Duplicate ----
LESSONS.append((61, "Contains Duplicate", "Arrays and Hashing", "Easy", 31,
"""Given an integer array nums, return true if any value appears at least twice.

Example: [1,2,3,1] -> true; [1,2,3,4] -> false""",
{
"Python":'''
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

if __name__ == "__main__":
    print(Solution().containsDuplicate([1,2,3,1]))
    print(Solution().containsDuplicate([1,2,3,4]))
''',
"JavaScript":'''
var containsDuplicate = function(nums){ return new Set(nums).size !== nums.length; };
console.log(containsDuplicate([1,2,3,1]), containsDuplicate([1,2,3,4]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean containsDuplicate(int[] nums){
        Set<Integer> s = new HashSet<>();
        for (int n: nums) if (!s.add(n)) return true;
        return false;
    }
    public static void main(String[] a){
        __CLASS__ x = new __CLASS__();
        System.out.println(x.containsDuplicate(new int[]{1,2,3,1}));
        System.out.println(x.containsDuplicate(new int[]{1,2,3,4}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    bool containsDuplicate(vector<int>& nums){
        unordered_set<int> s;
        for (int n: nums) if (!s.insert(n).second) return true;
        return false;
    }
};
int main(){ vector<int> a={1,2,3,1}, b={1,2,3,4};
    cout<<Solution().containsDuplicate(a)<<" "<<Solution().containsDuplicate(b)<<endl; }
''',
"Go":'''
package main
import "fmt"
func containsDuplicate(nums []int) bool {
    m := map[int]bool{}
    for _,n := range nums { if m[n] { return true }; m[n]=true }
    return false
}
func main(){ fmt.Println(containsDuplicate([]int{1,2,3,1}), containsDuplicate([]int{1,2,3,4})) }
''',
"R":'''
containsDuplicate <- function(nums) length(unique(nums)) != length(nums)
print(containsDuplicate(c(1,2,3,1)))
print(containsDuplicate(c(1,2,3,4)))
''',
}))

# ---- 062 Valid Sudoku ----
LESSONS.append((62, "Valid Sudoku", "Arrays and Hashing", "Medium", 31,
"""Determine if a 9x9 Sudoku board is valid (no duplicates in any row, column, or 3x3 box). Empty cells are '.'.""",
{
"Python":'''
class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".": continue
                items = [(v,"r",i),(v,"c",j),(v,"b",i//3,j//3)]
                for it in items:
                    if it in seen: return False
                    seen.add(it)
        return True

if __name__ == "__main__":
    b = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(b))
''',
"JavaScript":'''
var isValidSudoku = function(board){
    const seen = new Set();
    for (let i=0;i<9;i++) for (let j=0;j<9;j++){
        const v = board[i][j]; if (v===".") continue;
        const k = [`r${i}${v}`, `c${j}${v}`, `b${(i/3|0)}${(j/3|0)}${v}`];
        for (const x of k){ if (seen.has(x)) return false; seen.add(x); }
    }
    return true;
};
const b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]];
console.log(isValidSudoku(b));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean isValidSudoku(char[][] b){
        Set<String> s = new HashSet<>();
        for (int i=0;i<9;i++) for (int j=0;j<9;j++){
            char v = b[i][j]; if (v=='.') continue;
            if (!s.add("r"+i+v) || !s.add("c"+j+v) || !s.add("b"+(i/3)+(j/3)+v)) return false;
        }
        return true;
    }
    public static void main(String[] a){
        char[][] b = {
            {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}};
        System.out.println(new __CLASS__().isValidSudoku(b));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    bool isValidSudoku(vector<vector<char>>& b){
        set<string> s;
        for (int i=0;i<9;i++) for (int j=0;j<9;j++){
            char v=b[i][j]; if (v=='.') continue;
            string r="r"+to_string(i)+v, c="c"+to_string(j)+v, x="b"+to_string(i/3)+to_string(j/3)+v;
            if (!s.insert(r).second || !s.insert(c).second || !s.insert(x).second) return false;
        }
        return true;
    }
};
int main(){
    vector<vector<char>> b = {
        {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}};
    cout<<Solution().isValidSudoku(b)<<endl;
}
''',
"Go":'''
package main
import "fmt"
func isValidSudoku(b [][]byte) bool {
    s := map[string]bool{}
    for i:=0;i<9;i++ { for j:=0;j<9;j++ {
        v := b[i][j]; if v=='.' { continue }
        keys := []string{ fmt.Sprintf("r%d%c",i,v), fmt.Sprintf("c%d%c",j,v), fmt.Sprintf("b%d%d%c",i/3,j/3,v) }
        for _,k := range keys { if s[k] { return false }; s[k]=true }
    }}
    return true
}
func main(){
    b := [][]byte{
        {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}}
    fmt.Println(isValidSudoku(b))
}
''',
"R":'''
isValidSudoku <- function(b){
    seen <- c()
    for (i in 1:9) for (j in 1:9){
        v <- b[i,j]; if (v==".") next
        keys <- c(paste0("r",i,v), paste0("c",j,v), paste0("b",(i-1)%/%3,(j-1)%/%3,v))
        if (any(keys %in% seen)) return(FALSE)
        seen <- c(seen, keys)
    }
    TRUE
}
b <- matrix(c("5","3",".",".","7",".",".",".",".",
              "6",".",".","1","9","5",".",".",".",
              ".","9","8",".",".",".",".","6",".",
              "8",".",".",".","6",".",".",".","3",
              "4",".",".","8",".","3",".",".","1",
              "7",".",".",".","2",".",".",".","6",
              ".","6",".",".",".",".","2","8",".",
              ".",".",".","4","1","9",".",".","5",
              ".",".",".",".","8",".",".","7","9"), nrow=9, byrow=TRUE)
print(isValidSudoku(b))
''',
}))

# ---- 063 Encode and Decode Strings ----
LESSONS.append((63, "Encode and Decode Strings", "Arrays and Hashing", "Medium", 32,
"""Design encode/decode of a list of strings into one string and back.

Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).""",
{
"Python":'''
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
''',
"JavaScript":'''
const encode = strs => strs.map(s => s.length + "#" + s).join("");
const decode = s => { const out=[]; let i=0;
    while (i < s.length){ const j=s.indexOf("#",i); const n=+s.slice(i,j);
        out.push(s.slice(j+1,j+1+n)); i = j+1+n; } return out; };
const e = encode(["lint","code","love","you"]); console.log(e); console.log(decode(e));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public String encode(List<String> strs){
        StringBuilder sb = new StringBuilder();
        for (String s: strs) sb.append(s.length()).append('#').append(s);
        return sb.toString();
    }
    public List<String> decode(String s){
        List<String> out = new ArrayList<>(); int i=0;
        while (i < s.length()){ int j = s.indexOf('#', i); int n = Integer.parseInt(s.substring(i,j));
            out.add(s.substring(j+1, j+1+n)); i = j+1+n; }
        return out;
    }
    public static void main(String[] a){
        __CLASS__ c = new __CLASS__();
        String e = c.encode(Arrays.asList("lint","code","love","you"));
        System.out.println(e); System.out.println(c.decode(e));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Codec { public:
    string encode(vector<string>& strs){ string r; for (auto& s: strs) r += to_string(s.size())+"#"+s; return r; }
    vector<string> decode(string s){ vector<string> out; size_t i=0;
        while (i < s.size()){ size_t j = s.find('#', i); int n = stoi(s.substr(i, j-i));
            out.push_back(s.substr(j+1, n)); i = j+1+n; } return out; }
};
int main(){ vector<string> v={"lint","code","love","you"}; Codec c; auto e=c.encode(v);
    cout<<e<<endl; for (auto& x: c.decode(e)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import ("fmt"; "strconv"; "strings")
func encode(strs []string) string {
    var b strings.Builder
    for _,s := range strs { b.WriteString(strconv.Itoa(len(s))); b.WriteByte('#'); b.WriteString(s) }
    return b.String()
}
func decode(s string) []string {
    out := []string{}; i := 0
    for i < len(s) {
        j := strings.IndexByte(s[i:], '#') + i
        n,_ := strconv.Atoi(s[i:j])
        out = append(out, s[j+1:j+1+n]); i = j+1+n
    }
    return out
}
func main(){ e := encode([]string{"lint","code","love","you"}); fmt.Println(e); fmt.Println(decode(e)) }
''',
"R":'''
encode <- function(strs) paste0(sapply(strs, function(s) paste0(nchar(s),"#",s)), collapse="")
decode <- function(s){ out <- c(); i <- 1
    while (i <= nchar(s)){ j <- regexpr("#", substr(s,i,nchar(s)))[1] + i - 1
        n <- as.integer(substr(s,i,j-1)); out <- c(out, substr(s,j+1,j+n)); i <- j+1+n }
    out
}
e <- encode(c("lint","code","love","you")); print(e); print(decode(e))
''',
}))

# ---- 064 Move Zeroes ----
LESSONS.append((64, "Move Zeroes", "Two Pointers", "Easy", 32,
"""Move all 0s to the end while maintaining relative order. In-place.

Example: [0,1,0,3,12] -> [1,3,12,0,0]""",
{
"Python":'''
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0: nums[i], nums[j] = nums[j], nums[i]; j += 1
        return nums

if __name__ == "__main__":
    print(Solution().moveZeroes([0,1,0,3,12]))
''',
"JavaScript":'''
var moveZeroes = function(nums){
    let j = 0;
    for (let i=0;i<nums.length;i++) if (nums[i]!==0){ [nums[i],nums[j]]=[nums[j],nums[i]]; j++; }
    return nums;
};
console.log(moveZeroes([0,1,0,3,12]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] moveZeroes(int[] nums){
        int j=0;
        for (int i=0;i<nums.length;i++) if (nums[i]!=0){ int t=nums[i]; nums[i]=nums[j]; nums[j]=t; j++; }
        return nums;
    }
    public static void main(String[] a){ System.out.println(Arrays.toString(new __CLASS__().moveZeroes(new int[]{0,1,0,3,12}))); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    void moveZeroes(vector<int>& nums){
        int j=0; for (size_t i=0;i<nums.size();++i) if (nums[i]) swap(nums[i], nums[j++]);
    }
};
int main(){ vector<int> v={0,1,0,3,12}; Solution().moveZeroes(v); for (int x: v) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func moveZeroes(nums []int) []int {
    j := 0
    for i := range nums { if nums[i]!=0 { nums[i], nums[j] = nums[j], nums[i]; j++ } }
    return nums
}
func main(){ fmt.Println(moveZeroes([]int{0,1,0,3,12})) }
''',
"R":'''
moveZeroes <- function(nums){ z <- nums[nums!=0]; c(z, rep(0, length(nums)-length(z))) }
print(moveZeroes(c(0,1,0,3,12)))
''',
}))

# ---- 065 Squares of a Sorted Array ----
LESSONS.append((65, "Squares of a Sorted Array", "Two Pointers", "Easy", 33,
"""Given a sorted (non-decreasing) array, return an array of squares of each number, also sorted.

Example: [-4,-1,0,3,10] -> [0,1,9,16,100]""",
{
"Python":'''
class Solution:
    def sortedSquares(self, nums):
        n = len(nums); out = [0]*n
        l, r, k = 0, n-1, n-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]): out[k] = nums[l]*nums[l]; l += 1
            else: out[k] = nums[r]*nums[r]; r -= 1
            k -= 1
        return out

if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
''',
"JavaScript":'''
var sortedSquares = function(nums){
    const n=nums.length, out=new Array(n); let l=0,r=n-1,k=n-1;
    while (l<=r){ if (Math.abs(nums[l])>Math.abs(nums[r])){ out[k]=nums[l]*nums[l]; l++; } else { out[k]=nums[r]*nums[r]; r--; } k--; }
    return out;
};
console.log(sortedSquares([-4,-1,0,3,10]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] sortedSquares(int[] nums){
        int n=nums.length, l=0, r=n-1, k=n-1; int[] out=new int[n];
        while (l<=r){ if (Math.abs(nums[l])>Math.abs(nums[r])){ out[k--]=nums[l]*nums[l]; l++; } else { out[k--]=nums[r]*nums[r]; r--; } }
        return out;
    }
    public static void main(String[] a){ System.out.println(Arrays.toString(new __CLASS__().sortedSquares(new int[]{-4,-1,0,3,10}))); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<int> sortedSquares(vector<int>& nums){
        int n=nums.size(), l=0, r=n-1, k=n-1; vector<int> out(n);
        while (l<=r){ if (abs(nums[l])>abs(nums[r])){ out[k--]=nums[l]*nums[l]; l++; } else { out[k--]=nums[r]*nums[r]; r--; } }
        return out;
    }
};
int main(){ vector<int> v={-4,-1,0,3,10}; for (int x: Solution().sortedSquares(v)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func abs(x int) int { if x<0 {return -x}; return x }
func sortedSquares(nums []int) []int {
    n := len(nums); out := make([]int,n); l,r,k := 0,n-1,n-1
    for l<=r { if abs(nums[l])>abs(nums[r]) { out[k]=nums[l]*nums[l]; l++ } else { out[k]=nums[r]*nums[r]; r-- }; k-- }
    return out
}
func main(){ fmt.Println(sortedSquares([]int{-4,-1,0,3,10})) }
''',
"R":'''
sortedSquares <- function(nums) sort(nums*nums)
print(sortedSquares(c(-4,-1,0,3,10)))
''',
}))

# ---- 066 Sort Colors ----
LESSONS.append((66, "Sort Colors", "Two Pointers", "Medium", 33,
"""Sort an array containing only 0,1,2 in-place. Dutch National Flag.

Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]""",
{
"Python":'''
class Solution:
    def sortColors(self, nums):
        l, m, r = 0, 0, len(nums)-1
        while m <= r:
            if nums[m] == 0: nums[l], nums[m] = nums[m], nums[l]; l+=1; m+=1
            elif nums[m] == 2: nums[m], nums[r] = nums[r], nums[m]; r-=1
            else: m+=1
        return nums

if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))
''',
"JavaScript":'''
var sortColors = function(nums){
    let l=0,m=0,r=nums.length-1;
    while (m<=r){
        if (nums[m]===0){ [nums[l],nums[m]]=[nums[m],nums[l]]; l++; m++; }
        else if (nums[m]===2){ [nums[m],nums[r]]=[nums[r],nums[m]]; r--; }
        else m++;
    }
    return nums;
};
console.log(sortColors([2,0,2,1,1,0]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] sortColors(int[] nums){
        int l=0,m=0,r=nums.length-1;
        while (m<=r){
            if (nums[m]==0){ int t=nums[l]; nums[l]=nums[m]; nums[m]=t; l++; m++; }
            else if (nums[m]==2){ int t=nums[m]; nums[m]=nums[r]; nums[r]=t; r--; }
            else m++;
        }
        return nums;
    }
    public static void main(String[] a){ System.out.println(Arrays.toString(new __CLASS__().sortColors(new int[]{2,0,2,1,1,0}))); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    void sortColors(vector<int>& nums){
        int l=0,m=0,r=(int)nums.size()-1;
        while (m<=r){
            if (nums[m]==0) swap(nums[l++], nums[m++]);
            else if (nums[m]==2) swap(nums[m], nums[r--]);
            else m++;
        }
    }
};
int main(){ vector<int> v={2,0,2,1,1,0}; Solution().sortColors(v); for (int x: v) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func sortColors(nums []int) []int {
    l,m,r := 0,0,len(nums)-1
    for m<=r {
        switch nums[m] {
        case 0: nums[l], nums[m] = nums[m], nums[l]; l++; m++
        case 2: nums[m], nums[r] = nums[r], nums[m]; r--
        default: m++
        }
    }
    return nums
}
func main(){ fmt.Println(sortColors([]int{2,0,2,1,1,0})) }
''',
"R":'''
sortColors <- function(nums) sort(nums)
print(sortColors(c(2,0,2,1,1,0)))
''',
}))

# ---- 067 Reverse Vowels of a String ----
LESSONS.append((67, "Reverse Vowels of a String", "Two Pointers", "Easy", 34,
"""Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).

Example: hello -> holle""",
{
"Python":'''
class Solution:
    def reverseVowels(self, s):
        v = set("aeiouAEIOU"); a = list(s); l,r = 0, len(a)-1
        while l < r:
            while l < r and a[l] not in v: l += 1
            while l < r and a[r] not in v: r -= 1
            a[l], a[r] = a[r], a[l]; l += 1; r -= 1
        return "".join(a)

if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
''',
"JavaScript":'''
var reverseVowels = function(s){
    const v = new Set("aeiouAEIOU"); const a = s.split(""); let l=0,r=a.length-1;
    while (l<r){ while (l<r && !v.has(a[l])) l++; while (l<r && !v.has(a[r])) r--;
        [a[l],a[r]] = [a[r],a[l]]; l++; r--; }
    return a.join("");
};
console.log(reverseVowels("hello"), reverseVowels("leetcode"));
''',
"Java":'''
public class __CLASS__ {
    public String reverseVowels(String s){
        char[] a = s.toCharArray(); String v = "aeiouAEIOU"; int l=0,r=a.length-1;
        while (l<r){ while (l<r && v.indexOf(a[l])<0) l++; while (l<r && v.indexOf(a[r])<0) r--;
            char t=a[l]; a[l]=a[r]; a[r]=t; l++; r--; }
        return new String(a);
    }
    public static void main(String[] x){
        System.out.println(new __CLASS__().reverseVowels("hello"));
        System.out.println(new __CLASS__().reverseVowels("leetcode"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    string reverseVowels(string s){
        string v="aeiouAEIOU"; int l=0,r=s.size()-1;
        while (l<r){ while (l<r && v.find(s[l])==string::npos) l++; while (l<r && v.find(s[r])==string::npos) r--;
            swap(s[l],s[r]); l++; r--; }
        return s;
    }
};
int main(){ cout<<Solution().reverseVowels("hello")<<" "<<Solution().reverseVowels("leetcode")<<endl; }
''',
"Go":'''
package main
import "fmt"
func reverseVowels(s string) string {
    v := "aeiouAEIOU"; a := []byte(s); l,r := 0,len(a)-1
    isV := func(c byte) bool { for i:=0;i<len(v);i++ { if v[i]==c { return true } }; return false }
    for l<r {
        for l<r && !isV(a[l]) { l++ }
        for l<r && !isV(a[r]) { r-- }
        a[l],a[r] = a[r],a[l]; l++; r--
    }
    return string(a)
}
func main(){ fmt.Println(reverseVowels("hello"), reverseVowels("leetcode")) }
''',
"R":'''
reverseVowels <- function(s){
    v <- c("a","e","i","o","u","A","E","I","O","U")
    a <- strsplit(s,"")[[1]]; l <- 1; r <- length(a)
    while (l<r){
        while (l<r && !(a[l] %in% v)) l <- l+1
        while (l<r && !(a[r] %in% v)) r <- r-1
        tmp <- a[l]; a[l] <- a[r]; a[r] <- tmp; l <- l+1; r <- r-1
    }
    paste(a, collapse="")
}
print(reverseVowels("hello")); print(reverseVowels("leetcode"))
''',
}))

# ---- 068 Best Time to Buy and Sell Stock II ----
LESSONS.append((68, "Best Time to Buy and Sell Stock II", "Greedy", "Medium", 34,
"""You may complete as many transactions as you like (buy then sell). Return max profit.

Example: [7,1,5,3,6,4] -> 7  (buy 1 sell 5, buy 3 sell 6)""",
{
"Python":'''
class Solution:
    def maxProfit(self, prices):
        return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
''',
"JavaScript":'''
var maxProfit = function(prices){
    let p=0; for (let i=1;i<prices.length;i++) p += Math.max(0, prices[i]-prices[i-1]); return p;
};
console.log(maxProfit([7,1,5,3,6,4]));
''',
"Java":'''
public class __CLASS__ {
    public int maxProfit(int[] prices){
        int p=0; for (int i=1;i<prices.length;i++) p += Math.max(0, prices[i]-prices[i-1]); return p;
    }
    public static void main(String[] a){ System.out.println(new __CLASS__().maxProfit(new int[]{7,1,5,3,6,4})); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int maxProfit(vector<int>& p){ int s=0; for (size_t i=1;i<p.size();++i) s += max(0, p[i]-p[i-1]); return s; }
};
int main(){ vector<int> v={7,1,5,3,6,4}; cout<<Solution().maxProfit(v)<<endl; }
''',
"Go":'''
package main
import "fmt"
func maxProfit(prices []int) int {
    s := 0
    for i := 1; i < len(prices); i++ { if prices[i] > prices[i-1] { s += prices[i]-prices[i-1] } }
    return s
}
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
''',
"R":'''
maxProfit <- function(prices){
    d <- diff(prices); sum(d[d>0])
}
print(maxProfit(c(7,1,5,3,6,4)))
''',
}))

# ---- 069 Add Two Numbers ----
LESSONS.append((69, "Add Two Numbers", "Linked List", "Medium", 35,
"""Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.

Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)""",
{
"Python":'''
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(); cur = dummy; carry = 0
        while l1 or l2 or carry:
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, d = divmod(x, 10); cur.next = ListNode(d); cur = cur.next
            l1 = l1.next if l1 else None; l2 = l2.next if l2 else None
        return dummy.next

def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out
def from_list(a):
    dummy = ListNode(); cur = dummy
    for x in a: cur.next = ListNode(x); cur = cur.next
    return dummy.next

if __name__ == "__main__":
    print(to_list(Solution().addTwoNumbers(from_list([2,4,3]), from_list([5,6,4]))))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var addTwoNumbers = function(l1, l2){
    const dummy = new ListNode(); let cur = dummy, carry = 0;
    while (l1 || l2 || carry){
        const x = (l1?l1.val:0) + (l2?l2.val:0) + carry;
        carry = Math.floor(x/10); cur.next = new ListNode(x%10); cur = cur.next;
        l1 = l1?l1.next:null; l2 = l2?l2.next:null;
    }
    return dummy.next;
};
const fromArr = a => { const d = new ListNode(); let c = d; for (const x of a){ c.next = new ListNode(x); c = c.next; } return d.next; };
const toArr = n => { const a = []; while (n){ a.push(n.val); n = n.next; } return a; };
console.log(toArr(addTwoNumbers(fromArr([2,4,3]), fromArr([5,6,4]))));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode dummy = new ListNode(0), cur = dummy; int carry = 0;
        while (l1!=null || l2!=null || carry>0){
            int x = (l1!=null?l1.val:0) + (l2!=null?l2.val:0) + carry;
            carry = x/10; cur.next = new ListNode(x%10); cur = cur.next;
            if (l1!=null) l1 = l1.next; if (l2!=null) l2 = l2.next;
        }
        return dummy.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        System.out.println(toArr(new __CLASS__().addTwoNumbers(fromArr(new int[]{2,4,3}), fromArr(new int[]{5,6,4}))));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
class Solution { public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
        ListNode dummy(0), *cur=&dummy; int carry=0;
        while (l1 || l2 || carry){
            int x = (l1?l1->val:0) + (l2?l2->val:0) + carry;
            carry = x/10; cur->next = new ListNode(x%10); cur = cur->next;
            if (l1) l1=l1->next; if (l2) l2=l2->next;
        }
        return dummy.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next = new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().addTwoNumbers(fromArr({2,4,3}), fromArr({5,6,4}));
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    dummy := &ListNode{}; cur := dummy; carry := 0
    for l1 != nil || l2 != nil || carry > 0 {
        x := carry
        if l1 != nil { x += l1.Val; l1 = l1.Next }
        if l2 != nil { x += l2.Val; l2 = l2.Next }
        carry = x/10; cur.Next = &ListNode{Val: x%10}; cur = cur.Next
    }
    return dummy.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := addTwoNumbers(fromArr([]int{2,4,3}), fromArr([]int{5,6,4}))
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }; fmt.Println() }
''',
"R":'''
addTwoNumbers <- function(a, b){
    n <- max(length(a), length(b)); a <- c(a, rep(0, n-length(a))); b <- c(b, rep(0, n-length(b)))
    out <- c(); carry <- 0
    for (i in 1:n){ s <- a[i]+b[i]+carry; carry <- s %/% 10; out <- c(out, s %% 10) }
    if (carry > 0) out <- c(out, carry)
    out
}
print(addTwoNumbers(c(2,4,3), c(5,6,4)))
''',
}))

# ---- 070 Remove Nth Node From End of List ----
LESSONS.append((70, "Remove Nth Node From End of List", "Linked List", "Medium", 35,
"""Remove the nth node from the end of a linked list and return its head.

Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5""",
{
"Python":'''
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head); fast = slow = dummy
        for _ in range(n): fast = fast.next
        while fast.next: fast = fast.next; slow = slow.next
        slow.next = slow.next.next
        return dummy.next

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().removeNthFromEnd(from_list([1,2,3,4,5]), 2)))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var removeNthFromEnd = function(head, n){
    const d = new ListNode(0, head); let fast = d, slow = d;
    for (let i=0;i<n;i++) fast = fast.next;
    while (fast.next){ fast = fast.next; slow = slow.next; }
    slow.next = slow.next.next; return d.next;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(removeNthFromEnd(fromArr([1,2,3,4,5]), 2)));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v, ListNode n){val=v; next=n;} }
    public ListNode removeNthFromEnd(ListNode head, int n){
        ListNode d = new ListNode(0, head); ListNode fast=d, slow=d;
        for (int i=0;i<n;i++) fast = fast.next;
        while (fast.next != null){ fast = fast.next; slow = slow.next; }
        slow.next = slow.next.next; return d.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0,null), c=d; for (int x: a){ c.next = new ListNode(x,null); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){ System.out.println(toArr(new __CLASS__().removeNthFromEnd(fromArr(new int[]{1,2,3,4,5}), 2))); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
class Solution { public:
    ListNode* removeNthFromEnd(ListNode* head, int n){
        ListNode d(0); d.next = head; ListNode *fast=&d, *slow=&d;
        for (int i=0;i<n;i++) fast = fast->next;
        while (fast->next){ fast = fast->next; slow = slow->next; }
        slow->next = slow->next->next; return d.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().removeNthFromEnd(fromArr({1,2,3,4,5}), 2);
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    d := &ListNode{Next: head}; fast, slow := d, d
    for i := 0; i < n; i++ { fast = fast.Next }
    for fast.Next != nil { fast = fast.Next; slow = slow.Next }
    slow.Next = slow.Next.Next; return d.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := removeNthFromEnd(fromArr([]int{1,2,3,4,5}), 2); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println() }
''',
"R":'''
removeNthFromEnd <- function(a, n){ a[-(length(a)-n+1)] }
print(removeNthFromEnd(c(1,2,3,4,5), 2))
''',
}))

# ---- 071 Reorder List ----
LESSONS.append((71, "Reorder List", "Linked List", "Medium", 36,
"""Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...

Example: 1->2->3->4 -> 1->4->2->3""",
{
"Python":'''
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def reorderList(self, head):
        if not head or not head.next: return head
        slow = fast = head
        while fast.next and fast.next.next: slow = slow.next; fast = fast.next.next
        prev, cur = None, slow.next; slow.next = None
        while cur: nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        l1, l2 = head, prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2; l2.next = t1
            l1, l2 = t1, t2
        return head

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().reorderList(from_list([1,2,3,4]))))
    print(to_list(Solution().reorderList(from_list([1,2,3,4,5]))))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var reorderList = function(head){
    if (!head || !head.next) return head;
    let slow = head, fast = head;
    while (fast.next && fast.next.next){ slow = slow.next; fast = fast.next.next; }
    let prev = null, cur = slow.next; slow.next = null;
    while (cur){ const n = cur.next; cur.next = prev; prev = cur; cur = n; }
    let l1 = head, l2 = prev;
    while (l2){ const t1 = l1.next, t2 = l2.next; l1.next = l2; l2.next = t1; l1 = t1; l2 = t2; }
    return head;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(reorderList(fromArr([1,2,3,4]))));
console.log(toArr(reorderList(fromArr([1,2,3,4,5]))));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v, ListNode n){val=v; next=n;} }
    public void reorderList(ListNode head){
        if (head==null || head.next==null) return;
        ListNode slow=head, fast=head;
        while (fast.next!=null && fast.next.next!=null){ slow=slow.next; fast=fast.next.next; }
        ListNode prev=null, cur=slow.next; slow.next=null;
        while (cur!=null){ ListNode n=cur.next; cur.next=prev; prev=cur; cur=n; }
        ListNode l1=head, l2=prev;
        while (l2!=null){ ListNode t1=l1.next, t2=l2.next; l1.next=l2; l2.next=t1; l1=t1; l2=t2; }
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0,null), c=d; for (int x: a){ c.next=new ListNode(x,null); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        ListNode h = fromArr(new int[]{1,2,3,4}); new __CLASS__().reorderList(h); System.out.println(toArr(h));
        ListNode h2 = fromArr(new int[]{1,2,3,4,5}); new __CLASS__().reorderList(h2); System.out.println(toArr(h2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
class Solution { public:
    void reorderList(ListNode* head){
        if (!head || !head->next) return;
        ListNode *slow=head, *fast=head;
        while (fast->next && fast->next->next){ slow=slow->next; fast=fast->next->next; }
        ListNode *prev=nullptr, *cur=slow->next; slow->next=nullptr;
        while (cur){ ListNode* n=cur->next; cur->next=prev; prev=cur; cur=n; }
        ListNode *l1=head, *l2=prev;
        while (l2){ ListNode *t1=l1->next, *t2=l2->next; l1->next=l2; l2->next=t1; l1=t1; l2=t2; }
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto h = fromArr({1,2,3,4}); Solution().reorderList(h);
    while (h){ cout<<h->val<<" "; h=h->next; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func reorderList(head *ListNode) {
    if head == nil || head.Next == nil { return }
    slow, fast := head, head
    for fast.Next != nil && fast.Next.Next != nil { slow = slow.Next; fast = fast.Next.Next }
    var prev *ListNode = nil; cur := slow.Next; slow.Next = nil
    for cur != nil { n := cur.Next; cur.Next = prev; prev = cur; cur = n }
    l1, l2 := head, prev
    for l2 != nil { t1, t2 := l1.Next, l2.Next; l1.Next = l2; l2.Next = t1; l1, l2 = t1, t2 }
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ h := fromArr([]int{1,2,3,4}); reorderList(h); for h != nil { fmt.Print(h.Val," "); h = h.Next }; fmt.Println() }
''',
"R":'''
reorderList <- function(a){
    n <- length(a); out <- c(); l <- 1; r <- n
    while (l <= r){ out <- c(out, a[l]); if (l != r) out <- c(out, a[r]); l <- l+1; r <- r-1 }
    out
}
print(reorderList(c(1,2,3,4)))
print(reorderList(c(1,2,3,4,5)))
''',
}))

# ---- 072 Linked List Cycle ----
LESSONS.append((72, "Linked List Cycle", "Linked List", "Easy", 36,
"""Determine if a linked list has a cycle. Floyd's tortoise and hare.""",
{
"Python":'''
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow is fast: return True
        return False

if __name__ == "__main__":
    a = ListNode(1); b = ListNode(2); c = ListNode(3)
    a.next = b; b.next = c; c.next = a
    print(Solution().hasCycle(a))
    d = ListNode(1); d.next = ListNode(2)
    print(Solution().hasCycle(d))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var hasCycle = function(head){
    let slow = head, fast = head;
    while (fast && fast.next){ slow = slow.next; fast = fast.next.next; if (slow === fast) return true; }
    return false;
};
const a = new ListNode(1), b = new ListNode(2), c = new ListNode(3);
a.next=b; b.next=c; c.next=a; console.log(hasCycle(a));
const d = new ListNode(1); d.next = new ListNode(2); console.log(hasCycle(d));
''',
"Java":'''
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public boolean hasCycle(ListNode head){
        ListNode slow=head, fast=head;
        while (fast!=null && fast.next!=null){ slow=slow.next; fast=fast.next.next; if (slow==fast) return true; }
        return false;
    }
    public static void main(String[] a){
        ListNode x=new ListNode(1), y=new ListNode(2), z=new ListNode(3);
        x.next=y; y.next=z; z.next=x; System.out.println(new __CLASS__().hasCycle(x));
        ListNode p=new ListNode(1); p.next=new ListNode(2); System.out.println(new __CLASS__().hasCycle(p));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
class Solution { public:
    bool hasCycle(ListNode* head){
        ListNode *slow=head, *fast=head;
        while (fast && fast->next){ slow=slow->next; fast=fast->next->next; if (slow==fast) return true; }
        return false;
    }
};
int main(){
    auto a = new ListNode(1), b = new ListNode(2), c = new ListNode(3);
    a->next=b; b->next=c; c->next=a; cout<<Solution().hasCycle(a)<<endl;
    auto d = new ListNode(1); d->next = new ListNode(2); cout<<Solution().hasCycle(d)<<endl;
}
''',
"Go":'''
package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func hasCycle(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil { slow = slow.Next; fast = fast.Next.Next; if slow == fast { return true } }
    return false
}
func main(){
    a := &ListNode{Val:1}; b := &ListNode{Val:2}; c := &ListNode{Val:3}
    a.Next = b; b.Next = c; c.Next = a; fmt.Println(hasCycle(a))
    d := &ListNode{Val:1}; d.Next = &ListNode{Val:2}; fmt.Println(hasCycle(d))
}
''',
"R":'''
# R has no native pointer-based linked list; emulate cycle with index successor vector.
hasCycle <- function(next_idx, start=1){
    slow <- start; fast <- start
    repeat {
        if (is.na(next_idx[fast]) || is.na(next_idx[next_idx[fast]])) return(FALSE)
        slow <- next_idx[slow]; fast <- next_idx[next_idx[fast]]
        if (slow == fast) return(TRUE)
    }
}
print(hasCycle(c(2,3,1)))   # 1->2->3->1 cycle
print(hasCycle(c(2,NA)))    # 1->2->NA no cycle
''',
}))

# ---- 073 Copy List With Random Pointer ----
LESSONS.append((73, "Copy List With Random Pointer", "Linked List", "Medium", 37,
"""Deep copy a linked list where each node has next and a random pointer that may point to any node or null.""",
{
"Python":'''
class Node:
    def __init__(self, v, n=None, r=None): self.val=v; self.next=n; self.random=r
class Solution:
    def copyRandomList(self, head):
        if not head: return None
        m = {}; cur = head
        while cur: m[cur] = Node(cur.val); cur = cur.next
        cur = head
        while cur:
            m[cur].next = m.get(cur.next); m[cur].random = m.get(cur.random); cur = cur.next
        return m[head]

if __name__ == "__main__":
    a = Node(1); b = Node(2); a.next = b; a.random = b; b.random = b
    c = Solution().copyRandomList(a)
    print([(n.val, n.random.val if n.random else None) for n in [c, c.next]])
''',
"JavaScript":'''
function Node(v,n,r){ this.val=v; this.next=n||null; this.random=r||null; }
var copyRandomList = function(head){
    if (!head) return null;
    const m = new Map(); let cur = head;
    while (cur){ m.set(cur, new Node(cur.val)); cur = cur.next; }
    cur = head;
    while (cur){ m.get(cur).next = m.get(cur.next) || null; m.get(cur).random = m.get(cur.random) || null; cur = cur.next; }
    return m.get(head);
};
const a = new Node(1), b = new Node(2); a.next = b; a.random = b; b.random = b;
const c = copyRandomList(a);
console.log([[c.val, c.random.val], [c.next.val, c.next.random.val]]);
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class Node { int val; Node next, random; Node(int v){val=v;} }
    public Node copyRandomList(Node head){
        if (head==null) return null;
        Map<Node,Node> m = new HashMap<>(); Node cur = head;
        while (cur!=null){ m.put(cur, new Node(cur.val)); cur = cur.next; }
        cur = head;
        while (cur!=null){ m.get(cur).next = m.get(cur.next); m.get(cur).random = m.get(cur.random); cur = cur.next; }
        return m.get(head);
    }
    public static void main(String[] a){
        Node x=new Node(1), y=new Node(2); x.next=y; x.random=y; y.random=y;
        Node c = new __CLASS__().copyRandomList(x);
        System.out.println(c.val+","+c.random.val+" "+c.next.val+","+c.next.random.val);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct Node { int val; Node *next; Node *random; Node(int v):val(v),next(nullptr),random(nullptr){} };
class Solution { public:
    Node* copyRandomList(Node* head){
        if (!head) return nullptr;
        unordered_map<Node*, Node*> m; Node* cur = head;
        while (cur){ m[cur] = new Node(cur->val); cur = cur->next; }
        cur = head;
        while (cur){ m[cur]->next = m[cur->next]; m[cur]->random = m[cur->random]; cur = cur->next; }
        return m[head];
    }
};
int main(){
    auto a = new Node(1), b = new Node(2); a->next=b; a->random=b; b->random=b;
    auto c = Solution().copyRandomList(a);
    cout<<c->val<<","<<c->random->val<<" "<<c->next->val<<","<<c->next->random->val<<endl;
}
''',
"Go":'''
package main
import "fmt"
type Node struct { Val int; Next, Random *Node }
func copyRandomList(head *Node) *Node {
    if head == nil { return nil }
    m := map[*Node]*Node{}
    for c := head; c != nil; c = c.Next { m[c] = &Node{Val: c.Val} }
    for c := head; c != nil; c = c.Next { m[c].Next = m[c.Next]; m[c].Random = m[c.Random] }
    return m[head]
}
func main(){
    a := &Node{Val:1}; b := &Node{Val:2}; a.Next = b; a.Random = b; b.Random = b
    c := copyRandomList(a)
    fmt.Println(c.Val, c.Random.Val, c.Next.Val, c.Next.Random.Val)
}
''',
"R":'''
# Emulate with a data.frame: val, next_idx, random_idx
copyRandomList <- function(df){
    df2 <- df  # already a value copy in R
    df2
}
df <- data.frame(val=c(1,2), next_idx=c(2,NA), random_idx=c(2,2))
print(copyRandomList(df))
''',
}))

# ---- 074 LRU Cache ----
LESSONS.append((74, "LRU Cache", "Linked List", "Medium", 37,
"""Design an LRU cache with O(1) get and put.""",
{
"Python":'''
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity): self.cap = capacity; self.d = OrderedDict()
    def get(self, key):
        if key not in self.d: return -1
        self.d.move_to_end(key); return self.d[key]
    def put(self, key, value):
        if key in self.d: self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.cap: self.d.popitem(last=False)

if __name__ == "__main__":
    c = LRUCache(2); c.put(1,1); c.put(2,2); print(c.get(1))
    c.put(3,3); print(c.get(2)); c.put(4,4); print(c.get(1), c.get(3), c.get(4))
''',
"JavaScript":'''
class LRUCache {
    constructor(cap){ this.cap = cap; this.m = new Map(); }
    get(k){ if (!this.m.has(k)) return -1; const v = this.m.get(k); this.m.delete(k); this.m.set(k,v); return v; }
    put(k, v){ if (this.m.has(k)) this.m.delete(k); this.m.set(k,v); if (this.m.size > this.cap) this.m.delete(this.m.keys().next().value); }
}
const c = new LRUCache(2); c.put(1,1); c.put(2,2); console.log(c.get(1));
c.put(3,3); console.log(c.get(2)); c.put(4,4); console.log(c.get(1), c.get(3), c.get(4));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class LRU extends LinkedHashMap<Integer,Integer> {
        private final int cap;
        LRU(int c){ super(c, 0.75f, true); this.cap = c; }
        protected boolean removeEldestEntry(Map.Entry<Integer,Integer> e){ return size() > cap; }
    }
    public static void main(String[] a){
        LRU c = new LRU(2); c.put(1,1); c.put(2,2);
        System.out.println(c.getOrDefault(1,-1));
        c.put(3,3); System.out.println(c.getOrDefault(2,-1));
        c.put(4,4); System.out.println(c.getOrDefault(1,-1)+" "+c.getOrDefault(3,-1)+" "+c.getOrDefault(4,-1));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class LRUCache {
    int cap; list<pair<int,int>> dq; unordered_map<int, list<pair<int,int>>::iterator> m;
public:
    LRUCache(int c): cap(c) {}
    int get(int k){
        auto it = m.find(k); if (it == m.end()) return -1;
        dq.splice(dq.begin(), dq, it->second); return it->second->second;
    }
    void put(int k, int v){
        auto it = m.find(k);
        if (it != m.end()){ it->second->second = v; dq.splice(dq.begin(), dq, it->second); return; }
        dq.push_front({k,v}); m[k] = dq.begin();
        if ((int)dq.size() > cap){ m.erase(dq.back().first); dq.pop_back(); }
    }
};
int main(){ LRUCache c(2); c.put(1,1); c.put(2,2); cout<<c.get(1)<<endl;
    c.put(3,3); cout<<c.get(2)<<endl; c.put(4,4);
    cout<<c.get(1)<<" "<<c.get(3)<<" "<<c.get(4)<<endl; }
''',
"Go":'''
package main
import ("container/list"; "fmt")
type LRUCache struct { cap int; l *list.List; m map[int]*list.Element }
type entry struct { k, v int }
func Constructor(cap int) LRUCache { return LRUCache{cap: cap, l: list.New(), m: map[int]*list.Element{}} }
func (c *LRUCache) Get(k int) int {
    if e, ok := c.m[k]; ok { c.l.MoveToFront(e); return e.Value.(*entry).v }
    return -1
}
func (c *LRUCache) Put(k, v int) {
    if e, ok := c.m[k]; ok { e.Value.(*entry).v = v; c.l.MoveToFront(e); return }
    e := c.l.PushFront(&entry{k,v}); c.m[k] = e
    if c.l.Len() > c.cap { b := c.l.Back(); delete(c.m, b.Value.(*entry).k); c.l.Remove(b) }
}
func main(){ c := Constructor(2); c.Put(1,1); c.Put(2,2); fmt.Println(c.Get(1))
    c.Put(3,3); fmt.Println(c.Get(2)); c.Put(4,4); fmt.Println(c.Get(1), c.Get(3), c.Get(4)) }
''',
"R":'''
# Simple LRU using a named list with manual recency list
LRU <- function(cap){
    e <- new.env(); e$cap <- cap; e$keys <- c(); e$vals <- list()
    e$get <- function(k){
        if (!(k %in% e$keys)) return(-1)
        v <- e$vals[[as.character(k)]]; e$keys <- c(setdiff(e$keys, k), k); v
    }
    e$put <- function(k, v){
        e$vals[[as.character(k)]] <- v
        e$keys <- c(setdiff(e$keys, k), k)
        if (length(e$keys) > e$cap){
            old <- e$keys[1]; e$keys <- e$keys[-1]; e$vals[[as.character(old)]] <- NULL
        }
    }
    e
}
c <- LRU(2); c$put(1,1); c$put(2,2); print(c$get(1))
c$put(3,3); print(c$get(2)); c$put(4,4); print(c(c$get(1), c$get(3), c$get(4)))
''',
}))

# ---- 075 Merge K Sorted Lists ----
LESSONS.append((75, "Merge K Sorted Lists", "Linked List", "Hard", 38,
"""Merge k sorted linked lists into one sorted list.

Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6""",
{
"Python":'''
import heapq
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def mergeKLists(self, lists):
        h = []
        for i, n in enumerate(lists):
            if n: heapq.heappush(h, (n.val, i, n))
        d = ListNode(); cur = d
        while h:
            v, i, n = heapq.heappop(h); cur.next = n; cur = n
            if n.next: heapq.heappush(h, (n.next.val, i, n.next))
        return d.next

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().mergeKLists([from_list([1,4,5]), from_list([1,3,4]), from_list([2,6])])))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var mergeKLists = function(lists){
    const arr = []; for (const l of lists){ let n=l; while (n){ arr.push(n.val); n=n.next; } }
    arr.sort((a,b)=>a-b);
    const d = new ListNode(); let c = d; for (const x of arr){ c.next = new ListNode(x); c = c.next; }
    return d.next;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(mergeKLists([fromArr([1,4,5]), fromArr([1,3,4]), fromArr([2,6])])));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode mergeKLists(ListNode[] lists){
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b)->a.val-b.val);
        for (ListNode n: lists) if (n!=null) pq.add(n);
        ListNode d = new ListNode(0), cur = d;
        while (!pq.isEmpty()){
            ListNode n = pq.poll(); cur.next = n; cur = n;
            if (n.next != null) pq.add(n.next);
        }
        return d.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        ListNode[] ls = { fromArr(new int[]{1,4,5}), fromArr(new int[]{1,3,4}), fromArr(new int[]{2,6}) };
        System.out.println(toArr(new __CLASS__().mergeKLists(ls)));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
struct Cmp { bool operator()(ListNode* a, ListNode* b) const { return a->val > b->val; } };
class Solution { public:
    ListNode* mergeKLists(vector<ListNode*>& lists){
        priority_queue<ListNode*, vector<ListNode*>, Cmp> pq;
        for (auto n: lists) if (n) pq.push(n);
        ListNode d(0), *cur = &d;
        while (!pq.empty()){
            auto n = pq.top(); pq.pop(); cur->next = n; cur = n;
            if (n->next) pq.push(n->next);
        }
        return d.next;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ vector<ListNode*> ls = { fromArr({1,4,5}), fromArr({1,3,4}), fromArr({2,6}) };
    auto r = Solution().mergeKLists(ls); while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl; }
''',
"Go":'''
package main
import ("container/heap"; "fmt")
type ListNode struct { Val int; Next *ListNode }
type PQ []*ListNode
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].Val < p[j].Val }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(*ListNode)) }
func (p *PQ) Pop() interface{} { old := *p; n := len(old); x := old[n-1]; *p = old[:n-1]; return x }
func mergeKLists(lists []*ListNode) *ListNode {
    pq := &PQ{}; heap.Init(pq)
    for _, n := range lists { if n != nil { heap.Push(pq, n) } }
    d := &ListNode{}; cur := d
    for pq.Len() > 0 {
        n := heap.Pop(pq).(*ListNode); cur.Next = n; cur = n
        if n.Next != nil { heap.Push(pq, n.Next) }
    }
    return d.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ ls := []*ListNode{ fromArr([]int{1,4,5}), fromArr([]int{1,3,4}), fromArr([]int{2,6}) }
    r := mergeKLists(ls); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println() }
''',
"R":'''
mergeKLists <- function(lists) sort(unlist(lists))
print(mergeKLists(list(c(1,4,5), c(1,3,4), c(2,6))))
''',
}))

# ---- 076 Reverse Nodes in k-Group ----
LESSONS.append((76, "Reverse Nodes in k-Group", "Linked List", "Hard", 38,
"""Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.

Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5""",
{
"Python":'''
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def reverseKGroup(self, head, k):
        cur = head; cnt = 0
        while cur and cnt < k: cur = cur.next; cnt += 1
        if cnt < k: return head
        prev, cur = None, head
        for _ in range(k):
            nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return prev

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().reverseKGroup(from_list([1,2,3,4,5]), 2)))
    print(to_list(Solution().reverseKGroup(from_list([1,2,3,4,5]), 3)))
''',
"JavaScript":'''
function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var reverseKGroup = function(head, k){
    let cur = head, cnt = 0;
    while (cur && cnt < k){ cur = cur.next; cnt++; }
    if (cnt < k) return head;
    let prev = null; cur = head;
    for (let i=0;i<k;i++){ const n = cur.next; cur.next = prev; prev = cur; cur = n; }
    head.next = reverseKGroup(cur, k);
    return prev;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(reverseKGroup(fromArr([1,2,3,4,5]), 2)));
console.log(toArr(reverseKGroup(fromArr([1,2,3,4,5]), 3)));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode reverseKGroup(ListNode head, int k){
        ListNode cur = head; int cnt = 0;
        while (cur != null && cnt < k){ cur = cur.next; cnt++; }
        if (cnt < k) return head;
        ListNode prev = null; cur = head;
        for (int i=0;i<k;i++){ ListNode n = cur.next; cur.next = prev; prev = cur; cur = n; }
        head.next = reverseKGroup(cur, k);
        return prev;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        System.out.println(toArr(new __CLASS__().reverseKGroup(fromArr(new int[]{1,2,3,4,5}), 2)));
        System.out.println(toArr(new __CLASS__().reverseKGroup(fromArr(new int[]{1,2,3,4,5}), 3)));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };
class Solution { public:
    ListNode* reverseKGroup(ListNode* head, int k){
        ListNode* cur = head; int cnt = 0;
        while (cur && cnt < k){ cur = cur->next; cnt++; }
        if (cnt < k) return head;
        ListNode* prev = nullptr; cur = head;
        for (int i=0;i<k;i++){ ListNode* n = cur->next; cur->next = prev; prev = cur; cur = n; }
        head->next = reverseKGroup(cur, k);
        return prev;
    }
};
ListNode* fromArr(vector<int> a){ ListNode d(0), *c=&d; for (int x: a){ c->next=new ListNode(x); c=c->next; } return d.next; }
int main(){ auto r = Solution().reverseKGroup(fromArr({1,2,3,4,5}), 2);
    while (r){ cout<<r->val<<" "; r=r->next; } cout<<endl;
    auto s = Solution().reverseKGroup(fromArr({1,2,3,4,5}), 3);
    while (s){ cout<<s->val<<" "; s=s->next; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func reverseKGroup(head *ListNode, k int) *ListNode {
    cur := head; cnt := 0
    for cur != nil && cnt < k { cur = cur.Next; cnt++ }
    if cnt < k { return head }
    var prev *ListNode = nil; cur = head
    for i := 0; i < k; i++ { n := cur.Next; cur.Next = prev; prev = cur; cur = n }
    head.Next = reverseKGroup(cur, k)
    return prev
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := reverseKGroup(fromArr([]int{1,2,3,4,5}), 2); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println()
    s := reverseKGroup(fromArr([]int{1,2,3,4,5}), 3); for s != nil { fmt.Print(s.Val," "); s = s.Next }; fmt.Println() }
''',
"R":'''
reverseKGroup <- function(a, k){
    n <- length(a); out <- a; i <- 1
    while (i + k - 1 <= n){ out[i:(i+k-1)] <- rev(out[i:(i+k-1)]); i <- i + k }
    out
}
print(reverseKGroup(c(1,2,3,4,5), 2))
print(reverseKGroup(c(1,2,3,4,5), 3))
''',
}))

# ---- 077 Find the Duplicate Number ----
LESSONS.append((77, "Find the Duplicate Number", "Two Pointers", "Medium", 39,
"""An array of n+1 integers in [1,n] has exactly one duplicate. Find it (Floyd cycle detection, O(n) time, O(1) space).""",
{
"Python":'''
class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]; fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast: slow = nums[slow]; fast = nums[fast]
        return slow

if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))
''',
"JavaScript":'''
var findDuplicate = function(nums){
    let slow = nums[0], fast = nums[0];
    do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow !== fast);
    slow = nums[0];
    while (slow !== fast){ slow = nums[slow]; fast = nums[fast]; }
    return slow;
};
console.log(findDuplicate([1,3,4,2,2]), findDuplicate([3,1,3,4,2]));
''',
"Java":'''
public class __CLASS__ {
    public int findDuplicate(int[] nums){
        int slow = nums[0], fast = nums[0];
        do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
        slow = nums[0];
        while (slow != fast){ slow = nums[slow]; fast = nums[fast]; }
        return slow;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().findDuplicate(new int[]{1,3,4,2,2}));
        System.out.println(new __CLASS__().findDuplicate(new int[]{3,1,3,4,2}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int findDuplicate(vector<int>& nums){
        int slow = nums[0], fast = nums[0];
        do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
        slow = nums[0];
        while (slow != fast){ slow = nums[slow]; fast = nums[fast]; }
        return slow;
    }
};
int main(){ vector<int> a={1,3,4,2,2}, b={3,1,3,4,2};
    cout<<Solution().findDuplicate(a)<<" "<<Solution().findDuplicate(b)<<endl; }
''',
"Go":'''
package main
import "fmt"
func findDuplicate(nums []int) int {
    slow, fast := nums[0], nums[0]
    for { slow = nums[slow]; fast = nums[nums[fast]]; if slow == fast { break } }
    slow = nums[0]
    for slow != fast { slow = nums[slow]; fast = nums[fast] }
    return slow
}
func main(){ fmt.Println(findDuplicate([]int{1,3,4,2,2}), findDuplicate([]int{3,1,3,4,2})) }
''',
"R":'''
findDuplicate <- function(nums){ t <- table(nums); as.integer(names(t)[t > 1]) }
print(findDuplicate(c(1,3,4,2,2)))
print(findDuplicate(c(3,1,3,4,2)))
''',
}))

# ---- 078 Same Tree ----
LESSONS.append((78, "Same Tree", "Trees", "Easy", 39,
"""Given two binary trees, check if they are structurally identical with same node values.""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    c = TreeNode(1, TreeNode(2))
    print(Solution().isSameTree(a, b)); print(Solution().isSameTree(a, c))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var isSameTree = function(p, q){
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
const a = new TreeNode(1, new TreeNode(2), new TreeNode(3));
const b = new TreeNode(1, new TreeNode(2), new TreeNode(3));
const c = new TreeNode(1, new TreeNode(2));
console.log(isSameTree(a,b), isSameTree(a,c));
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public boolean isSameTree(TreeNode p, TreeNode q){
        if (p==null && q==null) return true;
        if (p==null || q==null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
    public static void main(String[] a){
        TreeNode x = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode y = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode z = new TreeNode(1, new TreeNode(2), null);
        System.out.println(new __CLASS__().isSameTree(x,y)+" "+new __CLASS__().isSameTree(x,z));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution { public:
    bool isSameTree(TreeNode* p, TreeNode* q){
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    }
};
int main(){ auto a = new TreeNode(1); a->left = new TreeNode(2); a->right = new TreeNode(3);
    auto b = new TreeNode(1); b->left = new TreeNode(2); b->right = new TreeNode(3);
    cout<<Solution().isSameTree(a,b)<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func isSameTree(p, q *TreeNode) bool {
    if p == nil && q == nil { return true }
    if p == nil || q == nil || p.Val != q.Val { return false }
    return isSameTree(p.Left,q.Left) && isSameTree(p.Right,q.Right)
}
func main(){ a := &TreeNode{Val:1, Left:&TreeNode{Val:2}, Right:&TreeNode{Val:3}}
    b := &TreeNode{Val:1, Left:&TreeNode{Val:2}, Right:&TreeNode{Val:3}}
    fmt.Println(isSameTree(a,b)) }
''',
"R":'''
# Represent a tree as a nested list: list(val, left, right) or NULL
isSameTree <- function(p, q){
    if (is.null(p) && is.null(q)) return(TRUE)
    if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
    isSameTree(p$left, q$left) && isSameTree(p$right, q$right)
}
a <- list(val=1, left=list(val=2,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL))
b <- list(val=1, left=list(val=2,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL))
print(isSameTree(a,b))
''',
}))

# ---- 079 Subtree of Another Tree ----
LESSONS.append((79, "Subtree of Another Tree", "Trees", "Easy", 40,
"""Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root, sub):
        if not root: return False
        if self.isSameTree(root, sub): return True
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    s = TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree(r, s))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
const same = (p,q) => !p && !q ? true : (!p||!q||p.val!==q.val ? false : same(p.left,q.left)&&same(p.right,q.right));
var isSubtree = function(root, sub){
    if (!root) return false;
    if (same(root, sub)) return true;
    return isSubtree(root.left, sub) || isSubtree(root.right, sub);
};
const r = new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(2)), new TreeNode(5));
const s = new TreeNode(4, new TreeNode(1), new TreeNode(2));
console.log(isSubtree(r, s));
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    boolean same(TreeNode p, TreeNode q){
        if (p==null && q==null) return true;
        if (p==null || q==null || p.val != q.val) return false;
        return same(p.left,q.left) && same(p.right,q.right);
    }
    public boolean isSubtree(TreeNode root, TreeNode sub){
        if (root == null) return false;
        if (same(root, sub)) return true;
        return isSubtree(root.left, sub) || isSubtree(root.right, sub);
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(2)), new TreeNode(5));
        TreeNode s = new TreeNode(4, new TreeNode(1), new TreeNode(2));
        System.out.println(new __CLASS__().isSubtree(r, s));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution {
    bool same(TreeNode* p, TreeNode* q){
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return same(p->left,q->left) && same(p->right,q->right);
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* sub){
        if (!root) return false;
        if (same(root, sub)) return true;
        return isSubtree(root->left, sub) || isSubtree(root->right, sub);
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(4); r->right = new TreeNode(5);
    r->left->left = new TreeNode(1); r->left->right = new TreeNode(2);
    auto s = new TreeNode(4); s->left = new TreeNode(1); s->right = new TreeNode(2);
    cout<<Solution().isSubtree(r, s)<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func same(p, q *TreeNode) bool {
    if p == nil && q == nil { return true }
    if p == nil || q == nil || p.Val != q.Val { return false }
    return same(p.Left,q.Left) && same(p.Right,q.Right)
}
func isSubtree(root, sub *TreeNode) bool {
    if root == nil { return false }
    if same(root, sub) { return true }
    return isSubtree(root.Left, sub) || isSubtree(root.Right, sub)
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:2}}, Right:&TreeNode{Val:5}}
    s := &TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:2}}
    fmt.Println(isSubtree(r, s))
}
''',
"R":'''
same <- function(p,q){ if (is.null(p) && is.null(q)) return(TRUE); if (is.null(p)||is.null(q)||p$val!=q$val) return(FALSE); same(p$left,q$left) && same(p$right,q$right) }
isSubtree <- function(r, s){ if (is.null(r)) return(FALSE); if (same(r,s)) return(TRUE); isSubtree(r$left,s) || isSubtree(r$right,s) }
mk <- function(v,l=NULL,rr=NULL) list(val=v,left=l,right=rr)
r <- mk(3, mk(4, mk(1), mk(2)), mk(5))
s <- mk(4, mk(1), mk(2))
print(isSubtree(r, s))
''',
}))

# ---- 080 Binary Tree Level Order Traversal ----
LESSONS.append((80, "Binary Tree Level Order Traversal", "Trees", "Medium", 40,
"""Return level-order traversal of a binary tree as list of lists.

Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]""",
{
"Python":'''
from collections import deque
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def levelOrder(self, root):
        if not root: return []
        out, q = [], deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft(); level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            out.append(level)
        return out

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().levelOrder(r))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var levelOrder = function(root){
    if (!root) return [];
    const out = [], q = [root];
    while (q.length){
        const lvl = [], n = q.length;
        for (let i=0;i<n;i++){ const x = q.shift(); lvl.push(x.val); if (x.left) q.push(x.left); if (x.right) q.push(x.right); }
        out.push(lvl);
    }
    return out;
};
const r = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
console.log(levelOrder(r));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> q = new ArrayDeque<>(); q.add(root);
        while (!q.isEmpty()){
            int n = q.size(); List<Integer> lvl = new ArrayList<>();
            for (int i=0;i<n;i++){ TreeNode x = q.poll(); lvl.add(x.val);
                if (x.left != null) q.add(x.left); if (x.right != null) q.add(x.right); }
            out.add(lvl);
        }
        return out;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(new __CLASS__().levelOrder(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution { public:
    vector<vector<int>> levelOrder(TreeNode* root){
        vector<vector<int>> out; if (!root) return out;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()){
            int n = q.size(); vector<int> lvl;
            for (int i=0;i<n;i++){ auto x = q.front(); q.pop(); lvl.push_back(x->val);
                if (x->left) q.push(x->left); if (x->right) q.push(x->right); }
            out.push_back(lvl);
        }
        return out;
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(9); r->right = new TreeNode(20);
    r->right->left = new TreeNode(15); r->right->right = new TreeNode(7);
    for (auto& lvl: Solution().levelOrder(r)){ for (int x: lvl) cout<<x<<" "; cout<<"|"; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func levelOrder(root *TreeNode) [][]int {
    out := [][]int{}; if root == nil { return out }
    q := []*TreeNode{root}
    for len(q) > 0 {
        n := len(q); lvl := []int{}
        for i := 0; i < n; i++ { x := q[0]; q = q[1:]; lvl = append(lvl, x.Val)
            if x.Left != nil { q = append(q, x.Left) }
            if x.Right != nil { q = append(q, x.Right) } }
        out = append(out, lvl)
    }
    return out
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:9}, Right:&TreeNode{Val:20, Left:&TreeNode{Val:15}, Right:&TreeNode{Val:7}}}
    fmt.Println(levelOrder(r))
}
''',
"R":'''
levelOrder <- function(root){
    if (is.null(root)) return(list())
    out <- list(); q <- list(root)
    while (length(q) > 0){
        lvl <- c(); nq <- list()
        for (n in q){ lvl <- c(lvl, n$val)
            if (!is.null(n$left)) nq <- c(nq, list(n$left))
            if (!is.null(n$right)) nq <- c(nq, list(n$right)) }
        out <- c(out, list(lvl)); q <- nq
    }
    out
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(levelOrder(mk(3, mk(9), mk(20, mk(15), mk(7)))))
''',
}))

# ---- 081 Binary Tree Right Side View ----
LESSONS.append((81, "Binary Tree Right Side View", "Trees", "Medium", 41,
"""Return the values of nodes you'd see ordered from top to bottom from the right side.

Example: [1,2,3,null,5,null,4] -> [1,3,4]""",
{
"Python":'''
from collections import deque
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def rightSideView(self, root):
        if not root: return []
        out, q = [], deque([root])
        while q:
            n = len(q)
            for i in range(n):
                x = q.popleft()
                if i == n-1: out.append(x.val)
                if x.left: q.append(x.left)
                if x.right: q.append(x.right)
        return out

if __name__ == "__main__":
    r = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(Solution().rightSideView(r))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var rightSideView = function(root){
    if (!root) return [];
    const out = [], q = [root];
    while (q.length){
        const n = q.length;
        for (let i=0;i<n;i++){ const x = q.shift(); if (i===n-1) out.push(x.val);
            if (x.left) q.push(x.left); if (x.right) q.push(x.right); }
    }
    return out;
};
const r = new TreeNode(1, new TreeNode(2, null, new TreeNode(5)), new TreeNode(3, null, new TreeNode(4)));
console.log(rightSideView(r));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public List<Integer> rightSideView(TreeNode root){
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> q = new ArrayDeque<>(); q.add(root);
        while (!q.isEmpty()){
            int n = q.size();
            for (int i=0;i<n;i++){ TreeNode x = q.poll(); if (i == n-1) out.add(x.val);
                if (x.left != null) q.add(x.left); if (x.right != null) q.add(x.right); }
        }
        return out;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(1, new TreeNode(2, null, new TreeNode(5)), new TreeNode(3, null, new TreeNode(4)));
        System.out.println(new __CLASS__().rightSideView(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution { public:
    vector<int> rightSideView(TreeNode* root){
        vector<int> out; if (!root) return out;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()){
            int n = q.size();
            for (int i=0;i<n;i++){ auto x = q.front(); q.pop(); if (i == n-1) out.push_back(x->val);
                if (x->left) q.push(x->left); if (x->right) q.push(x->right); }
        }
        return out;
    }
};
int main(){ auto r = new TreeNode(1); r->left = new TreeNode(2); r->right = new TreeNode(3);
    r->left->right = new TreeNode(5); r->right->right = new TreeNode(4);
    for (int x: Solution().rightSideView(r)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func rightSideView(root *TreeNode) []int {
    out := []int{}; if root == nil { return out }
    q := []*TreeNode{root}
    for len(q) > 0 {
        n := len(q)
        for i := 0; i < n; i++ { x := q[0]; q = q[1:]; if i == n-1 { out = append(out, x.Val) }
            if x.Left != nil { q = append(q, x.Left) }
            if x.Right != nil { q = append(q, x.Right) } }
    }
    return out
}
func main(){
    r := &TreeNode{Val:1, Left:&TreeNode{Val:2, Right:&TreeNode{Val:5}}, Right:&TreeNode{Val:3, Right:&TreeNode{Val:4}}}
    fmt.Println(rightSideView(r))
}
''',
"R":'''
rightSideView <- function(root){
    if (is.null(root)) return(c())
    out <- c(); q <- list(root)
    while (length(q) > 0){
        nq <- list(); n <- length(q)
        for (i in seq_along(q)){ x <- q[[i]]; if (i == n) out <- c(out, x$val)
            if (!is.null(x$left)) nq <- c(nq, list(x$left))
            if (!is.null(x$right)) nq <- c(nq, list(x$right)) }
        q <- nq
    }
    out
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(rightSideView(mk(1, mk(2, NULL, mk(5)), mk(3, NULL, mk(4)))))
''',
}))

# ---- 082 Count Good Nodes in Binary Tree ----
LESSONS.append((82, "Count Good Nodes in Binary Tree", "Trees", "Medium", 41,
"""A node X is good if no node on the path from root to X has value greater than X. Count good nodes.

Example: [3,1,4,3,null,1,5] -> 4""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def goodNodes(self, root):
        def dfs(n, mx):
            if not n: return 0
            c = 1 if n.val >= mx else 0
            mx = max(mx, n.val)
            return c + dfs(n.left, mx) + dfs(n.right, mx)
        return dfs(root, root.val)

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(Solution().goodNodes(r))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var goodNodes = function(root){
    const dfs = (n, mx) => { if (!n) return 0;
        const c = n.val >= mx ? 1 : 0; const m = Math.max(mx, n.val);
        return c + dfs(n.left, m) + dfs(n.right, m); };
    return dfs(root, root.val);
};
const r = new TreeNode(3, new TreeNode(1, new TreeNode(3)), new TreeNode(4, new TreeNode(1), new TreeNode(5)));
console.log(goodNodes(r));
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    int dfs(TreeNode n, int mx){ if (n == null) return 0;
        int c = n.val >= mx ? 1 : 0; int m = Math.max(mx, n.val);
        return c + dfs(n.left, m) + dfs(n.right, m); }
    public int goodNodes(TreeNode root){ return dfs(root, root.val); }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(1, new TreeNode(3), null), new TreeNode(4, new TreeNode(1), new TreeNode(5)));
        System.out.println(new __CLASS__().goodNodes(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution {
    int dfs(TreeNode* n, int mx){ if (!n) return 0;
        int c = n->val >= mx ? 1 : 0; int m = max(mx, n->val);
        return c + dfs(n->left, m) + dfs(n->right, m); }
public:
    int goodNodes(TreeNode* root){ return dfs(root, root->val); }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(1); r->right = new TreeNode(4);
    r->left->left = new TreeNode(3); r->right->left = new TreeNode(1); r->right->right = new TreeNode(5);
    cout<<Solution().goodNodes(r)<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func goodNodes(root *TreeNode) int {
    var dfs func(n *TreeNode, mx int) int
    dfs = func(n *TreeNode, mx int) int {
        if n == nil { return 0 }
        c := 0; if n.Val >= mx { c = 1 }
        m := mx; if n.Val > m { m = n.Val }
        return c + dfs(n.Left, m) + dfs(n.Right, m)
    }
    return dfs(root, root.Val)
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:1, Left:&TreeNode{Val:3}}, Right:&TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:5}}}
    fmt.Println(goodNodes(r))
}
''',
"R":'''
goodNodes <- function(root){
    dfs <- function(n, mx){ if (is.null(n)) return(0)
        c <- if (n$val >= mx) 1 else 0
        m <- max(mx, n$val)
        c + dfs(n$left, m) + dfs(n$right, m) }
    dfs(root, root$val)
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(goodNodes(mk(3, mk(1, mk(3)), mk(4, mk(1), mk(5)))))
''',
}))

# ---- 083 Validate Binary Search Tree ----
LESSONS.append((83, "Validate Binary Search Tree", "Trees", "Medium", 42,
"""Given the root of a binary tree, determine if it is a valid BST.""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def isValidBST(self, root):
        def go(n, lo, hi):
            if not n: return True
            if n.val <= lo or n.val >= hi: return False
            return go(n.left, lo, n.val) and go(n.right, n.val, hi)
        return go(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    r = TreeNode(2, TreeNode(1), TreeNode(3))
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(r)); print(Solution().isValidBST(bad))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var isValidBST = function(root){
    const go = (n, lo, hi) => { if (!n) return true;
        if (n.val <= lo || n.val >= hi) return false;
        return go(n.left, lo, n.val) && go(n.right, n.val, hi); };
    return go(root, -Infinity, Infinity);
};
const r = new TreeNode(2, new TreeNode(1), new TreeNode(3));
const bad = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
console.log(isValidBST(r), isValidBST(bad));
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    boolean go(TreeNode n, long lo, long hi){
        if (n == null) return true;
        if (n.val <= lo || n.val >= hi) return false;
        return go(n.left, lo, n.val) && go(n.right, n.val, hi);
    }
    public boolean isValidBST(TreeNode root){ return go(root, Long.MIN_VALUE, Long.MAX_VALUE); }
    public static void main(String[] a){
        TreeNode r = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        TreeNode bad = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
        System.out.println(new __CLASS__().isValidBST(r)+" "+new __CLASS__().isValidBST(bad));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution {
    bool go(TreeNode* n, long lo, long hi){
        if (!n) return true;
        if (n->val <= lo || n->val >= hi) return false;
        return go(n->left, lo, n->val) && go(n->right, n->val, hi);
    }
public:
    bool isValidBST(TreeNode* root){ return go(root, LONG_MIN, LONG_MAX); }
};
int main(){ auto r = new TreeNode(2); r->left = new TreeNode(1); r->right = new TreeNode(3);
    cout<<Solution().isValidBST(r)<<endl;
    auto b = new TreeNode(5); b->left = new TreeNode(1); b->right = new TreeNode(4);
    b->right->left = new TreeNode(3); b->right->right = new TreeNode(6);
    cout<<Solution().isValidBST(b)<<endl; }
''',
"Go":'''
package main
import ("fmt"; "math")
type TreeNode struct { Val int; Left, Right *TreeNode }
func isValidBST(root *TreeNode) bool {
    var go func(n *TreeNode, lo, hi float64) bool
    go = func(n *TreeNode, lo, hi float64) bool {
        if n == nil { return true }
        v := float64(n.Val); if v <= lo || v >= hi { return false }
        return go(n.Left, lo, v) && go(n.Right, v, hi)
    }
    return go(root, math.Inf(-1), math.Inf(1))
}
func main(){
    r := &TreeNode{Val:2, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:3}}
    bad := &TreeNode{Val:5, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:4, Left:&TreeNode{Val:3}, Right:&TreeNode{Val:6}}}
    fmt.Println(isValidBST(r), isValidBST(bad))
}
''',
"R":'''
isValidBST <- function(root){
    go <- function(n, lo, hi){ if (is.null(n)) return(TRUE)
        if (n$val <= lo || n$val >= hi) return(FALSE)
        go(n$left, lo, n$val) && go(n$right, n$val, hi) }
    go(root, -Inf, Inf)
}
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
print(isValidBST(mk(2, mk(1), mk(3))))
print(isValidBST(mk(5, mk(1), mk(4, mk(3), mk(6)))))
''',
}))

# ---- 084 Kth Smallest Element in a BST ----
LESSONS.append((84, "Kth Smallest Element in a BST", "Trees", "Medium", 42,
"""Given a BST, return the kth smallest value (1-indexed). Use inorder traversal.""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def kthSmallest(self, root, k):
        st, cur = [], root
        while st or cur:
            while cur: st.append(cur); cur = cur.left
            cur = st.pop(); k -= 1
            if k == 0: return cur.val
            cur = cur.right

if __name__ == "__main__":
    r = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(Solution().kthSmallest(r, 1))
    print(Solution().kthSmallest(r, 3))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var kthSmallest = function(root, k){
    const st = []; let cur = root;
    while (st.length || cur){
        while (cur){ st.push(cur); cur = cur.left; }
        cur = st.pop(); if (--k === 0) return cur.val;
        cur = cur.right;
    }
};
const r = new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4));
console.log(kthSmallest(r, 1), kthSmallest(r, 3));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public int kthSmallest(TreeNode root, int k){
        Deque<TreeNode> st = new ArrayDeque<>(); TreeNode cur = root;
        while (!st.isEmpty() || cur != null){
            while (cur != null){ st.push(cur); cur = cur.left; }
            cur = st.pop(); if (--k == 0) return cur.val;
            cur = cur.right;
        }
        return -1;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4));
        System.out.println(new __CLASS__().kthSmallest(r, 1)+" "+new __CLASS__().kthSmallest(r, 3));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution { public:
    int kthSmallest(TreeNode* root, int k){
        stack<TreeNode*> st; TreeNode* cur = root;
        while (!st.empty() || cur){
            while (cur){ st.push(cur); cur = cur->left; }
            cur = st.top(); st.pop(); if (--k == 0) return cur->val;
            cur = cur->right;
        }
        return -1;
    }
};
int main(){ auto r = new TreeNode(3); r->left = new TreeNode(1); r->right = new TreeNode(4);
    r->left->right = new TreeNode(2);
    cout<<Solution().kthSmallest(r,1)<<" "<<Solution().kthSmallest(r,3)<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func kthSmallest(root *TreeNode, k int) int {
    st := []*TreeNode{}; cur := root
    for len(st) > 0 || cur != nil {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        cur = st[len(st)-1]; st = st[:len(st)-1]; k--
        if k == 0 { return cur.Val }
        cur = cur.Right
    }
    return -1
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:1, Right:&TreeNode{Val:2}}, Right:&TreeNode{Val:4}}
    fmt.Println(kthSmallest(r,1), kthSmallest(r,3))
}
''',
"R":'''
inorder <- function(n){ if (is.null(n)) return(c()); c(inorder(n$left), n$val, inorder(n$right)) }
kthSmallest <- function(root, k) inorder(root)[k]
mk <- function(v,l=NULL,r=NULL) list(val=v,left=l,right=r)
r <- mk(3, mk(1, NULL, mk(2)), mk(4))
print(kthSmallest(r, 1)); print(kthSmallest(r, 3))
''',
}))

# ---- 085 Construct Binary Tree from Preorder and Inorder ----
LESSONS.append((85, "Construct Binary Tree from Preorder and Inorder", "Trees", "Medium", 43,
"""Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r
class Solution:
    def buildTree(self, preorder, inorder):
        idx = {v:i for i,v in enumerate(inorder)}
        self.p = 0
        def go(l, r):
            if l > r: return None
            v = preorder[self.p]; self.p += 1
            root = TreeNode(v); m = idx[v]
            root.left = go(l, m-1); root.right = go(m+1, r)
            return root
        return go(0, len(inorder)-1)

def pre(n):
    if not n: return []
    return [n.val] + pre(n.left) + pre(n.right)

if __name__ == "__main__":
    t = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(pre(t))
''',
"JavaScript":'''
function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var buildTree = function(preorder, inorder){
    const idx = new Map(); inorder.forEach((v,i) => idx.set(v,i));
    let p = 0;
    const go = (l, r) => { if (l > r) return null;
        const v = preorder[p++]; const root = new TreeNode(v); const m = idx.get(v);
        root.left = go(l, m-1); root.right = go(m+1, r); return root; };
    return go(0, inorder.length-1);
};
const pre = n => n ? [n.val, ...pre(n.left), ...pre(n.right)] : [];
console.log(pre(buildTree([3,9,20,15,7], [9,3,15,20,7])));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int p = 0; Map<Integer,Integer> idx = new HashMap<>();
    TreeNode go(int[] preorder, int l, int r){
        if (l > r) return null;
        int v = preorder[p++]; TreeNode root = new TreeNode(v); int m = idx.get(v);
        root.left = go(preorder, l, m-1); root.right = go(preorder, m+1, r);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder){
        for (int i=0;i<inorder.length;i++) idx.put(inorder[i], i);
        return go(preorder, 0, inorder.length-1);
    }
    static List<Integer> pre(TreeNode n){ List<Integer> r=new ArrayList<>(); if (n==null) return r;
        r.add(n.val); r.addAll(pre(n.left)); r.addAll(pre(n.right)); return r; }
    public static void main(String[] a){
        TreeNode t = new __CLASS__().buildTree(new int[]{3,9,20,15,7}, new int[]{9,3,15,20,7});
        System.out.println(pre(t));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };
class Solution {
    int p = 0; unordered_map<int,int> idx;
    TreeNode* go(vector<int>& pre, int l, int r){
        if (l > r) return nullptr;
        int v = pre[p++]; TreeNode* root = new TreeNode(v); int m = idx[v];
        root->left = go(pre, l, m-1); root->right = go(pre, m+1, r);
        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder){
        for (int i=0;i<(int)inorder.size();i++) idx[inorder[i]] = i;
        return go(preorder, 0, inorder.size()-1);
    }
};
void pre(TreeNode* n){ if (!n) return; cout<<n->val<<" "; pre(n->left); pre(n->right); }
int main(){ vector<int> p={3,9,20,15,7}, i={9,3,15,20,7};
    auto t = Solution().buildTree(p, i); pre(t); cout<<endl; }
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func buildTree(preorder, inorder []int) *TreeNode {
    idx := map[int]int{}
    for i,v := range inorder { idx[v] = i }
    p := 0
    var go func(l, r int) *TreeNode
    go = func(l, r int) *TreeNode {
        if l > r { return nil }
        v := preorder[p]; p++
        root := &TreeNode{Val: v}; m := idx[v]
        root.Left = go(l, m-1); root.Right = go(m+1, r)
        return root
    }
    return go(0, len(inorder)-1)
}
func pre(n *TreeNode, out *[]int){ if n == nil { return }; *out = append(*out, n.Val); pre(n.Left, out); pre(n.Right, out) }
func main(){ t := buildTree([]int{3,9,20,15,7}, []int{9,3,15,20,7})
    out := []int{}; pre(t, &out); fmt.Println(out) }
''',
"R":'''
buildTree <- function(preorder, inorder){
    if (length(preorder) == 0) return(NULL)
    v <- preorder[1]; m <- which(inorder == v)
    list(val = v,
         left = buildTree(preorder[seq_len(m-1)+1], inorder[seq_len(m-1)]),
         right = buildTree(preorder[(m+1):length(preorder)], inorder[(m+1):length(inorder)]))
}
pre <- function(n) if (is.null(n)) c() else c(n$val, pre(n$left), pre(n$right))
t <- buildTree(c(3,9,20,15,7), c(9,3,15,20,7))
print(pre(t))
''',
}))

write_lessons(LESSONS)
