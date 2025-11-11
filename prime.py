import math

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to print twin primes
def print_twin_primes(limit):
    print("Twin primes less than", limit, "are:")
    for i in range(2, limit):
        if is_prime(i) and is_prime(i + 2):
            print("(", i, ",", i + 2, ")")

# Functions for permutations and combinations
def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return permutation(n, r) // math.factorial(r)

# Main program
print_twin_primes(1000)

# Taking input for permutation & combination
n = int(input("\nEnter n: "))
r = int(input("Enter r: "))

if n >= r:
    print(f"P({n},{r}) = {permutation(n, r)}")
    print(f"C({n},{r}) = {combination(n, r)}")
else:
    print("Invalid input! n must be >= r")
