// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 217 -- Evaluate Division
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.
// =============================================================
import java.util.*;
public class Lesson217_EvaluateDivision{
  static Map<String,Map<String,Double>> g=new HashMap<>();
  static double dfs(String s,String t,Set<String> seen){if(!g.containsKey(s)||!g.containsKey(t))return -1;if(s.equals(t))return 1;seen.add(s);for(var e:g.get(s).entrySet()){if(seen.contains(e.getKey()))continue;double r=dfs(e.getKey(),t,seen);if(r!=-1)return e.getValue()*r;}return -1;}
  public static void main(String[]a){List<List<String>> eq=Arrays.asList(Arrays.asList("a","b"),Arrays.asList("b","c"));double[] v={2,3};for(int i=0;i<eq.size();i++){g.computeIfAbsent(eq.get(i).get(0),k->new HashMap<>()).put(eq.get(i).get(1),v[i]);g.computeIfAbsent(eq.get(i).get(1),k->new HashMap<>()).put(eq.get(i).get(0),1/v[i]);}List<List<String>> q=Arrays.asList(Arrays.asList("a","c"),Arrays.asList("a","e"));for(var x:q)System.out.println(dfs(x.get(0),x.get(1),new HashSet<>()));}
}
