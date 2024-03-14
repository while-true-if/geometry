import math

def cie_euclidean(ax, ay, bx, by):
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

def euclidean(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def pythagorean(a, b, c):
    if a == 'x':
        return math.sqrt(c ** 2 - b ** 2)
    elif b == 'x':
        return math.sqrt(c ** 2 - a ** 2)
    else:
        return math.sqrt(a ** 2 + b ** 2)

def cie_heron(ax, ay, bx, by, cx, cy):
    x = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
    y = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
    z = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
    s = (x + y + z) / 2
    return math.sqrt(s * (s - x) * (s - y) * (s - z))

def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def cie_manhattan(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def manhattan(a, b):
    return a + b

def hamming(a, b):
    a = list(str(a))
    b = list(str(b))
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c

def permutation(a, b):
    c = 1
    for i in range(a - b + 1, a + 1):
        c *= i
    return c

def combination(a, b):
    return permutation(a, b) // math.factorial(b)

def accumulate(x):
    y = [0] * len(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = y[i-1] + x[i]
    return y

def reduce(a,b):
    c=math.gcd(a,b)
    a=a//c
    b=b//c
    return a,b

__all__ = [
    "cie_euclidean",
    "euclidean",
    "pythagorean",
    "cie_heron",
    "heron",
    "cie_manhattan",
    "manhattan",
    "hamming",
    "permutation",
    "combination",
    "accumulate",
    "reduce"
]
