
def hanoi(n, x='A', y='B', z='C'):
    """
    A B C - 3 pegs
    n - # of disks
    """

    if n == 1:
        print '{} -> {}'.format(x, z)
    else:
        hanoi(n-1, x, z, y)
        hanoi(1, x, y, z)
        hanoi(n-1, y, x, z)


hanoi(4)
