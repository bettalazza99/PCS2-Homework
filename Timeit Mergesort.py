setup="""
import random
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()

def MeasureThis(size):
    mylist=[]
    for i in range(size):
        mylist.append(random.randint(0,size))
"""
import timeit
t=timeit.Timer('MeasureThis(1000)', setup=setup)
print (t.timeit(5))

