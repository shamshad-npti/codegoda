## Trip Planner

<sup>Section: 5, Score: 76, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Agoda’s objective is to provide the best price to customers, but it is not always easy. There are many factors that affect the price. For example, the price of a hotel room depends on the number of rooms available, the number of people who want to book the room, etc.

For each hotel room, Agoda has a price for each day of the year. Agoda offers discounts for long stays. It also offers "Agoda Cash" on specific days in the year to make customers happy and encourage them to book more.

Mr. Agoji who always books hotels through Agoda, is planning his next long holiday. Specifically, he wants to go to Agodaland that has $N$ hotels for $D$ days. He knows the price of each hotel for each day. He also got a secret deal message from Agoda for a set of $P$ hotels that if he books a hotel room $Q$ for at least $X$ consecutive days, he gets $Y$% discount on the total price of the consecutive stay at the hotel. The total discount is rounded up to the smallest integer not smaller than the discount itself. To make things more interesting, when he logged in to Agoda app on his phone, he got a notification of all available Agoda Cash for a list of hotel rooms and days.

He cannot wait to book the hotel rooms. He knows that he can maximize Agoda Cash and minimize the cost of staying in Agodaland by optimally selecting which hotel room to book for each day. However, there is another challenge for him. He must travel from one hotel to other, but not all hotels are connected to each other

Specifically, there are $M$ bidirectional roads each connecting two hotels, $U$ and $V$, with a cost $C$ of traveling from one hotel to other. Mr. Agoji can travel from one hotel to another only if there is a sequence of roads connecting them. For this problem you can assume that traveling from one hotel to another is instantaneous.

Mr. Agoji has a superpower, on day one he can magically go to any one hotel. After that he can only travel from one hotel to another using the roads.

Mr. Agoji wants to know the maximum Agoda Cash he can get and the minimum cost of staying in Agodaland. Can you help him? It should be noted that you should maximize Agoda Cash first and then minimize the cost of staying in Agodaland.

_Warning: Please note that if you're using a slower programming language like Python, there's a possibility that the code might exceed the time limit and result in a timeout error on large input._

### Input Format

The first line contains three space separated integers number of hotels $N$, number of days $D$ and number of roads $M$.

The next $N$ lines contain $D$ space separated integers each. The $j^{th}$ integer in the ith line $Price_{ij}$ denotes the price of ith hotel on day $j$.

The next $M$ lines contain three space separated integers hotel $U$, hotel $V$ and cost of traveling $C$.

The next line contains an integer $P$. The next $P$ lines contain three space separated integers hotel $Q$, number of consecutive days $X$ and discount $Y$ (in percentage).

The next line contains an integer, the number of Agoda Cash $K$. The next $K$ lines contain three space separated integers hotel $R$, day $S$ and Agoda Cash $T$.



### Constraints

There are three types of testcases. Constraints on the number of hotels, $N$, and the number of days, $D$, are different for each type but constraints on other parameters are the same

**Small Input**

$1 \le N, D \le 8$

**Medium Input**

$9 \le N, D \le 20$

**Large Input**

$21 \le N, D \le 250$

Constraints on other parameters

$0 \le M \le 1000$

$0 \le P \le N$

$0 \le K \le N\times D$

$1 \le U, V, Q, R \le N$

$1 \le X, S \le D$

$1 \le Y \le 100$

$1 \le C, Price_{ij}, T \le 50000$

$U \ne V$

All $Q$ are distinct

All pair of $(R, S)$ are distinct

### Output Format

Two space separated integers, the maximum Agoda Cash, and the minimum cost of staying in Agodaland. 

### Sample Input

```
3 3 3
10 25 5
20 30 1
2 2 2
1 2 10
2 3 5
1 3 6
1
2 2 50
3
1 1 7
1 2 10
2 2 10
```

### Sample Output

```
17 35
```

### Explanation

There are several ways to maximize the amount of Agoda cash earned, but one optimal solution is to stay at hotel 1 for all three days, which would earn $17 in Agoda cash. However, the cost of this stay would be $40. After trying all possible combinations, it becomes clear that it's impossible to earn more than $17 in Agoda cash. 

However, it is possible to minimize the overall cost of the trip while still earning the maximum amount of Agoda cash. For example, the traveler could stay at hotel 1 on the first day, then travel to hotel 2 on the second day and stay there for the next two days. This would cost $10 for staying at hotel 1 on day 1, $10 for traveling from hotel 1 to hotel 2 on day 2, $31 for staying at hotel 2 on days 2 and 3, and a discount of $16 (50% of $31 rounded up for staying at hotel 2 for at least two consecutive days) for a total of $35. 

### Sample Input

```
2 5 1
25 25 50 50 50
100 120 60 60 60
1 2 20
1
2 2 20
6
1 2 30
1 3 40
2 1 20
2 2 30
2 3 40
2 4 10
```

### Sample Output

```
100 309
```
