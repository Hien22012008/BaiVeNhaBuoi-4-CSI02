def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ví dụ sử dụng:
n = 3
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
