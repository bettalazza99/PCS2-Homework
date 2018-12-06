import matplotlib.pyplot as plt
setup="""
import random
def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )


def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def MeasureThis(size):
    mylist=[]
    for i in range(size):
        mylist.append(random.randint(0,size))
"""
import timeit
TimeQuick=timeit.Timer('MeasureThis(1000)', setup=setup)
print (TimeQuick.timeit(5))


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
TimeMerge=timeit.Timer('MeasureThis(1000)', setup=setup)
print (TimeMerge.timeit(5))

tm=[TimeMerge.timeit(1)]
tq=[TimeQuick.timeit(1)]
tqc=[]
tmc=[]
tqc=tq[0]
tmc=tm[0]
def drawplot(TimeQuick, TimeMerge):
    plt.plot([0,tq[0]], [0.001,0.1], label= "QuickSort")
    plt.plot([0,tm[0]], [0.001,0.1], label="MergeSort")
    plt.xlabel("Seconds")
    plt.legend()
    plt.title("Time Comparison")
    plt.grid()
    plt.show()

drawplot(tqc, tmc)
