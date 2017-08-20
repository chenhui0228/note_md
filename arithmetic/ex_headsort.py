# coding: utf8


def adjustheap(arr=None, i=0, nlength=0):
    j = i*2 + 1
    temp = arr[i]
    while(j < nlength):
        if(j+1<nlength and arr[j+1]>arr[j]):
            j += 1
        if(arr[j] > temp):
            break
        arr[i] = arr[j]
        i = j
        j = i*2 + 1
    arr[i] = temp

def heapsort(arr=None, root=0, nlength=0):
    for i in range(nlength/2-1, 0, -1):
        adjustheap(arr, i, nlength)
    for i in range(nlength-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjustheap(arr, 0, i-1)

def main():
    arr = [2, 4, 1, 3, 8, 9, 10, 7, 6, 5]
    print('old: %s' % arr)
    heapsort(arr, 0, len(arr))
    print('now: %s' % arr)


if __name__ == '__main__':
    main()
