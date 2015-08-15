# PSU CS350
## Homework 4, Problem 3

There are three materials involved in the manufacture of Wertzial Widgets (WWs): we will call these materials X, Y and Z. Each WW requires a specified amount of X, Y and Z to manufacture. The X, Y and Z come from one of several conglomerations:

* Alphium (A): X
* Betium (B):  Y
* Cetium (C):  Z
* Deltium (D): XXXYYYZ (3X3YZ)
* Etium (E):   YYZZZZZ (2Y5Z)
* Ferium (F):  XXXXXXZZ (6X2Z)
* Gatium (G):  XXYYYYYYZ (2X6YZ)
* Herium (H):  YZZ (Y2Z)

Give worst-case asymptotic polynomial time algorithms for the following problems, and indicate their big-O complexity.

(a) Given: the amount of each material required to manufacture a WW. Solution: a collection of conglomerations of minimum cardinality (number of conglomerations in the collection) that contains sufficient materials to manufacture that WW. You may not waste material. That is, the total amount of materials in the conglomerations should exactly equal the WW materials cost.

(b) Optional Extra Credit: As in (a), but with waste of material allowed.

Hints: Memoization or dynamic programming will be needed here. An implementation is not required, but might be very useful in testing your solution. If you try part (b), the trick is to watch out for cases where adding a conglomeration does not reduce the total amount of material. Otherwise, you may end up with infinite recursion.
