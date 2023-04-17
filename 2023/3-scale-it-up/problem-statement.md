[Home](../README.md) | [Solution](./solution.py)

## Scale It Up

<sup>Section: 3, Score: 33, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Krit is a capacity planner at Agoda who frequently faces the following questions: What is the minimum time required to achieve a particular capacity for a given set of servers and an application? To answer this question, Krit must consider the fact that servers are interconnected through a bidirectional network, with each connection between two servers having a latency that is consistent in both directions.

Moreover, Krit must consider the warmup time required for each server. The warmup time is the period required for the application to launch on a server, and the server begins serving requests at maximum capacity only after the warmup period has ended.

The network contains $N$ servers, labeled with integers from $1$ to $N$. The application is initially on the server labeled $1$ and is distributed to all other servers in the network as soon as possible. When the application arrives at a server, it immediately starts booting up, and the server reaches its maximum capacity only after the warmup time has elapsed.

Given the network topology, the warmup time for each server, and the capacity of each server, Krit requires a program that utilizes this information to determine the minimum time required to reach a specific capacity for a given set of servers and an application.

### Input Format

The first line contains two space-separated integers $N$ and $M$, where $N$ is the number of servers and $M$ is the number of connections.

The next $M$ lines contains three space-separated integers $A$, $B$ and $L$, where $A$ and $B$ are the servers connected by a connection with latency $L$ milliseconds.

The next line contains $N$ space-separated integers, where the $i^{th}$ integer is the warmup time $W$ milliseconds of the $i^{th}$ server.

The next line contains $N$ space-separated integers, where the $i^{th}$ integer is the capacity or throughput $T$ request/milliseconds of the $i^{th}$ server.

The next line contains an integer $Q$, where $Q$ is the number of queries.

The next $Q$ lines contains an integer $C$, where $C$ is the capacity Krit is interested in.

### Constraints

$1 \le N \le 10^5$

$1 \le M \le 2\times 10^5$

$1 \le A, B \le N$

$1 \le L \le 10^4$

$1 \le W \le 10^4$

$1 \le T \le 10^4$

$1 \le Q \le 10^5$

$1 \le C \le 2\times 10^9$

### Output Format

For each query print the minimum time (in milliseconds) required to reach at least capacity $C$. If it is not possible to reach at least capacity $C$, print `-1`.

### Sample Input

```
3 2
1 2 100
2 3 100
20 30 40
1000 1000 1000
3
700
1500
3300
```

### Sample Output

```
20
130
-1
```

### Explanation

The server labeled as 1 can start serving in just 20ms and has the capacity to handle up to 700 requests per millisecond. In the second test case, both server 1 and server 2 have equivalent capacity, but server 2 will require 130ms to reach its maximum capacity. This is due to the time taken to receive the application from server 1 (100ms) and warm up (30ms). Server 1, on the other hand, can begin serving immediately after 20ms.

When all three servers are combined, their maximum capacity is 3000 requests per millisecond. Therefore, it is impossible for them to achieve a throughput of 3300.

### Sample Input

```
5 7
1 2 9
1 4 5
1 5 7
2 3 8
2 5 3
3 4 10
4 5 8
1 2 8 5 7
9 2 5 6 4
7
17
10
1
3
19
25
4
```

### Sample Output

```
11
10
1
1
14
23
1
```
