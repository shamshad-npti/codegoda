[Home](../README.md) | [Solution](./solution.py)

## AG Lite Text Editor
<sup>Section: 1, Score: 12, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Mr. Agoji is developing the next generation of AGLTE – AGoda Lite Text Editor. AGLTE supports many operations. `CUT`, `COPY`, `PASTE` are the three most common operations. 

A string in the editor is represented as one-indexed array of characters, as shown below
```
index: [1,2,3,4,5,6,7]

data:  [H,E,L,L,O,A,G]
```
If you COPY string “HE” and then find command `PASTE` 1 which means `PASTE` string “HE” beginning of the string or if command is `PASTE` 8 which means paste “HE” at the end of the string. CUT copies data to the clipboard and also deletes it from the original string.


Currently, AGLTE does not support multiple `CUT`/`COPY` commands, which means that if the `COPY` command is executed multiple times, it only remembers the latest command. However, in our next-generation AGLTE, we aim to support multiple CUT and `COPY` operations. This will enable users to execute `COPY` X times, CUT Y times, and then PASTE X+Y times. 

Here are the command formats for each operation: 

`COPY startPostion endPosition` - copies all data from startPostion to endPostion to the clipboard. 

`CUT startPostion endPosition` - copies all data from startPostion to endPostion to the clipboard and deletes it from the string. 

`PASTE index` – takes the latest data from the clipboard and puts it into the string at index. 

When executing these commands, please keep the following rules in mind:

1. You start with a string and an empty clipboard.
2. The first operation is either `COPY` or `CUT`, while subsequent operations can be any of the three.
3. `COPY/CUT/PASTE` operations are instant; this means the state of the clipboard and/or string will be updated each time you execute one of the three commands
4. Each `PASTE` will remove string from clipboard from the previous `COPY/CUT` operation, except when there is only one string on the clipboard


### Input Format
The first line will be a string, S, which is your text document 

Next line will be an integer C, where C represents the number of operations. 

Next C lines will contain one operation each 

Input always contains valid sequence of operations 


### Constraints
$1 \le \left|S\right| \le 100$

$1 \le C \le 16 $

*S contains alphanumeric characters and spaces*


### Output Format
Output the final text document in a single line after executing all commands.

### Sample Input
```
Agoda Flight
7
COPY 4 4
COPY 4 6
COPY 2 4
PASTE 1
CUT 1 3
PASTE 8
PASTE 2
```
### Sample Output
```
Ada goda Fgodlight
```
### Sample Input
```
AG LITE
4
COPY 2 4
PASTE 1
CUT 1 3
PASTE 8
```
### Sample Output
```
AG LITEG L
```
### Explanation
Here's an explanation of the commands and resulting string manipulations:

`COPY 2 4`: This command copies the characters "G L" from positions 2 to 4 in the original string, which is "AG LITE".

`PASTE 1`: This command pastes the copied characters "G L" at position 1 in the original string, resulting in the new string " G LAG LITE".

`CUT 1 3`: This command cuts the characters "G L" from positions 1 to 3 in the new string, resulting in the new string "AG LITE".

`PASTE 8`: This command pastes the characters from the clipboard (which is currently "G L") at position 8 in the new string, resulting in the final string "AG LITEG L".