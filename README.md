# PCS2-Homework
Student Project for my Principle of Computer Science II. 

QuickSort and MergeSort are two algorithms. 
The first one takes last element as pivot(which is an element that divides the list of numbers in two smaller list), places the pivot element at its correct position in sorted array, and places all smaller (than the pivot) to its left and all greater elements to its right, through the partition() process;
the other one divides input array(a list of numbers) in two halves, and since it's recursive calls itself for the two halves and then merges the two sorted halves, and the key process is the merge(arr), that assumes that the arrays are sorted and allows the merging of the two sorted sub-arrays into one (our final list).

                                                        - THE CODE -

The first step is to create a random list, importing 'random' composed by n elements (form 0 to n) with n=1000; 
after that we can apply our two algorithms to the random list.
Then, we must import 'Timeit' to measure the execution speed of both algorithms, and to import it, we must use the 'setup function' to make sure to run the algorithms in the correct way.
Thanks to a plot, it's easier to compare the two speeds obtained, so we can assume that the QuickSort algorithm is faster than the MergeSort one, because MergeSort uses extra space in the memory, but still it's a better algorithm if we are using large data structures.

