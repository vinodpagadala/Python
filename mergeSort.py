import numpy as np
import sys

sys.setrecursionlimit(10000)

def Merge(l, r, A):
  nl = len(l)
  nr = len(r)
  i = j = k = 0
  
  while i< nl & j < nr:
    if l[i] < r[j]:
      A[k] = l[i]
      i = i + 1
    elif r[j] < l[i]:
      A[k] = r[j]
      j = j + 1
    k = k + 1
  
  while i < nl:
    A[k] = l[i]
    i = i + 1
    k = k + 1
  
  while j < nr:
    A[k] = r[j]
    j = j + 1
    k = k + 1
  print(A)
  
#MergeSort Main Function
def MergeSort(alist):
	m = len(alist)
	if m < 2:
	  return
	mid = int(m/2)
	left = list()
	right = list()
	for k in range(0, mid):
		left.append(alist[k])
	
	for l in range(mid, m):
		right.append(alist[l])
	
	MergeSort(left)
	MergeSort(right)
	Merge(left, right, alist)
	

	
num_array = list()
print("Enter number of elements to be sorted")
num = int(input())
print("Enter elements to be sorted")
for i in range(0, num):
  n = int(input())
  num_array.append(n)
print(num_array)
MergeSort(num_array)
