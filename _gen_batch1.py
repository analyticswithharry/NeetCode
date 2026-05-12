"""
Generates lessons 001-025 in all 6 languages with QUESTION + SOLUTION.
Each file is fully runnable.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
LANG_EXT = {"Python":"py","JavaScript":"js","Java":"java","CPP":"cpp","Go":"go","R":"R"}
COMMENT  = {"Python":"#","JavaScript":"//","Java":"//","CPP":"//","Go":"//","R":"#"}

def slug(t):
    s = re.sub(r"[^a-zA-Z0-9 ]", " ", t).strip().lower()
    return re.sub(r"\s+", "_", s)

def java_class(num, t):
    parts = re.sub(r"[^a-zA-Z0-9 ]", " ", t).split()
    return f"Lesson{num:03d}_" + "".join(p.capitalize() for p in parts)

def header(lang, num, title, cat, diff, day, question):
    c = COMMENT[lang]
    head = [
        f"{c} =============================================================",
        f"{c} MIT License | @analyticswithharry2026",
        f"{c} GitHub  : https://github.com/analyticswithharry",
        f"{c} YouTube : Analytics with Harry",
        f"{c} =============================================================",
        f"{c} Lesson     : {num:03d} -- {title}",
        f"{c} Category   : {cat}",
        f"{c} Difficulty : {diff}",
        f"{c} Study Plan : Day {day}",
        f"{c} =============================================================",
        f"{c}",
        f"{c} QUESTION:",
    ]
    for line in question.strip().splitlines():
        head.append(f"{c}   {line}".rstrip())
    head.append(f"{c} =============================================================")
    head.append("")
    return "\n".join(head)

def fname(lang, num, title):
    if lang == "Java": return f"{java_class(num,title)}.java"
    return f"Lesson_{num:03d}_{slug(title)}.{LANG_EXT[lang]}"

# (num, title, category, difficulty, day, question, {lang: body})
LESSONS = []

# ============================================================
# 001 - Reverse String  (Two Pointers, Easy)
# ============================================================
LESSONS.append((1,"Reverse String","Two Pointers","Easy",1,
"""Write a function that reverses a string. The input string is given as
an array of characters s. You must do this by modifying the input array
in-place with O(1) extra memory.

Example:
  Input : s = ['h','e','l','l','o']
  Output: ['o','l','l','e','h']""",
{
"Python":'''
class Solution:
    def reverseString(self, s: list) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    s = list("hello")
    Solution().reverseString(s)
    print(s)  # ['o','l','l','e','h']
''',
"JavaScript":'''
var reverseString = function(s) {
    let l = 0, r = s.length - 1;
    while (l < r) { [s[l], s[r]] = [s[r], s[l]]; l++; r--; }
};

const arr = ["h","e","l","l","o"];
reverseString(arr);
console.log(arr); // ['o','l','l','e','h']
''',
"Java":'''
import java.util.Arrays;

public class __CLASS__ {
    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while (l < r) { char t = s[l]; s[l++] = s[r]; s[r--] = t; }
    }
    public static void main(String[] args) {
        char[] s = {'h','e','l','l','o'};
        new __CLASS__().reverseString(s);
        System.out.println(Arrays.toString(s));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = (int)s.size() - 1;
        while (l < r) swap(s[l++], s[r--]);
    }
};

int main() {
    vector<char> s = {'h','e','l','l','o'};
    Solution().reverseString(s);
    for (char c : s) cout << c;
    cout << endl;
}
''',
"Go":'''
package main

import "fmt"

func reverseString(s []byte) {
    l, r := 0, len(s)-1
    for l < r { s[l], s[r] = s[r], s[l]; l++; r-- }
}

func main() {
    s := []byte("hello")
    reverseString(s)
    fmt.Println(string(s))
}
''',
"R":'''
reverseString <- function(s) {
    rev(s)
}

s <- c("h","e","l","l","o")
print(reverseString(s))
''',
}))

# ============================================================
# 002 - Two Sum II Input Array Is Sorted
# ============================================================
LESSONS.append((2,"Two Sum II Input Array Is Sorted","Two Pointers","Medium",1,
"""Given a 1-indexed sorted array of integers `numbers`, find two numbers
such that they add up to a specific `target`. Return their 1-based
indices as [index1, index2]. Use O(1) extra space.

Example:
  Input : numbers = [2,7,11,15], target = 9
  Output: [1,2]   (because 2 + 7 = 9)""",
{
"Python":'''
class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l+1, r+1]
            if s < target: l += 1
            else: r -= 1
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))  # [1, 2]
''',
"JavaScript":'''
var twoSum = function(numbers, target) {
    let l = 0, r = numbers.length - 1;
    while (l < r) {
        const s = numbers[l] + numbers[r];
        if (s === target) return [l+1, r+1];
        if (s < target) l++; else r--;
    }
    return [];
};

console.log(twoSum([2,7,11,15], 9)); // [1, 2]
''',
"Java":'''
import java.util.Arrays;

public class __CLASS__ {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s == target) return new int[]{l+1, r+1};
            if (s < target) l++; else r--;
        }
        return new int[]{};
    }
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new __CLASS__().twoSum(new int[]{2,7,11,15}, 9)));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = (int)numbers.size() - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s == target) return {l+1, r+1};
            if (s < target) l++; else r--;
        }
        return {};
    }
};

int main() {
    vector<int> v = {2,7,11,15};
    auto r = Solution().twoSum(v, 9);
    cout << r[0] << "," << r[1] << endl;
}
''',
"Go":'''
package main

import "fmt"

func twoSum(numbers []int, target int) []int {
    l, r := 0, len(numbers)-1
    for l < r {
        s := numbers[l] + numbers[r]
        if s == target { return []int{l+1, r+1} }
        if s < target { l++ } else { r-- }
    }
    return []int{}
}

func main() { fmt.Println(twoSum([]int{2,7,11,15}, 9)) }
''',
"R":'''
twoSum <- function(numbers, target) {
    l <- 1; r <- length(numbers)
    while (l < r) {
        s <- numbers[l] + numbers[r]
        if (s == target) return(c(l, r))
        if (s < target) l <- l + 1 else r <- r - 1
    }
    integer(0)
}

print(twoSum(c(2,7,11,15), 9))  # 1 2
''',
}))

# ============================================================
# 003 - Reverse Linked List
# ============================================================
LESSONS.append((3,"Reverse Linked List","Linked List","Easy",2,
"""Given the head of a singly linked list, reverse the list and return
the new head.

Example:
  Input : 1 -> 2 -> 3 -> 4 -> 5
  Output: 5 -> 4 -> 3 -> 2 -> 1""",
{
"Python":'''
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

def to_list(h):
    out = []
    while h: out.append(h.val); h = h.next
    return out

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(to_list(Solution().reverseList(head)))  # [5,4,3,2,1]
''',
"JavaScript":'''
function ListNode(val, next) { this.val = val ?? 0; this.next = next ?? null; }

var reverseList = function(head) {
    let prev = null;
    while (head) { const n = head.next; head.next = prev; prev = head; head = n; }
    return prev;
};

const toArr = h => { const a = []; while (h) { a.push(h.val); h = h.next; } return a; };
const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
console.log(toArr(reverseList(head))); // [5,4,3,2,1]
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) { ListNode n = head.next; head.next = prev; prev = head; head = n; }
        return prev;
    }

    public static void main(String[] args) {
        ListNode h = new ListNode(1); h.next = new ListNode(2); h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(4); h.next.next.next.next = new ListNode(5);
        ListNode r = new __CLASS__().reverseList(h);
        List<Integer> out = new ArrayList<>();
        while (r != null) { out.add(r.val); r = r.next; }
        System.out.println(out);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

struct ListNode { int val; ListNode* next; ListNode(int v):val(v),next(nullptr){} };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) { ListNode* n = head->next; head->next = prev; prev = head; head = n; }
        return prev;
    }
};

int main() {
    auto* h = new ListNode(1); h->next = new ListNode(2); h->next->next = new ListNode(3);
    h->next->next->next = new ListNode(4); h->next->next->next->next = new ListNode(5);
    auto* r = Solution().reverseList(h);
    while (r) { cout << r->val << " "; r = r->next; }
    cout << endl;
}
''',
"Go":'''
package main

import "fmt"

type ListNode struct { Val int; Next *ListNode }

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    for head != nil { n := head.Next; head.Next = prev; prev = head; head = n }
    return prev
}

func main() {
    h := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
    r := reverseList(h)
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }
    fmt.Println()
}
''',
"R":'''
# R lacks built-in linked list; represent as a vector and reverse.
reverseList <- function(v) rev(v)
print(reverseList(c(1,2,3,4,5)))  # 5 4 3 2 1
''',
}))

# ============================================================
# 004 - Merge Two Sorted Lists
# ============================================================
LESSONS.append((4,"Merge Two Sorted Lists","Linked List","Easy",2,
"""You are given the heads of two sorted linked lists list1 and list2.
Merge them into one sorted list and return its head.

Example:
  Input : 1->2->4, 1->3->4
  Output: 1->1->2->3->4->4""",
{
"Python":'''
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

class Solution:
    def mergeTwoLists(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val: tail.next, a = a, a.next
            else:              tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

def build(vs):
    d = ListNode(); t = d
    for v in vs: t.next = ListNode(v); t = t.next
    return d.next

def to_list(h):
    out = []
    while h: out.append(h.val); h = h.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().mergeTwoLists(build([1,2,4]), build([1,3,4]))))
''',
"JavaScript":'''
function ListNode(val, next) { this.val = val ?? 0; this.next = next ?? null; }

var mergeTwoLists = function(a, b) {
    const d = new ListNode(); let t = d;
    while (a && b) {
        if (a.val <= b.val) { t.next = a; a = a.next; }
        else { t.next = b; b = b.next; }
        t = t.next;
    }
    t.next = a || b;
    return d.next;
};

const build = vs => { const d = new ListNode(); let t = d; for (const v of vs) { t.next = new ListNode(v); t = t.next; } return d.next; };
const toArr = h => { const r = []; while (h) { r.push(h.val); h = h.next; } return r; };
console.log(toArr(mergeTwoLists(build([1,2,4]), build([1,3,4]))));
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} }

    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        ListNode d = new ListNode(), t = d;
        while (a != null && b != null) {
            if (a.val <= b.val) { t.next = a; a = a.next; }
            else { t.next = b; b = b.next; }
            t = t.next;
        }
        t.next = (a != null) ? a : b;
        return d.next;
    }

    static ListNode build(int[] v) { ListNode d = new ListNode(), t = d;
        for (int x : v) { t.next = new ListNode(x); t = t.next; } return d.next; }

    public static void main(String[] args) {
        ListNode r = new __CLASS__().mergeTwoLists(build(new int[]{1,2,4}), build(new int[]{1,3,4}));
        List<Integer> out = new ArrayList<>();
        while (r != null) { out.add(r.val); r = r.next; }
        System.out.println(out);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

struct ListNode { int val; ListNode* next; ListNode(int v=0):val(v),next(nullptr){} };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        ListNode d, *t = &d;
        while (a && b) {
            if (a->val <= b->val) { t->next = a; a = a->next; }
            else { t->next = b; b = b->next; }
            t = t->next;
        }
        t->next = a ? a : b;
        return d.next;
    }
};

ListNode* build(vector<int> v){ ListNode* d=new ListNode(); ListNode* t=d;
    for(int x: v){ t->next=new ListNode(x); t=t->next;} return d->next; }

int main() {
    auto* r = Solution().mergeTwoLists(build({1,2,4}), build({1,3,4}));
    while (r) { cout << r->val << " "; r = r->next; }
    cout << endl;
}
''',
"Go":'''
package main

import "fmt"

type ListNode struct { Val int; Next *ListNode }

func mergeTwoLists(a, b *ListNode) *ListNode {
    d := &ListNode{}; t := d
    for a != nil && b != nil {
        if a.Val <= b.Val { t.Next = a; a = a.Next } else { t.Next = b; b = b.Next }
        t = t.Next
    }
    if a != nil { t.Next = a } else { t.Next = b }
    return d.Next
}

func build(v []int) *ListNode { d := &ListNode{}; t := d
    for _, x := range v { t.Next = &ListNode{Val:x}; t = t.Next }
    return d.Next }

func main() {
    r := mergeTwoLists(build([]int{1,2,4}), build([]int{1,3,4}))
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }
    fmt.Println()
}
''',
"R":'''
# Merge two already-sorted vectors to mimic merging two sorted lists.
mergeTwoLists <- function(a, b) {
    out <- integer(length(a) + length(b)); i <- 1; j <- 1; k <- 1
    while (i <= length(a) && j <= length(b)) {
        if (a[i] <= b[j]) { out[k] <- a[i]; i <- i + 1 } else { out[k] <- b[j]; j <- j + 1 }
        k <- k + 1
    }
    while (i <= length(a)) { out[k] <- a[i]; i <- i + 1; k <- k + 1 }
    while (j <= length(b)) { out[k] <- b[j]; j <- j + 1; k <- k + 1 }
    out
}

print(mergeTwoLists(c(1,2,4), c(1,3,4)))  # 1 1 2 3 4 4
''',
}))

# ============================================================
# 005 - Binary Tree Inorder Traversal
# ============================================================
LESSONS.append((5,"Binary Tree Inorder Traversal","Trees","Easy",3,
"""Given the root of a binary tree, return the inorder (Left, Root, Right)
traversal of its nodes' values.

Example:
  Input : root = [1,null,2,3]
  Output: [1, 3, 2]""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def inorderTraversal(self, root):
        out, stack, cur = [], [], root
        while cur or stack:
            while cur: stack.append(cur); cur = cur.left
            cur = stack.pop(); out.append(cur.val); cur = cur.right
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().inorderTraversal(root))  # [1, 3, 2]
''',
"JavaScript":'''
function TreeNode(v, l, r) { this.val = v ?? 0; this.left = l ?? null; this.right = r ?? null; }

var inorderTraversal = function(root) {
    const out = [], stack = []; let cur = root;
    while (cur || stack.length) {
        while (cur) { stack.push(cur); cur = cur.left; }
        cur = stack.pop(); out.push(cur.val); cur = cur.right;
    }
    return out;
};

console.log(inorderTraversal(new TreeNode(1, null, new TreeNode(2, new TreeNode(3)))));
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>(); Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop(); out.add(cur.val); cur = cur.right;
        }
        return out;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1); root.right = new TreeNode(2); root.right.left = new TreeNode(3);
        System.out.println(new __CLASS__().inorderTraversal(root));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> out; stack<TreeNode*> st; TreeNode* cur = root;
        while (cur || !st.empty()) {
            while (cur) { st.push(cur); cur = cur->left; }
            cur = st.top(); st.pop(); out.push_back(cur->val); cur = cur->right;
        }
        return out;
    }
};

int main() {
    auto* r = new TreeNode(1); r->right = new TreeNode(2); r->right->left = new TreeNode(3);
    for (int v : Solution().inorderTraversal(r)) cout << v << " ";
    cout << endl;
}
''',
"Go":'''
package main

import "fmt"

type TreeNode struct { Val int; Left, Right *TreeNode }

func inorderTraversal(root *TreeNode) []int {
    out := []int{}; st := []*TreeNode{}; cur := root
    for cur != nil || len(st) > 0 {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        n := len(st) - 1; cur = st[n]; st = st[:n]
        out = append(out, cur.Val); cur = cur.Right
    }
    return out
}

func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(inorderTraversal(r))
}
''',
"R":'''
# Tree as nested list: list(val, left, right). NULL for missing children.
inorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(inorderTraversal(node$left), node$val, inorderTraversal(node$right))
}

root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(inorderTraversal(root))  # 1 3 2
''',
}))

# ============================================================
# 006 - Binary Tree Preorder Traversal
# ============================================================
LESSONS.append((6,"Binary Tree Preorder Traversal","Trees","Easy",3,
"""Given the root of a binary tree, return the preorder (Root, Left, Right)
traversal of its nodes' values.

Example:
  Input : root = [1,null,2,3]
  Output: [1, 2, 3]""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def preorderTraversal(self, root):
        if not root: return []
        out, st = [], [root]
        while st:
            n = st.pop(); out.append(n.val)
            if n.right: st.append(n.right)
            if n.left:  st.append(n.left)
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().preorderTraversal(root))  # [1, 2, 3]
''',
"JavaScript":'''
function TreeNode(v, l, r) { this.val = v ?? 0; this.left = l ?? null; this.right = r ?? null; }

var preorderTraversal = function(root) {
    if (!root) return [];
    const out = [], st = [root];
    while (st.length) {
        const n = st.pop(); out.push(n.val);
        if (n.right) st.push(n.right);
        if (n.left)  st.push(n.left);
    }
    return out;
};

console.log(preorderTraversal(new TreeNode(1, null, new TreeNode(2, new TreeNode(3)))));
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> st = new ArrayDeque<>(); st.push(root);
        while (!st.isEmpty()) {
            TreeNode n = st.pop(); out.add(n.val);
            if (n.right != null) st.push(n.right);
            if (n.left  != null) st.push(n.left);
        }
        return out;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1); root.right = new TreeNode(2); root.right.left = new TreeNode(3);
        System.out.println(new __CLASS__().preorderTraversal(root));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> out; if (!root) return out;
        stack<TreeNode*> st; st.push(root);
        while (!st.empty()) {
            auto* n = st.top(); st.pop(); out.push_back(n->val);
            if (n->right) st.push(n->right);
            if (n->left)  st.push(n->left);
        }
        return out;
    }
};

int main() {
    auto* r = new TreeNode(1); r->right = new TreeNode(2); r->right->left = new TreeNode(3);
    for (int v : Solution().preorderTraversal(r)) cout << v << " ";
    cout << endl;
}
''',
"Go":'''
package main

import "fmt"

type TreeNode struct { Val int; Left, Right *TreeNode }

func preorderTraversal(root *TreeNode) []int {
    if root == nil { return []int{} }
    out := []int{}; st := []*TreeNode{root}
    for len(st) > 0 {
        n := st[len(st)-1]; st = st[:len(st)-1]
        out = append(out, n.Val)
        if n.Right != nil { st = append(st, n.Right) }
        if n.Left  != nil { st = append(st, n.Left) }
    }
    return out
}

func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(preorderTraversal(r))
}
''',
"R":'''
preorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(node$val, preorderTraversal(node$left), preorderTraversal(node$right))
}

root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(preorderTraversal(root))  # 1 2 3
''',
}))

# ============================================================
# 007 - Lemonade Change
# ============================================================
LESSONS.append((7,"Lemonade Change","Greedy","Easy",4,
"""At a lemonade stand, each lemonade costs $5. Customers stand in line
to buy from you and order one lemonade each. Each customer pays with
either a $5, $10, or $20 bill. You must provide the correct change to
each customer (so the net transaction is $5). Note that you don't have
any change in hand at first. Return true if and only if you can provide
every customer with correct change.

Example:
  Input : bills = [5,5,5,10,20]
  Output: true""",
{
"Python":'''
class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for b in bills:
            if b == 5: five += 1
            elif b == 10:
                if not five: return False
                five -= 1; ten += 1
            else:
                if ten and five: ten -= 1; five -= 1
                elif five >= 3:  five -= 3
                else: return False
        return True

if __name__ == "__main__":
    print(Solution().lemonadeChange([5,5,5,10,20]))  # True
''',
"JavaScript":'''
var lemonadeChange = function(bills) {
    let five = 0, ten = 0;
    for (const b of bills) {
        if (b === 5) five++;
        else if (b === 10) { if (!five) return false; five--; ten++; }
        else {
            if (ten && five) { ten--; five--; }
            else if (five >= 3) five -= 3;
            else return false;
        }
    }
    return true;
};

console.log(lemonadeChange([5,5,5,10,20])); // true
''',
"Java":'''
public class __CLASS__ {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int b : bills) {
            if (b == 5) five++;
            else if (b == 10) { if (five == 0) return false; five--; ten++; }
            else {
                if (ten > 0 && five > 0) { ten--; five--; }
                else if (five >= 3) five -= 3;
                else return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().lemonadeChange(new int[]{5,5,5,10,20}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for (int b : bills) {
            if (b == 5) five++;
            else if (b == 10) { if (!five) return false; five--; ten++; }
            else {
                if (ten && five) { ten--; five--; }
                else if (five >= 3) five -= 3;
                else return false;
            }
        }
        return true;
    }
};

int main() {
    vector<int> v = {5,5,5,10,20};
    cout << boolalpha << Solution().lemonadeChange(v) << endl;
}
''',
"Go":'''
package main

import "fmt"

func lemonadeChange(bills []int) bool {
    five, ten := 0, 0
    for _, b := range bills {
        switch b {
        case 5: five++
        case 10:
            if five == 0 { return false }
            five--; ten++
        default:
            if ten > 0 && five > 0 { ten--; five-- } else if five >= 3 { five -= 3 } else { return false }
        }
    }
    return true
}

func main() { fmt.Println(lemonadeChange([]int{5,5,5,10,20})) }
''',
"R":'''
lemonadeChange <- function(bills) {
    five <- 0; ten <- 0
    for (b in bills) {
        if (b == 5) five <- five + 1
        else if (b == 10) { if (five == 0) return(FALSE); five <- five - 1; ten <- ten + 1 }
        else {
            if (ten > 0 && five > 0) { ten <- ten - 1; five <- five - 1 }
            else if (five >= 3) five <- five - 3
            else return(FALSE)
        }
    }
    TRUE
}

print(lemonadeChange(c(5,5,5,10,20)))  # TRUE
''',
}))

# ============================================================
# 008 - Maximum Subarray (Kadane)
# ============================================================
LESSONS.append((8,"Maximum Subarray","Greedy","Medium",4,
"""Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.

Example:
  Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6   (subarray [4,-1,2,1])""",
{
"Python":'''
class Solution:
    def maxSubArray(self, nums):
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
''',
"JavaScript":'''
var maxSubArray = function(nums) {
    let best = nums[0], cur = nums[0];
    for (let i = 1; i < nums.length; i++) {
        cur = Math.max(nums[i], cur + nums[i]);
        best = Math.max(best, cur);
    }
    return best;
};

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])); // 6
''',
"Java":'''
public class __CLASS__ {
    public int maxSubArray(int[] nums) {
        int best = nums[0], cur = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], cur + nums[i]);
            best = Math.max(best, cur);
        }
        return best;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best = nums[0], cur = nums[0];
        for (int i = 1; i < (int)nums.size(); ++i) {
            cur = max(nums[i], cur + nums[i]);
            best = max(best, cur);
        }
        return best;
    }
};

int main() {
    vector<int> v = {-2,1,-3,4,-1,2,1,-5,4};
    cout << Solution().maxSubArray(v) << endl;
}
''',
"Go":'''
package main

import "fmt"

func maxSubArray(nums []int) int {
    best, cur := nums[0], nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > cur + nums[i] { cur = nums[i] } else { cur += nums[i] }
        if cur > best { best = cur }
    }
    return best
}

func main() { fmt.Println(maxSubArray([]int{-2,1,-3,4,-1,2,1,-5,4})) }
''',
"R":'''
maxSubArray <- function(nums) {
    best <- nums[1]; cur <- nums[1]
    for (i in 2:length(nums)) { cur <- max(nums[i], cur + nums[i]); best <- max(best, cur) }
    best
}

print(maxSubArray(c(-2,1,-3,4,-1,2,1,-5,4)))  # 6
''',
}))

# ============================================================
# 009 - Binary Search
# ============================================================
LESSONS.append((9,"Binary Search","Binary Search","Easy",5,
"""Given a sorted (ascending) array of integers nums and a target, return
the index of target if it exists, otherwise -1. You must run in O(log n).

Example:
  Input : nums = [-1,0,3,5,9,12], target = 9
  Output: 4""",
{
"Python":'''
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[m] < target: l = m + 1
            else: r = m - 1
        return -1

if __name__ == "__main__":
    print(Solution().search([-1,0,3,5,9,12], 9))  # 4
''',
"JavaScript":'''
var search = function(nums, target) {
    let l = 0, r = nums.length - 1;
    while (l <= r) {
        const m = (l + r) >> 1;
        if (nums[m] === target) return m;
        if (nums[m] < target) l = m + 1; else r = m - 1;
    }
    return -1;
};

console.log(search([-1,0,3,5,9,12], 9)); // 4
''',
"Java":'''
public class __CLASS__ {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) >>> 1;
            if (nums[m] == target) return m;
            if (nums[m] < target) l = m + 1; else r = m - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().search(new int[]{-1,0,3,5,9,12}, 9));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size() - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) return m;
            if (nums[m] < target) l = m + 1; else r = m - 1;
        }
        return -1;
    }
};

int main() {
    vector<int> v = {-1,0,3,5,9,12};
    cout << Solution().search(v, 9) << endl;
}
''',
"Go":'''
package main

import "fmt"

func search(nums []int, target int) int {
    l, r := 0, len(nums)-1
    for l <= r {
        m := (l + r) / 2
        if nums[m] == target { return m }
        if nums[m] < target { l = m + 1 } else { r = m - 1 }
    }
    return -1
}

func main() { fmt.Println(search([]int{-1,0,3,5,9,12}, 9)) }
''',
"R":'''
binarySearch <- function(nums, target) {
    l <- 1; r <- length(nums)
    while (l <= r) {
        m <- (l + r) %/% 2
        if (nums[m] == target) return(m - 1L)  # 0-based
        if (nums[m] < target) l <- m + 1 else r <- m - 1
    }
    -1L
}

print(binarySearch(c(-1,0,3,5,9,12), 9))  # 4
''',
}))

# ============================================================
# 010 - Search Insert Position
# ============================================================
LESSONS.append((10,"Search Insert Position","Binary Search","Easy",5,
"""Given a sorted array of distinct integers and a target, return the
index if the target is found. If not, return the index where it would
be inserted in order. Must run in O(log n).

Example:
  Input : nums = [1,3,5,6], target = 5    Output: 2
  Input : nums = [1,3,5,6], target = 2    Output: 1""",
{
"Python":'''
class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            else: r = m
        return l

if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))  # 2
    print(Solution().searchInsert([1,3,5,6], 2))  # 1
''',
"JavaScript":'''
var searchInsert = function(nums, target) {
    let l = 0, r = nums.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (nums[m] < target) l = m + 1; else r = m;
    }
    return l;
};

console.log(searchInsert([1,3,5,6], 5)); // 2
console.log(searchInsert([1,3,5,6], 2)); // 1
''',
"Java":'''
public class __CLASS__ {
    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (nums[m] < target) l = m + 1; else r = m;
        }
        return l;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().searchInsert(new int[]{1,3,5,6}, 5));
        System.out.println(new __CLASS__().searchInsert(new int[]{1,3,5,6}, 2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < target) l = m + 1; else r = m;
        }
        return l;
    }
};

int main() {
    vector<int> v = {1,3,5,6};
    cout << Solution().searchInsert(v, 5) << endl;
    cout << Solution().searchInsert(v, 2) << endl;
}
''',
"Go":'''
package main

import "fmt"

func searchInsert(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        m := (l + r) / 2
        if nums[m] < target { l = m + 1 } else { r = m }
    }
    return l
}

func main() {
    fmt.Println(searchInsert([]int{1,3,5,6}, 5))
    fmt.Println(searchInsert([]int{1,3,5,6}, 2))
}
''',
"R":'''
searchInsert <- function(nums, target) {
    l <- 1; r <- length(nums) + 1
    while (l < r) {
        m <- (l + r) %/% 2
        if (nums[m] < target) l <- m + 1 else r <- m
    }
    l - 1L
}

print(searchInsert(c(1,3,5,6), 5))  # 2
print(searchInsert(c(1,3,5,6), 2))  # 1
''',
}))

CPP_PORTABLE = "#include <vector>\n#include <string>\n#include <iostream>\n#include <stack>\n#include <queue>\n#include <algorithm>"

def write_all():
    print(f"Writing {len(LESSONS)} lessons x 6 langs = {len(LESSONS)*6} files...")
    for num, title, cat, diff, day, q, codes in LESSONS:
        for lang in LANG_EXT:
            body = codes[lang].replace("__CLASS__", java_class(num, title))
            if lang == "CPP":
                body = body.replace("#include <bits/stdc++.h>", CPP_PORTABLE)
            prefix = "//go:build ignore\n\n" if lang == "Go" else ""
            content = prefix + header(lang, num, title, cat, diff, day, q) + body
            if not content.endswith("\n"): content += "\n"
            d = os.path.join(ROOT, lang); os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, fname(lang, num, title)), "w") as f:
                f.write(content)
    print("Done.")

if __name__ == "__main__":
    write_all()
