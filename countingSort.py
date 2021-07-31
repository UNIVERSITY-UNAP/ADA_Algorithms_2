def countingSort(A):
	k = int(max(A))
	B = [None for i in range(len(A))]
	C = [0 for i in range(k+1)]
	for i in range(len(A)):
		C[A[i]] += 1
	for i in range(1,k+1):
		C[i] += C[i-1]
	for i in range(len(A)-1,-1,-1):
		B[C[A[i]] - 1] = A[i]
		C[A[i]] -= 1
	return B
