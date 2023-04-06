## Agoji's Scrum
<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Mr. Agoji joins Agoda and works in the scrum team where tasks are managed within a backlog. The team operates with high ownership, allowing anyone to add or remove tasks freely. To ensure that the most valuable tasks are picked during sprint planning, we always prioritize and keep the tasks in the backlog sorted by the business value regularly.  

The team performs three operations: adding new tasks, deleting unnecessary tasks, and picking the $N$ most valuable tasks to do to gain business value. The total business gain from doing those tasks is equal to the sum of values of the individual tasks we pick. 

Additionally, if there are multiple tasks with the same value, we will pick based on lexicographical order of task id. In the case that we try to pick more tasks than what is available in the backlog, all tasks in the backlog will be selected. Also, if a non-existing task is mistakenly deleted, no effect will occur.  

You are the person can help us to see how well Mr. Agoji team’s performance. Please help Mr. Agoji to total business values his team made! 

### Input Format
The first line of the input will contain $Q$, the number of operations.  
The next $Q$ lines contain the operation symbol and parameters depending on the operation type. 

There are $3$ types of operations: 

1. Add a task to the backlog. <br/> 
   Input format: `+ T V`<br/>
   where $T$ represents the task ID, and $V$ represents the business value of the task. 

2. Delete the task from the backlog <br/>
   Input format: `- T`</br>
   $T$ represents the task ID 

3. Pick the N most valuable tasks <br/>
   Input format: `> N`<br/>
   $N$ represents the number of tasks going to be picked

### Constraints
$1 \le Q \le 10^5$

$1 \le \left|T\right| \le 10$ 

$T$ consists of printable, non-space ASCII characters

$1 \le V \le 10^6$

$1 \le N \le 10^5$

### Output Format
An integer, representing the total business value we get after picking all tasks selected by operation of type 3.

### Sample Input
```
6
+ AGD-101 10
+ AGD-102 100
+ AGD-103 50
+ AGD-104 10
- AGD-102
> 2
```
### Sample Output
```
60
```
### Explanation
We add the 4 tasks to the backlog, then we remove the ADG-102 task. So, when we pick 2 of the highest-value tasks, we get ADG-101 and ADG-103 tasks. So, the total gained value is 10+50 = 60. 

### Sample Input
```
5
+ AGD-101 10
> 1
+ AGD-102 100
+ AGD-103 50
> 1
```
### Sample Output
```
110
```
### Explanation
In the first pick, we pick the ADG-101 task with the value of 10. 
In the second pick, we pick the ADG-102 task with the value of 100. 
So, the total value is 110.  