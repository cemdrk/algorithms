
def linear_search(l, v):
    index = None

    for i in range(len(l)):
        if l[i] == v:
            index = i
            break

    return index


if __name__ == '__main__':
    print(linear_search([4, 5, 2, 1, 0, 3, 8], 3))
