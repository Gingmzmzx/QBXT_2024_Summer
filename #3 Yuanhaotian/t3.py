from collections import defaultdict

paths = 0

def check(path, permutation):  # 手动离散化
    if permutation[0] < permutation[1]:
        if path[0] >= path[1]:
            return False
    
    if permutation[0] > permutation[1]:
        if path[0] <= path[1]:
            return False
        
    if permutation[0] < permutation[2]:
        if path[0] >= path[2]:
            return False
    
    if permutation[0] > permutation[2]:
        if path[0] <= path[2]:
            return False
        
    if permutation[1] < permutation[2]:
        if path[1] >= path[2]:
            return False
    
    if permutation[1] > permutation[2]:
        if path[1] <= path[2]:
            return False
    
    return True
    

def find_all_paths(n, edges, permutation):
    # 构建树的邻接表
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    prev = [-1] * (n + 1)

    # 查找所有可能的三节点路径
    def dfs(node, parent, depth):
        if depth == 3:
            path = [node]
            while parent != -1:
                path.append(parent)
                parent = prev[parent]
            if len(path) != 3:
                return
            print(path)
            if check(path, permutation):
                global paths
                paths += 1
            return
        
        for neighbor in adj[node]:
            if neighbor != parent:
                prev[neighbor] = node
                dfs(neighbor, node, depth + 1)
                prev[neighbor] = -1
    
    # 从每个节点开始 DFS
    for start in range(1, n + 1):
        dfs(start, -1, 1)
    
    return paths

# if __name__ == "__main__":
import sys
input_file = open("tree.in", "r")
original_stdin = sys.stdin
sys.stdin = input_file
output_file = open("tree.out", "w")

n = int(input())
p1, p2, p3 = list(map(int, input().split()))
edges = []
for _ in range(n-1):
    u, v = input().split()
    edges.append((int(u), int(v)))

print(find_all_paths(n, edges, [p1, p2, p3]), file=output_file)
