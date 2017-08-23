# coding: utf8


def adjustheap(arr, i, nlength):
	old = i
	j = old*2 + 1
	while(j<nlength):
		if (j+1<nlength and arr[j+1]>arr[j]):
			j+=1
		if (arr[j]>arr[old]):
			arr[j], arr[old] = arr[old], arr[j]
		else:
			break
		old = j
		j = old*2 + 1


def buildheap(arr, i, nlength):
	for i in range(nlength/2-1, -1, -1):
		adjustheap(arr, i, nlength)
		print("ing: %s" % arr)

def heapsort(arr, i, nlength):
	buildheap(arr, 0, nlength)
	print('build: %s' % arr)
	for i in range(nlength-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		adjustheap(arr, 0, i)

def main():
	arr = [11, 4, 6, 1, 2, 7, 8, 5, 10, 9, 3]
	arr = [2, 4, 1, 3, 8, 9, 10, 7, 6, 5]
	print('old: %s' % arr)
	heapsort(arr, 0, len(arr))
	print('now: %s' % arr)

if __name__ == "__main__":
	main()