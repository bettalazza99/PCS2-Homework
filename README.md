# PCS2-Homework
Student Project for my Principle of Computer Science II. 

QuickSort and MergeSort are two algorithms. 
The first one picks an element as pivot, which is an element that divides the list of numbers in two smaller list, and partitions the given array around the picked pivot, indeed the key step in this algorithm is the partition();
the other one divides input array in two halves, calls itself for the two halves and then merges the two sorted halves, and the key process is the merge(arr), that assumes that the arrays are sorted and allows the merging of the two sorted sub-arrays into one.

With 'Timeit' i measured the execution speed of both algoritms with a stochastic list, composed by n elements (form 0 to n) with n=1000. Comparing the two speeds obtained, we can assume that the QuickSort algorithm is faster than the MergeSort one, because MergeSort uses extra space in the memory, but still it's a better algorithm if we are using large data structures.

