import math

# simply choose j from n
def choose(n,j):
    return math.factorial(n) / (math.factorial(j) * math.factorial(n - j))

print choose(9,4)
