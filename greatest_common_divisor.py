
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


if __name__ == '__main__':
    print(gcd(1525, 875))
