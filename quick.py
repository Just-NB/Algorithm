import random

def quicksort(A, left, right) :
    if left >= right :
        return A
    pivot = random.randrange(left, right)

    A[pivot], A[left] = A[left], A[pivot]
    low = left
    high = left+1

    while high < right:
        if A[left] < A[high] :
            high += 1
        elif A[left] >= A[high] :
            low += 1
            A[low], A[high] = A[high], A[low]
            high += 1

    A[low], A[left] = A[left], A[low]
    quicksort(A, left, low)
    quicksort(A, low+1, right)
    return A






if __name__ == '__main__':

    # A = [3, 8, 5, 4, 9, 1, 6, 2, 7]
    A = [random.randint(1, 100) for i in range(20)]
    print(A)
    sortedA = quicksort(A, 0, len(A))
    print(sortedA)
