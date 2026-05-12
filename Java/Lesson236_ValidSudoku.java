// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 236 -- Valid Sudoku
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Validate 9x9 board: rows, cols, 3x3 boxes have unique 1-9 (ignore '.').
// =============================================================
import java.util.*;
public class Lesson236_ValidSudoku{
  static boolean isValid(char[][] b){Set<String> s=new HashSet<>();for(int i=0;i<9;i++)for(int j=0;j<9;j++){char c=b[i][j];if(c=='.')continue;String r="r"+i+c,co="c"+j+c,k="b"+(i/3)+(j/3)+c;if(!s.add(r)||!s.add(co)||!s.add(k))return false;}return true;}
  public static void main(String[]a){char[][] bd={{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};System.out.println(isValid(bd));}
}
