# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 007 -- Lemonade Change
# Category   : Greedy
# Difficulty : Easy
# Study Plan : Day 4
# =============================================================
#
# QUESTION:
#   At a lemonade stand, each lemonade costs $5. Customers stand in line
#   to buy from you and order one lemonade each. Each customer pays with
#   either a $5, $10, or $20 bill. You must provide the correct change to
#   each customer (so the net transaction is $5). Note that you don't have
#   any change in hand at first. Return true if and only if you can provide
#   every customer with correct change.
#
#   Example:
#     Input : bills = [5,5,5,10,20]
#     Output: true
# =============================================================

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
