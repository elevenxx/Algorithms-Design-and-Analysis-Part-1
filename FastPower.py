"""
input: positive integers a and b
output: a^b
https://oi-wiki.org/math/quick-pow/
"""

def fastPower(a, b):
    if b == 1:
        return a
    else:
        c = a * a
        ans = fastPower(c, b//2)
    if b & 1:
        return a * ans
    else:
        return ans

if __name__ == "__main__":
    ans = fastPower(2, 10)
    print(ans)