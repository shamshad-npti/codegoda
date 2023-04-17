[Home](../README.md) | [Solution](./solution.py)

## Alice's Dream Trip
<sup>Section: 1, Score: 12, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Alice is a big spender who is planning her dream trip and has found great deals on Agoda. She is looking to book a series of hotel rooms, with each room having a nightly rate. However, she wants to maximize the amount of money spent on booking the rooms in such a way that no two adjacent rooms are booked.

Given a list of integers representing the nightly rate for each hotel room, we must return the maximum amount of money Alice can spend by booking from the given rooms with the restrictions mentioned above.  

### Input Format
The first line has N which is the number of rooms 

The next N lines contain the nightly rate of each room. 

### Constraints
$1 \le N \le 10^5$

$1 \le rate \le 500$

### Output Format
An integer representing the max amount spent

### Sample Input
```
5
80
70
90
100
60
```
### Sample Output
```
230
```
### Explanation
Alice can book the rooms with rates 80, 90, and 60 for a total of 230.
### Sample Input
```
5
10
3
7
1
6
```
### Sample Output
```
23
```