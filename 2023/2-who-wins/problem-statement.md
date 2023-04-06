## Who Wins

<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Agoda is hosting an event to promote Agoda Cash by organizing a game. The game involves badges numbered from 1 to a given max badge value. The max badge value and a target sum are determined at the beginning of each game. The game is played between two players who take turns selecting a badge. The selected badge cannot be used again. The players then add the value of the badge to a running total, and the player who first reaches or exceeds the target sum is declared the winner. The winner receives Agoda Cash equal to the winning sum.

However, it has come to people's attention that the first player always wins the game. Can you check if it is possible to make the first player always win with the given max badge value and the target sum? Assume both players play optimally.

### Input Format

The first line contains an integer $T$, number of games played.

Each of the next $T$ lines contain 2 space-separated integers, maxBadgeValue and targetSum, selected for the $i^{th}$ game.

### Constraints

$1 \le T \le 20$

$0 \le targetSum \le 300$

<u>Small Input</u>

$1 \le maxBadgeValue \le 8$

<u>Large Input</u>

$1 \le maxBadgeValue \le 20$

### Output Format

For each testcase, print “YES” (without quotes) if the first player wins, otherwise print “NO” (without quotes)

### Sample Input

```
10
6 18
4 0
7 17
4 9
5 1
8 0
5 10
2 2
8 18
6 2
```

### Sample Output

```
NO
YES
YES
NO
YES
YES
YES
YES
NO
YES
```

### Sample Input

```
2
10 11
10 0
```

### Sample Output

```
NO
YES
```

### Explanation

In the first game, no matter what badge the first player chooses, the first player will always lose. First player can choose any badge between 1 to 10. The second player has always an option to choose from the remaining card which will make the sum >= 11. 
For example, player one picks 1, the second player will pick 10 and the sum will reach 11, which is the winning sum and hence the second player wins. So, player one will always lose.
