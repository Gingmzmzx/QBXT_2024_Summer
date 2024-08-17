def solve(n):
    trailing_zeros = count_trailing_zeros(n)
    last_digit = last_nonzero_digit(n)
    return trailing_zeros, last_digit

def count_trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

def last_nonzero_digit(n):
    p = 10
    result = 1
    for i in range(1, n+1):
        result = (result * i) % p
    return result

print(*solve(int(input())))