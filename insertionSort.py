import numpy as np

def insertionSort(alist):
  for j in range(1,len(alist)):
    key = alist[j]
    i = j-1
    while i+1 > 0 and alist[i] > key:
      alist[i + 1] = alist[i]
      i = i - 1
    alist[i + 1] = key

alist = [10,5,8,2,4,9]
insertionSort(alist)
print (alist)
