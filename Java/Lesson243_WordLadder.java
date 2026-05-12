// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 243 -- Word Ladder
// Category   : Graphs
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   Shortest transformation sequence length from begin to end. BFS with wildcard buckets.
// =============================================================
import java.util.*;
public class Lesson243_WordLadder{
  static int ladderLength(String b,String e,List<String> wl){Set<String> ws=new HashSet<>(wl);if(!ws.contains(e))return 0;int L=b.length();Map<String,List<String>> buc=new HashMap<>();for(String w:ws)for(int i=0;i<L;i++){String k=w.substring(0,i)+"*"+w.substring(i+1);buc.computeIfAbsent(k,z->new ArrayList<>()).add(w);}Deque<Object[]> q=new ArrayDeque<>();q.add(new Object[]{b,1});Set<String> seen=new HashSet<>();seen.add(b);while(!q.isEmpty()){Object[] x=q.poll();String w=(String)x[0];int d=(int)x[1];if(w.equals(e))return d;for(int i=0;i<L;i++){String k=w.substring(0,i)+"*"+w.substring(i+1);for(String n:buc.getOrDefault(k,new ArrayList<>()))if(seen.add(n))q.add(new Object[]{n,d+1});}}return 0;}
  public static void main(String[]a){System.out.println(ladderLength("hit","cog",Arrays.asList("hot","dot","dog","lot","log","cog")));}
}
