[Home](../README.md) | [Solution](./solution.py)

## Arrange Goodies

<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

When an employee joins Agoda, they receive a box containing a set number of goodies, each with a value tag attached. All boxes are equivalent and contain an equal number of goodies.

However, on one occasion, the delivery team makes a mistake and sends two boxes with an equal number of goodies, but with different values.

You are given the task of making both the boxes equivalent with the following operation:

Choose two indices $i$ and $j$ and swap the $i^{th}$ goodie of box1 with the $j^{th}$ goodie of box2. The cost of the swap is $min(box1[i], box2[j])$.

Two goodies are equivalent if they have the same value. Two boxes are equivalent if for every goodie in the first box, there is a unique equivalent goodie in the second box.

Help calculate the minimum cost to make the boxes equivalent.

### Input Format

The first line contains an integer $N$, the number of goodies in each box.

The next line contains $N$ space-separated integers, value of goodies in box1.

The next line contains $N$ space-separated integers, value of goodies in box2.

### Constraints

$1 \le N \le 10^5$

$1 \le box1_i, box2_i \le 10^9,$ for $1 \le i \le N$

### Output Format

Print the minimum cost to make the boxes equivalent. If it is not possible to make both boxes equivalent, print -1.

### Sample Input

```
4
4 2 2 2
1 4 1 2
```

### Sample Output

```
1
```

### Explanation

Swap index 1 of box1 with index 0 of box2, which has cost 1. Now box1 = `[4,1,2,2]` and box2 = `[2,4,1,2]`. Rearranging both the boxes makes them equal.

### Sample Input
```
4
2 3 4 1
3 2 5 1
```

### Sample Output
```
-1
```