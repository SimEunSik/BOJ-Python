N = int(input())
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        b = b % 15746
    return b
print(fibonacci(N))