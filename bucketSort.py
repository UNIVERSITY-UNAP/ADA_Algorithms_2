def insertionSort(A):
	for i in range(1, len(A)):
		aux = A[i]
		j = i - 1
		while j >= 0 and A[j] > aux:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = aux    
	return A    

def bucketSort(x):
	A = []
	espacios = 10
	for i in range(espacios):
		A.append([])
	for j in x:
		A[int(espacios * j)].append(j)
	for i in range(espacios):
		A[i] = insertionSort(A[i])
	k = 0
	for i in range(espacios):
		for j in range(len(A[i])):
			x[k] = A[i][j]
			k += 1
	return x
