"""
Integer Multiplication
The Karatsuba algorithm
x = a*10**n + b
y = c*10**n + d
then, x*y = ac*10**(2*n) + (ad+bc)*10**n + bd
"""
def karatsuba(x, y):
    # base case
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y))) // 2
        a, b = x // 10**n, x % 10**n
        c, d = y // 10**n, y % 10**n
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd
        prod = ac * 10**(2*n) + ad_plus_bc * 10**n + bd
        return prod

if __name__ == "__main__":
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    ans = karatsuba(a, b)
    print(ans)