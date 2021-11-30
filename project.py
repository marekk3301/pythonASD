import time
from random import randint


def random_list_generator(length, max):
    randomList = []
    for i in range(length):
        number = randint(0, max)
        randomList.append(number)
    return randomList


def sorted_list_generator(length, max):
    sortedList = []
    for i in range(1, length):
        sortedList.append(i)
    return sortedList


def reversed_list_generator(length, max):
    reversedList = []
    for i in range(length, 1, -1):
        reversedList.append(i)
    return reversedList


randomList = random_list_generator(1000_000, 9999999)
sortedList = sorted_list_generator(1000_000, 9999999)
reversedList = reversed_list_generator(1000_000, 9999999)
maxValue = max(randomList)
length = len(randomList)


def bubbleSort(randomList, length):
    n = length
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if randomList[j] > randomList[j + 1]:
                randomList[j], randomList[j + 1] = randomList[j + 1], randomList[j]


def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def countingPositionSort(inputArray, maxValue):
    output = []
    for i in range(len(inputArray)):
        output.append(0)
    for position in range(1, len(str(maxValue)) + 1):
        A = []
        B = []
        temp = []
        for number in inputArray:
            try:
                A.append(int(str(number)[-position]))
            except IndexError:
                A.append(0)
        k = max(A)
        for i in range(len(inputArray)):
            B.append(0)
        for i in range(k + 1):
            temp.append(0)
        for j in range(0, len(A)):
            temp[A[j]] += 1
        for i in range(1, k + 1):
            temp[i] += temp[i - 1]
        for j in range(len(A) - 1, -1, -1):
            output[temp[A[j]] - 1] = inputArray[j]
            B[temp[A[j]] - 1] = A[j]
            temp[A[j]] -= 1
        for i in range(len(output)):
            inputArray[i] = output[i]

    return output


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def showResults(list):
    start_ = time.time()

    # bubblesort
    start = time.time()
    list = randomList.copy()
    bubbleSort(list, length)
    end = time.time()
    print("Bubblesort: " + str(end - start) + " seconds.")

    # insertion sort
    start = time.time()
    list = randomList.copy()
    insertionSort(list)
    end = time.time()
    print("Insertion sort: " + str(end - start) + " seconds.")

    # counting posintion sort
    start = time.time()
    list = randomList.copy()
    countingPositionSort(list, maxValue)
    end = time.time()
    print("Counting position sort: " + str(end - start) + " seconds.")

    # quicksort
    start = time.time()
    list = randomList.copy()
    quicksort(list, 0, length - 1)
    end = time.time()
    print("Quicksort: " + str(end - start) + " seconds.")

    print("Total: " + str(end - start_) + " seconds.")


print("Random array:")
showResults(randomList)

print("Sorted array:")
showResults(sortedList)

print("Reverse-sorted array:")
showResults(reversedList)
