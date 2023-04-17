[Home](../README.md) | [Solution](./solution.py)

## Don't split our teams

<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Everyone loves a good Hackathon. This year, Agoda is planning a party for all Hackathon participants and needs to arrange transportation. Everyone is super excited and starts to queue up with their teammates. There are $N$ teams from the Hackathon and $A_i$ members on each team. There are $Q$ buses with $q_i$ capacity. Since we do not want to split up teams, each bus can take all team members of one or more consecutive teams in the queue. Also, since Agoda is environmentally conscious, each bus must be filled to its full capacity.

Can you help Agoda figure out how many ways to fill the buses?

### Input Format

The first line will have two space-separated integers $N$ and $Q$, the number of teams and the number of buses.

The next line contains $N$ space-separated integers, $A_i$, size for ith team.

The next $Q$ lines contain an integer $q_i$ the capacity of the $i^{th}$ bus.

### Constraints

$1 \le N \le 2\times 10^5$

$1 \le Q \le 2\times 10^2$

$1 \le A_i \le 5\times 10^{12}$

$1 \le q_i \le 2\times 10^{18}$

### Output Format

Output the number of ways Agoda can fill each bus

### Sample Input

```
8 3
20 30 40 11 29 20 20 10
50 30 20
```

### Sample Output

```
2
2
3
```

### Explanation

For the 1st bus with capacity 50, the following teams can be arranged:

- (20, 30)
- (20, 20, 10)

### Sample Input

```
10 5
11 9 11 9 10 8 10 8 10 11
70 30 80 40 10
```

### Sample Output

```
0
1
0
1
3
```
