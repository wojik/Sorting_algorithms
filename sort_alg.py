import sys
import time
from random import randint
sys.setrecursionlimit(100000)
ciag = input('Wpisz rodzaj ciągu: \n -L - losowy, \n -A - A-kształtny, \n -V - V-kształtny, \n -R - rosnący, \n -M - malejący \n')
typ = input('Wpisz rodzaj algorytmu sortowania: \n -MS - Merge Sort, \n -HS - Heap Sort, \n -BS - Bubble Sort, \n -SS - Selection Sort, \n -IS - Insertion Sort, \n -QS - Quick Sort, \n -ALL\n')
#typ = 'bs'
#ciag = 'l'
nl = [100, 500, 1000, 3000, 5000, 7000, 9000, 12000, 15000, 18000]
A = []
for n in nl:
    A = []
    if ciag == 'L' or ciag == 'l':
        A = []
        for i in range(n):
            A.append(randint(1, n))
        d=len(A)
        B = A.copy()
    if ciag == 'A' or ciag == 'a':
        A = []
        for i in range(1, (n // 2) + 1):
            A.append(i)
        for i in range((n // 2)+1, 0, -1):
            A.append(i)
        d = len(A)
        B = A.copy()
    if ciag == 'V' or ciag == 'v':
        A = []
        for i in range((n // 2), 0, -1):
            A.append(i)
        for i in range(1, (n // 2)+1):
            A.append(i)
        d = len(A)
        B = A.copy()
    if ciag == 'R' or ciag == 'r':
        A = []
        for i in range(1, n+1):
            A.append(i)
        d = len(A)
        B = A.copy()
    if ciag == 'M' or ciag == 'm':
        A = []
        for i in range(n, 0, -1):
            A.append(i)
        d = len(A)
        B = A.copy()
    def quicksort(array):
        if len(array) < 2:
            return array
        low, same, high = [], [], []
        pivot = array[(len(array) - 1)]
        for item in array:
            if item > pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item < pivot:
                high.append(item)
        return quicksort(low) + same + quicksort(high)

    def mergeSort(myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]
            mergeSort(left)
            mergeSort(right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    myList[k] = left[i]
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1

    def heapify(array, a, b):
        largest = b
        l = 2 * b + 1
        root = 2 * b + 2
        if l < a and array[b] > array[l]:
            largest = l
        if root < a and array[largest] > array[root]:
            largest = root
        if largest != b:
            array[b], array[largest] = array[largest], array[b]
            heapify(array, a, largest)

    def Heap_Sort(array):
        a = len(array)
        for b in range(a // 2 - 1, -1, -1):
            heapify(array, a, b)
        for b in range(a - 1, 0, -1):
            array[b], array[0] = array[0], array[b]  # swap
            heapify(array, b, 0)

    if typ == 'MS' or typ == 'ms' or typ == 'ALL' or typ == 'all':
        print('MERGE SORT dla ',n,' elementów')
        t0 = time.time()
        mergeSort(A)
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ')
        dif = t1-t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()

    if typ == 'HS' or typ == 'hs' or typ == 'ALL' or typ == 'all':
        print('HEAP SORT dla ',n,' elementów')
        t0 = time.time()
        Heap_Sort(A)
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ')
        dif = t1 - t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()

    if typ == 'BS' or typ == 'bs' or typ == 'ALL' or typ == 'all':
        print('BUBBLE SORT dla ',n,' elementów')
        t0 = time.time()
        for j in range(1, d):
            for i in range(0, d - j):
                if A[i] < A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ')
        dif = t1 - t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()

    if typ == 'SS' or typ == 'ss' or typ == 'ALL' or typ == 'all':
        print('SELECTION SORT dla ',n,' elementów')
        t0 = time.time()
        for j in range(0, d - 1):
            max = j
            for i in range(j + 1, d):
                if A[i] > A[max]:
                    max = i
            A[max], A[j] = A[j], A[max]
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ')
        dif = t1 - t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()

    if typ == 'IS' or typ == 'is' or typ == 'ALL' or typ == 'all':
        print('INSERTION SORT dla ',n,' elementów')
        porow = 0
        t0 = time.time()
        for j in range(1, d):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] < key:
                porow += 1
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ', porow)
        dif = t1 - t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()

    if typ == 'QS' or typ == 'qs' or typ == 'ALL' or typ == 'all':
        print('QUICK SORT dla ',n,' elementów')
        t0 = time.time()
        A = quicksort(A)
        t1 = time.time()
        print('lista początkowa: ', B, '\nlista posortowana: ', A, '\nliczba porównań: ')
        dif = t1 - t0
        print('Czas sortowania: ', dif)
        print('\n\n')
        A = B.copy()
