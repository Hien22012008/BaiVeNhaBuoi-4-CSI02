def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

def simplify_fraction(a, b):
    common_divisor = gcd(a, b)
    return a // common_divisor, b // common_divisor

a, b = 20, 4
a, b = simplify_fraction(a, b)
print(f"Phân số sau khi rút gọn: a = {a}, b = {b}")