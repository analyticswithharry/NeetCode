// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 007 -- Lemonade Change
// Category   : Greedy
// Difficulty : Easy
// Study Plan : Day 4
// =============================================================
//
// QUESTION:
//   At a lemonade stand, each lemonade costs $5. Customers stand in line
//   to buy from you and order one lemonade each. Each customer pays with
//   either a $5, $10, or $20 bill. You must provide the correct change to
//   each customer (so the net transaction is $5). Note that you don't have
//   any change in hand at first. Return true if and only if you can provide
//   every customer with correct change.
//
//   Example:
//     Input : bills = [5,5,5,10,20]
//     Output: true
// =============================================================

public class Lesson007_LemonadeChange {
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
        System.out.println(new Lesson007_LemonadeChange().lemonadeChange(new int[]{5,5,5,10,20}));
    }
}
