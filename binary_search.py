
def binary_search_recursive(arr, v, low, up):
    """ search ascending order """
    if low > up:
        return None

    mid = (low + up) // 2

    if v == arr[mid]:
        return mid
    elif v < arr[mid]:
        return binary_search_recursive(arr, v, low, (mid - 1))
    else:
        return binary_search_recursive(arr, v, (mid + 1), up)


def binary_search_iterative(arr, v):
    """ search ascending order """
    low = 0
    up = len(arr)-1
    index = None

    while low <= up:
        mid = (low + up) // 2

        if v == arr[mid]:
            index = mid
            break
        elif v < arr[mid]:
            up = (mid - 1)
        else:
            low = (mid + 1)

    return index


if __name__ == '__main__':

    A = [1, 2, 3, 4, 5]

    print(binary_search_iterative(A, 3))

    print(binary_search_recursive(A, 3, 0, len(A)-1))
