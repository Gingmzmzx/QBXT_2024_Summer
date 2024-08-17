def max_triangle_area_squared(lengths):
    lengths.sort()  # 排序木棒长度
    max_area_squared = -1
    
    # 遍历所有三根木棒的组合
    for i in range(len(lengths) - 2):
        a, b, c = lengths[i], lengths[i+1], lengths[i+2]
        if a + b > c:
            # 计算面积的平方
            s = (a + b + c) / 2
            area_squared = s * (s - a) * (s - b) * (s - c)
            max_area_squared = max(max_area_squared, area_squared)
    
    return int(max_area_squared) if max_area_squared != -1 else -1

if __name__ == "__main__":
    import sys
    input_file = open("triangle.in", "r")
    original_stdin = sys.stdin
    sys.stdin = input_file
    output_file = open("triangle.out", "w")
    
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        L = list(map(int, input().split()))
        lengths = list(map(int, L))
        
        print(max_triangle_area_squared(lengths), file=output_file)
