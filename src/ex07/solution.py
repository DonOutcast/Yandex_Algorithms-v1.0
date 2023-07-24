import sys

sys.setrecursionlimit(1_00_000)

def dfs(now, neighbors, subtree_size):
    subtree_size[now] = 1
    for next in neighbors[now]:
        if subtree_size[next] == -1:
            subtree_size[now] += dfs(next, neighbors, subtree_size)
    return subtree_size[now]

n = int(input())

neighbors = []
for i in range(n + 1):
    neighbors.append([])

for i in range(n - 1):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

subtree_size = [-1] * (n + 1)
print(dfs(1, neighbors, subtree_size))
print(*subtree_size[1:])


