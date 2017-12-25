# coding: utf-8


def quick_sort(arr=None, left=0, right=0):
    if arr is None:
        arr = []
    if left >= right:
        return
    i = left
    j = right
    print('i: %s, j: %s' % (i, j))
    old = arr[i]
    while(i < j):
        while(i < j and arr[j] > old):
            j = j-1
        if(i < j):
            arr[i] = arr[j]
            i = i+1
        while(i < j and arr[i] < old):
            i = i+1
        if(i < j):
            arr[j] = arr[i]
            j = j-1

    print('iiiiiiiiiiii: %s' % i)
    arr[i] = old
    print('sorting: %s' % arr)
    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    # arr = [4, 3, 5, 9, 2, 7, 8, 1, 6]
    print('old: %s' % arr)
    quick_sort(arr, 0, len(arr)-1)
    print('new: %s' % arr)
