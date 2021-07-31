def countingSortForRadix(A, exp1):
    n = len(A)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (A[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (A[i] / exp1)
        output[count[int(index % 10)] - 1] = A[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]

def radixSort(A):
    max1 = max(A)
    exp = 1
    while max1 / exp > 0:
        countingSortForRadix(A, exp)
        exp *= 10
