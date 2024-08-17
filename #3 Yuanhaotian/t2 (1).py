def func(L):
    # 对木棒长度进行排序
    L.sort(reverse=True)
    n = len(L)
    
    # 遍历最大的三条边，检查是否能组成三角形
    for i in range(n - 2):
        a, b, c = L[i], L[i + 1], L[i + 2]
        if a < b + c and b < a + c and c < a + b:
            # 计算面积平方
            s = (a + b + c) / 2
            area_square = s * (s - a) * (s - b) * (s - c)
            return int(area_square)  # 返回最大面积的平方
    
    # 如果找不到可行的三条边
    return -1

import sys
input_file = open("triangle.in", "r")
original_stdin = sys.stdin
sys.stdin = input_file
output_file = open("triangle.out", "w")

T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    print(func(L), file=output_file)
