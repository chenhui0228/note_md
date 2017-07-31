#coding: utf8

def bubbl_sort(arr=None, arr_len=0):
    if arr is None:
        arr = []
    if arr_len == 0:
        arr_len = len(arr)
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def choice_sort(arr=None, arr_len=0):
    if arr is None:
        arr = []
    if arr_len == 0:
        arr_len = len(arr)
    for i in range(arr_len):
        k = i
        for j in range(i+1, arr_len):
            if arr[k] > arr[j]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

    return arr

def insert_sort(arr=None, arr_len=0):
    if arr is None:
        arr = []
    if arr_len == 0:
        arr_len = len(arr)
    for i in range(1, arr_len):
        old_num = arr[i]
        j = i-1
        while(j >=0 and arr[j] > old_num):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = old_num
    return arr


if __name__ == '__main__':
    arr = [1, 3, 2, 6, 4, 9]
    print(arr)
    arr = bubbl_sort(arr,3)
    print(arr)
    arr = [1, 4, 2, 9, 5, 7, 6]
    print(arr)
    arr = choice_sort(arr)
    print(arr)

    arr = [1, 4, 2, 9, 5, 7, 6]
    print(arr)
    arr = insert_sort(arr)
    print(arr)