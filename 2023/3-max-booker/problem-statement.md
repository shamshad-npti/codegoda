## Max Booker

<sup>Section: 3, Score: 33, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Agoda is an online travel booking platform that offers hotel and accommodation reservation services worldwide. If someone books accommodation, we call them a booker. Sometimes the booker wants to cancel a booking. For simplicity of the problem, per cancellation attempt, a booker can only cancel their last booking. If there is no last booking, the operation has no impact. If they want to cancel two previous bookings, they need to send two cancel commands to the system. Sometimes we want to know who is booking the maximum number of accommodations. In this problem, your job is to help us find the bookers who have more than a certain number of bookings.

### Input Format

The first line of the input contains an integer $N$, which represents the number of operations. Each of the next $N$ lines consists of a command of one of the following three types:

1. `B booker_id`: meaning that the booker_id has booked accommodation.
2. `C booker_id`: meaning that the booker_id has canceled one previous booking.
3. `P K`: print how many bookers have at least K bookings and sum of all bookings from them.

### Constraints

$1 \le N \le 3\times10^5$

$1 \le booker\text{_}id \le 10^7$

$1 \le K \le 10^7$

### Output Format

For every input of type 3(print command) print two integers separated by a single space. The first integer should indicate how many bookers have at least $K$ bookings and the second integer should indicate sum of all bookings from them.

### Sample Input

```
11
B 1
B 3
B 6
P 1
B 6
P 1
B 6
P 2
C 6
C 6
P 2
```

### Sample Output

```
3 3
3 4
1 3
0 0
```

### Explanation

1. For the first print(P) command, we have 3 bookers (1, 3, 6). Each of them booked only one accommodation. So, the output is 3 3.
2. For the second print(P) command, the booker with id 6 has booked 2 accommodations and others have one booking each. Therefore, they all have at least one booking and the total sum of their bookings is 4. So, the output is 3 4.
3. For the third print(P) command, we can see that only booker id 6 has at least two bookings. And he has 3 bookings. Thus, the output is 1 3.
4. For the last print(P) command, we see no booker has at least 2 bookings. Therefore, the output is 0 0.

### Sample Input

```
17
B 4
P 1
C 5
C 5
B 5
B 5
C 3
C 4
B 5
P 3
B 4
P 1
B 6
B 4
C 4
B 4
P 3
```

### Sample Output

```
1 1
1 3
2 4
1 3
```
