"""
Integer Multiplication
The Karatsuba algorithm
"""
def karatsuba(x, y):
    # base case
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        n2 = n // 2
        a, b = x // 10**n2, x % 10**n2
        c, d = y // 10**n2, y % 10**n2
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bd = karatsuba(a+b, c+d) - ac - bd
        prod = ac * 10**(2*n2) + ad_plus_bd * 10**n2 + bd
        print(prod)
        return prod

if __name__ == "__main__":
    karatsuba(1234, 567)