## Can Alice Finish the Game?

<sup>Section: 3, Score: 33, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Alice plays a game with $K$ levels numbered from $1$ to $K$. To complete the game Alice must pass all the levels in order. If Alice passes a level, she can move to the next level. If she fails a level, she must restart the game from level $1$. The probability of passing level $i$ is $\frac{1}{R_i}$. Passing or failing a level is independent of everything that happened in the game before. It takes $1$ hour for Alice to pass or fail a level, and she does not need extra time to move to the next level or go to level $1$ again in case of failing a level.

If Alice has a total of $N$ hours, what is the probability that she can complete the game? 
Output the probability modulo $1,000,000,007$ (AKA James Bond Prime).

### Input Format

The first line contains two space-separated integers $K$ and $N$.

The next line contains $K$ space separated integers where ith integer $R_i$ is probability $\frac{1}{R_i}$ of passing level $i$.

### Constraints

$1 \le R_i \le 100$ for all $i$, where $1 \le i \le K$

**Small Testcase**

$1 \le K \le 2$

$1 \le N \le 10$

**Medium Testcase**

$1 \le K \le 5$

$1 \le N \le 10^5$

**Large Testcase**

$1 \le K \le 50$

$1 \le N \le 10^{18}$

### Output Format

Print, an integer, the required probability modulo 1e9+7 (i.e. 1,000,000,007)

### Sample Input

```
2 2
2 2
```

### Sample Output

```
250000002
```

### Explanation

Alice has a chance of $\frac{1}{2}$ to pass level one in the first hour, and a chance of $\frac{1}{2}$ to pass level two in the second hour if she already passed level one. Therefore, the probability of her finishing the game in two hours is $\frac{1}{4}$. When calculating this probability modulo 1e9+7, the result is $250000002$.

### Sample Input

```
2 1
2 2
```

### Sample Output

```
0
```

### Explanation

In order to pass both level 1 and level 2, it takes at least two hours. Since Alice only played for one hour, she did not pass the game, and the probability of her finishing the game is zero.
