## Tower of Codegoda
<sup>Section: 1, Score: 12, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

To challenge Codegoda throne, you need to conquer Codegoda tower. The tower consists of N floors. In each floor have one boss with power bi. After the boss is defeated, the boss's spirit will become your foot soldier and join your team with power si. While you have the strength to defeat all the bosses, your foot soldiers, who have powers less than that of the boss will be eliminated. 

Luckily, you have some information about the tower, and you want to know how many foot soldiers you will be able to bring back after defeating the last boss (Nth floor.) 

### Input Format
The first line will contain an integer $N$, denoting the number of floors. 

The second line will have $N$ space separated integers $b_i$, representing the power of the boss in the ith floor. 

The third line will have $N$ space separated integers $s_i$, representing the power of the foot soldier after the ith boss is defeated. 

### Constraints
$1 \le N \le 10^6$

$1 \le b_i \le 10^5$

$1 \le s_i \le 10^5$

### Output Format
An integer, representing the number of foot soldiers after defeating the last boss.

### Sample Input
```
5
1 2 3 4 5
3 3 3 8 10
```
### Sample Output
```
2
```
### Explanation
After defeating floor 1 boss, foot soldiers = `[3]`

After defeating floor 2 boss, foot soldiers = `[3, 3]`

After defeating floor 3 boss, foot soldiers = `[3, 3, 3]`

After defeating floor 4 boss, foot soldiers = `[8]`

After defeating floor 5 boss, foot soldiers = `[8, 10]`

Hence answer is 2

### Sample Input
```
5
1 4 2 3 2
3 2 1 4 2
```
### Sample Output
```
2
```
