"""Concatenate

Two or more arrays can be concatenated together using the concatenate function
with a tuple of the arrays to be joined:

import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))

#Output
[1 2 3 4 5 6 7 8 9]

If an array has more than one dimension, it is possible to specify the axis
along which multiple arrays are concatenated. By default, it is along the first dimension.

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]

Task

You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column).
Your task is to concatenate the arrays along axis 0.

Input Format

The first line contains space separated integers N, M and P.
The next  lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size (N + M) x P.

Sample Input

4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] """


import numpy as np

# assigns value to n, m, p as type int
n, m, p = map(int, input().split())
# creates array of int type and for range of n
arr_n = np.array([input().strip().split() for _ in range(n)], int)
# creates array of int type and for range of m
arr_m = np.array([input().strip().split() for _ in range(m)], int)
# shapes arr_n, arr_m into array of shape (nxp & mxp)
ar_n = arr_n.reshape(n, p)
ar_m = arr_m.reshape(m, p)
print(np.concatenate((ar_n, ar_m), axis=0))

