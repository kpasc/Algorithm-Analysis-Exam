import math
import matplotlib.pyplot as plt

# Function simply computes choose j given n
def choose(n,j):
    return math.factorial(n) / (math.factorial(j) * math.factorial(n - j))

# function for probablility of getting j 1's from n (given in lecture slides
def p(n,j):
    n = float(n)
    frac = 1 / n
    one_minus_frac = 1 - frac
    first = choose(n,j)
    second = math.pow(frac,j)
    third = math.pow(one_minus_frac,n-j)

    return first * second * third

# recursive function given from the L(n) recurrence in the lecture slides
def l(n,sum):
    denom = 1 - p(n,0) - p(n,n)

    # recursion first
    for j in range(2,n):
        sum += l(j,sum)*p(n,j)

    return (1 + sum) / denom

# we need to call l(n) 17 times for 3 - 20. Record each value in an array to plot later
n = []
l_n = []
for i in range(3,20):

    val = l(i,0.0)

    n.append(i)
    l_n.append(val)

# plot l(n) values vs n (n = 3:20)
plt.plot(n,l_n)
plt.title("L(n) vs. n for 3:20")
plt.xlabel("n")
plt.ylabel("L(n)")
plt.show()