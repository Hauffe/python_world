import numpy as np

a = np.arange(12)

#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

type(a)
a.shape
a.shape = 3, 4 #Change the shape of the array, adding one dimension, then inspecting the result.

a
# array([[ 0, 1, 2, 3],
#        [ 4, 5, 6, 7],
#        [ 8, 9, 10, 11]])

a[:, 1] 

#array([1, 5, 9]

a.transpose() #Create a new array by transposing (swapping columns with rows).
# array([[ 0,  4,  8],
#        [ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11]])


# NumPy also supports high-level operations for loading, saving, and operating on all
# elements of a numpy.ndarray:

import numpy

floats = numpy.loadtxt('floats-10M-lines.txt')
floats[-3:]
#array([ 3016362.69195522, 535281.10514262, 4566560.44373946])
floats *= .5
floats[-3:]
#array([ 1508181.34597761, 267640.55257131, 2283280.22186973])
from time import perf_counter as pc
t0 = pc(); floats /= 3; pc() - t0
#0.03690556302899495
numpy.save('floats-10M', floats)

floats2 = numpy.load('floats-10M.npy', 'r+')
floats2 *= 6
floats2[-3:]