"""
Approach: DFS
A = |alphabet size| = 26
Time Complexity: O(A*N)
Space Complexity: O(A*N)
"""


import string


def chr_to_inx(c):
    return 25 - (ord(c) - ord('A'))


def dfs(tree, S):
    stack = [0]
    node_status = [0] * len(tree)
    node_status[0] = 1
    while stack:
        u = stack[-1]
        visit = [v for v in tree[u] if node_status[v] == 0]
        if visit:
            for v in visit:
                stack.append(v)
                node_status[v] = 1
        else:
            max1, max2, max3 = [[0] * 26 for _ in range(3)]
            for v in tree[u]:
                if node_status[v] == 1:
                    continue
                current, subtree = node_status[v]
                max3 = max(subtree, max3)
                if current > max1:
                    max2 = max1
                    max1 = current
                elif current > max2:
                    max2 = current
            max1[chr_to_inx(S[u])] += 1
            merged = [max1[i] + max2[i] for i in range(26)]
            node_status[u] = max1, max(merged, max3)
            stack.pop()
    return node_status[0]


def main():
    n = int(input())
    S = input()
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    _, ans = dfs(tree, S)
    return ''.join(c*a for c, a in zip(string.ascii_uppercase[::-1], ans))


if __name__ == '__main__':
    print(main())
