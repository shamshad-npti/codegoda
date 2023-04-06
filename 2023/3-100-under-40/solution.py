"""
Approach: Strongly Connected Components, DFS, DP on DAG
Time Complexity: O(N + M + Q)
Space Complexity: O(N + M + Q)
"""


from sys import setrecursionlimit
setrecursionlimit(10**6)


def strongly_connected_components(graph):
    N = len(graph)
    rev_graph = [[] for _ in range(N)]
    for u in range(N):
        for v in graph[u]:
            rev_graph[v].append(u)

    stack, components = [], []

    def dfs(u, visited):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v, visited)
        stack.append(u)

    def dfs_rev(u, visited, component):
        visited[u] = True
        for v in rev_graph[u]:
            if not visited[v]:
                dfs_rev(v, visited, component)
        component.append(u)

    visited = [False] * N
    for u in range(N):
        if not visited[u]:
            dfs(u, visited)

    visited = [False] * N
    for u in stack[::-1]:
        if not visited[u]:
            component = []
            dfs_rev(u, visited, component)
            components.append(component)
    return components


def maximum_reachable_node(graph):
    scc = strongly_connected_components(graph)
    N = len(graph)
    comp_mappping = [0] * N
    for i, comp in enumerate(scc):
        for u in comp:
            comp_mappping[u] = i

    induced_graph = [[] for _ in range(len(scc))]
    for u in range(N):
        for v in graph[u]:
            if comp_mappping[u] != comp_mappping[v]:
                induced_graph[comp_mappping[u]].append(comp_mappping[v])

    for i in range(len(scc)):
        induced_graph[i] = list(set(induced_graph[i]))

    visited = [False] * len(scc)
    best_path_size = [0] * len(scc)

    def dfs(u):
        visited[u] = True
        best = 0
        for v in induced_graph[u]:
            if not visited[v]:
                best = max(best, dfs(v))
            else:
                best = max(best, best_path_size[v])
        best_path_size[u] = best+len(scc[u])
        return best_path_size[u]

    for u in range(len(scc)):
        if not visited[u]:
            dfs(u)

    result = [0] * N
    for u in range(N):
        result[u] = best_path_size[comp_mappping[u]]
    return result


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
    best_path_size = maximum_reachable_node(graph)
    Q = int(input())
    result = []
    for _ in range(Q):
        C = int(input())-1
        result.append(str(best_path_size[C]))
    return result


if __name__ == '__main__':
    print(*main(), sep='\n')
