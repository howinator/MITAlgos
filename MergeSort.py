import random

def merge(L, R):
    i = 0
    j = 0
    answer = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i < len(L):
        answer.extend(L[i:])
    if j < len(R):
        answer.extend(R[j:])
    return answer


def mergeSort(A):
    n = len(A)
    if n == 1:
        return A
    mid =len(A) // 2
    L = mergeSort(A[:mid])
    R = mergeSort(A[mid:])
    return merge(L, R)

