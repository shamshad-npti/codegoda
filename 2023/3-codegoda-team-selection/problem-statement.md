## Codegoda Team Selection

<sup>Section: 3, Score: 33, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

The much-awaited Codegoda is here. The organizer is trying to form teams to write and test problems, but forming teams is not an easy task. The organizer has made many attempts but every time a team is missing a tester or has only testers. A good team should have a mentor, and some volunteer(s) to write and test problems. The organizer writes an algorithm to form perfect teams, but his algorithm is not efficient for large constraints. Now, you must help him to write a slightly different solution for large constraints.

There are $M$ volunteers who are willing to only write problems and $N$ volunteers who are willing to do both test and write problems. The organizer is trying to form $K$ teams with at least one volunteer who is willing to test problems and at least one problem writer in each team. The organizer also needs $K$ out of $X$ mentors who will guide each team. These mentors are not from $M+N$ volunteers. Each team must have a mentor and a mentor can be part of at most one team. Each volunteer must be part of one and only one team. Can you help the organizer to find how many unique ways he can form $K$ teams? Two ways to form teams will be considered different if there is at least one volunteer with a different mentor.

### Input Format

The first line of the input contains an integer $T$ the number of test cases.

The next $T$ lines contain four space-separated integers, $M$, $N$, $X$, and $K$ as described above in each line.

### Constraints

$1 \le T \le 10^5$

$1 \le M, N, X \le 10^5$

$1 \le K \le 200$

$K \le N, X$

### Output Format

For each test case print one integer, the number of ways to form teams, in a new line. The answer can be large, so print it modulo 1,000,000,007 (AKA James Bond Prime).

### Sample Input

```
2
2 2 2 2
3 3 3 3
```

### Sample Output

```
8
162
```

### Explanation

In 1st case,  
If we put only one volunteer of type N in a team and others in the second team, we can form the teams in 4 possible ways.

If we put one volunteer of type N and one volunteer of type M in each team, we can form the teams in 4 possible ways too.

So, we can make teams in 8 possible ways.

### Sample Input

```
3
3 5 9 1
6 3 3 3
8 10 1 1
```

### Sample Output

```
9
4374
1
```
