## Big Bang

<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Since the big bang, the universe has been expanding at an accelerating rate. There are many objects in the universe, some are small, and some are big. Sometimes these objects collide with each other, and when they collide, they create new objects. The new object's mass is the sum of the mass of objects that collided. The new object is created at the location of the smaller object. The smaller objects are destroyed in the process. The total momentum, i.e., product of mass and velocity, of the system is conserved in the process.

You are given the initial state of the universe, and you are asked to find the final state of the universe after all the possible collisions are over.

In this problem there are $N$ objects in the universe. The $i^{th}$ object has mass $M_i$ and velocity $V_i$. It is located at point $i$ in one-dimensional space, and it is moving in the direction of the positive x-axis with velocity $V_i$.

Please note that there could be multiple collisions at the same time but in different parts of the universe and more than two objects could collide at once to form a new object.

### Input Format

The first line contains an integer $N$, where $N$ is the number of objects in the universe.

The next line contains $N$ integers, where the $i^{th}$ integer is $M_i$, where $M_i$ is the mass of the $i^{th}$ object.

The next line contains $N$ integers, where the $i^{th}$ integer is $V_i$, where $V_i$ is the velocity of the $i^{th}$ object.

### Constraints

$1 \le N \le 10^5$

$1 \le M_i \le 10^6$

$1 \le V_i \le 10^6$

### Output Format

The first line contains an integer $K$, where $K$ is the number of objects in the final state of the universe.

The next $K$ lines contains two integers in each line, where the $i^{th}$ line contains integers $M_i$ and $P_i$, where $M_i$ is the mass of the object and $P_i$ is the momentum of the object in the final state of the universe. The momentum of an object is the product of its mass and velocity. The objects should be printed in the increasing order of mass and momentum.

### Sample Input

```
5
1 2 3 4 5
1 2 3 4 5
```

### Sample Output

```
5
1 1
2 4
3 9
4 16
5 25
```

### Explanation

In the testcase above there are $5$ objects in the universe and there is no collision. So, the number of objects in the final state of the universe is $5$ and the objects are printed in the increasing order of the mass and the momentum.

### Sample Input

```
5
1 2 3 4 5
5 4 3 2 1
```

### Sample Output

```
1
15 35
```

### Explanation

In the testcase above there are $5$ objects in the universe, and they eventually collide to form a single object with mass $15$ and momentum $35$
