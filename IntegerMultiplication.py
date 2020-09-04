"""
Integer Multiplication
The grade-school algorithm
"""
def gradeSchool(x, y, base=10):
    x = [int(n) for n in str(x)]
    y = [int(n) for n in str(y)]
    product = [0] * (len(x) + len(y))
    for j in range(len(y)-1, -1, -1):
        carry = 0
        for i in range(len(x)-1, -1, -1):
            product[i+j+1] += carry + x[i] * y[j]
            carry = product[i+j+1] // base
            product[i+j+1] %= base
        product[j] = carry
    print(product)
    product = [str(n) for n in product]
    product = ''.join(product).lstrip('0')
    print(product)
    return product

if __name__ == "__main__":
    gradeSchool(1234, 567)