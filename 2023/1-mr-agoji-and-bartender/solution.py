import sys
sys.setrecursionlimit(10 ** 6)

def dfs(u, graph, visited, nodes):
    visited[u] = True
    nodes.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, nodes)

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        queue1 = list(map(int, input().split()))
        queue2 = list(map(int, input().split()))
        graph = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        visited = [False]*N
        for u in range(N):
            if not visited[u]:
                nodes = []
                dfs(u, graph, visited, nodes)
                subgroup1 = [queue1[i] for i in nodes]
                subgroup2 = [queue2[i] for i in nodes]
                if sorted(subgroup1) != sorted(subgroup2):
                    print("NO")
                    break
        else:
            print("YES")


if __name__ == "__main__":
    main()