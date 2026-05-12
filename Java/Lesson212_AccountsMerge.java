// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 212 -- Accounts Merge
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.
// =============================================================
import java.util.*;
public class Lesson212_AccountsMerge{
  static Map<String,String> p=new HashMap<>(),own=new HashMap<>();
  static String f(String x){while(!p.get(x).equals(x)){p.put(x,p.get(p.get(x)));x=p.get(x);}return x;}
  public static void main(String[]a){List<List<String>> acc=Arrays.asList(Arrays.asList("A","a@x","b@x"),Arrays.asList("A","b@x","c@x"),Arrays.asList("B","d@x"));for(List<String> x:acc){for(int i=1;i<x.size();i++){p.putIfAbsent(x.get(i),x.get(i));own.put(x.get(i),x.get(0));p.put(f(x.get(i)),f(x.get(1)));}}Map<String,List<String>> g=new HashMap<>();for(String e:p.keySet())g.computeIfAbsent(f(e),k->new ArrayList<>()).add(e);for(List<String> v:g.values()){Collections.sort(v);List<String> r=new ArrayList<>();r.add(own.get(v.get(0)));r.addAll(v);System.out.println(r);}}
}
