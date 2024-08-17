def solve():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        
        # 初始化 dp 数组
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + a[i-2]
            if i > 2:
                dp[i] = min(dp[i], dp[i-2] + b[i-3])
            if i > 3:
                dp[i] = min(dp[i], dp[i-3] + c[i-4])
        
        # 计算 d(s, t) 的总和
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += dp[i] * (n - i + 1)
        
        print(total_sum, file=output_file)

import sys
input_file = open("dist.in", "r")
original_stdin = sys.stdin
sys.stdin = input_file
output_file = open("dist.out", "w")

solve()