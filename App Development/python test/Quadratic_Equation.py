import math

def find_roots(a, b, c):
    result1 = float((-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a))
    result2 = float((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a))
    return (result1, result2)

print(find_roots(2, 10, 8));