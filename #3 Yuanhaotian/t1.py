from collections import deque

def can_reach(S, start, target):
    # BFS
    queue = deque([start])
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        
        for neighbor in S:
            if neighbor not in visited and can_transform(current, neighbor):
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

def can_transform(x, y):
    # 转换为三进制列表表示
    x_ternary = to_ternary_list(x)
    y_ternary = to_ternary_list(y)
    
    # 保证长度相等，填充前导零
    max_len = max(len(x_ternary), len(y_ternary))
    x_ternary = [0] * (max_len - len(x_ternary)) + x_ternary
    y_ternary = [0] * (max_len - len(y_ternary)) + y_ternary
    
    # 检查条件
    count_greater = 0
    for i in range(len(x_ternary)):
        if x_ternary[i] > y_ternary[i]:
            count_greater += 1
        if count_greater > 1:
            return False
    return True

def to_ternary_list(num):
    # 数字->三进制列表
    if num == 0:
        return [0]
    result = []
    while num > 0:
        result.append(num % 3)
        num //= 3
    return result[::-1]

# if __name__ == "__main__":
import sys
input_file = open("number.in", "r")
original_stdin = sys.stdin
sys.stdin = input_file
output_file = open("number.out", "w")

T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    
    if can_reach(S, S[0], S[-1]):
        print("yes", file=output_file)
    else:
        print("no", file=output_file)
