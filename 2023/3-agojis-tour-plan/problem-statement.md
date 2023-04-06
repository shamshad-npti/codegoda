## Agoji's Tour Plan

<sup>Section: 3, Score: 33, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

It has been a long time since Agoji had a tour. So, he plans to visit Agodaland on his next summer vacation which has many tourist attractions and is known for tropical beaches, opulent royal palaces, ancient ruins, and ornate temples.

There are $n$ cities in Agodaland numbered from $1$ to $n$ and connected by some two-way roads in such a way that there exists exactly one path between any two cities.

Each city has an attractiveness rating — a letter from 'A' to 'Z' with 'Z' being the most attractive and 'A' being the least attractive.

A tour between two distinct cities, $u$ and $v$, is defined as a path from $u$ to $v$ without visiting any city twice.

During the tour Agoji must collect the rating of each city and arrange them in arbitrary order to form a string, which he defines as the attractiveness of the tour.

What is the most lexicographically attractive string he can attain by selecting the start and end city of the tour?

String $S$ is lexicographically larger than String $T$ when any of the following conditions satisfies.

1. $\left|S\right| \gt \left|T\right|$ and $T$ is prefix of $S$.
2. $\left|S\right| \le \left|T\right|$ and there exists an index $i$ ($0 \le i \lt \left|S\right|$) such that $S_i \gt T_i$ (compared according to their ASCII codes).

For example, "poster" is lexicographically larger than "post" and "ranger" is lexicographically larger than "racecar".

### Input Format

The first line contains a single integer $n$ — the number of cities in Agodaland.

The second line contains a string s of length $n$ consisting of uppercase Latin letters 'A' to 'Z'. The ith letter of the string denotes the attractiveness rating of the ith city.

The following $n - 1$ lines describe the roads. Each of these lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) — indices of cities connecting by the road.

### Constraints

$2 \le n \le 10^5$

$1 \le u, v \le n, u \ne v$

### Output Format

Print a string t — lexicographically largest attractiveness among all tour paths.

### Sample Input

```
5
BACAD
1 2
1 3
2 4
2 5
```

### Sample Output

```
DCBA
```

### Explanation

In the sample

Following are the attractiveness of each distinct tour path after being arranged in arbitrary order.

```
(1, 2) -> BA 

(1, 3) -> CB 

(1, 4) -> BAA 

(1, 5) -> DAB 

(2, 3) -> ABC 

(2, 4) -> AA 

(2, 5) -> DA 

(3, 4) -> CBAA 

(3, 5) -> DCBA 

(4, 5) -> ADA
```

Out of all the tours, the tour between cities 3 and 5, i.e., DCBA, is the most lexicographically attractive.

### Sample Input

```
5
BZCZZ
1 2
1 3
2 4
2 5
```

### Sample Output

```
ZZZ
```
