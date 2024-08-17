from collections import defaultdict, deque

def get_size_combinations(nodes, p):
    sizes = [nodes[p[0]-1], nodes[p[1]-1], nodes[p[2]-1]]
    return sizes

def bfs(graph, start):
    n = len(graph)
    distance = [-1] * n
    queue = deque([start])
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance

def count_valid_apples(n, p, edges):
    # 建立树的邻接表表示法
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # 枚举每一个节点对并求出其最远的节点对
    unique_combinations = set()
    
    for node in range(n):
        distance = bfs(graph, node)
        for u in range(n):
            for v in range(u + 1, n):
                if distance[u] != -1 and distance[v] != -1 and distance[u] + distance[v] == distance[v] + distance[u] - 2 * distance[node]:
                    sizes = sorted([u+1, v+1, node+1])
                    for perm in [(p[0]-1, p[1]-1, p[2]-1)]:
                        if get_size_combinations(sizes, perm) == sizes:
                            unique_combinations.add(tuple(sizes))
    
    return len(unique_combinations)

# 读入数据
n = int(input())
p = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# 计算并输出结果
print(count_valid_apples(n, p, edges))
