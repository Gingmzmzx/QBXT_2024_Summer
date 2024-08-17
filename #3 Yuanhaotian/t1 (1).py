def is_legal_move(x, y):
    cnt = 0
    while x > 0 or y > 0:
        X_j = x % 3
        Y_j = y % 3
        if X_j < Y_j:
            cnt += 1
        if cnt > 1:
            return False
        x //= 3
        y //= 3
    return True

def can_transform(S):
    current = S[0]
    for i in range(1, len(S)):
        next_value = S[i]
        if is_legal_move(current, next_value):
            current = next_value
    return current == S[-1]

def solve():
    T = int(input().strip())
    results = []
    for _ in range(T):
        N = int(input().strip())
        S = list(map(int, input().strip().split()))
        if can_transform(S):
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))

# Example usage:
solve()
