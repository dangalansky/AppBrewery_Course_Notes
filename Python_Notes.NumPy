NumPy
* THE standard for working with numerical data in Python

import statement:
-import numpy as np


Definitions:

* vector —>single dimensional array

*axes —> dimensions (z, x, y), pl. of axis

*scalar—> a single number, applied to an array evenly
		ex) array = [2, 4, 5]  * 5
			—>results in: [10, 20, 25]

*broadcasting—> NumPy makes scalar into a smaller array
			—> So it will be compatible with original array

—> Bracket Usage <—
* 1 dimension
	ex) np.array([1, 2, 3]) 

* 2 dimensions (matrix)
	ex) np.array([[1, 2, 3], [5,6,7]])

*3+ dimensions (tensor)
	ex) np.array([[[1, 2, 3], [4,5,6]],
				[[ 1, 2, 3], [4,5,6]],
				[[ 1 2, 3], [4,5,6]]])

—> Retrieving Data <—
- works like any other indexed data
	ex) array[1,2]
		*retrieves the 3rd piece of data from the second column
	ex) array[0,1,3]
		*retrieves the 4th piece of data from the second column in the first tensor

** you can also use ‘:’ to retrieve entire row and all values therein
	ex) array[:, :, 0]
		* retrieves first piece of data from all columns, all tensors


Properties, and Methods of NumPy:

*ndarray —> homogeneous n-dimensional array object
	- homogeneous - all data must be same type
	-n- dimensional - can work with single column, to matrix to stacked 		matrices

* tensor - an array of 3 or more dimensions

*arange(a, b)
	—>returns vector of values ranging from a to b, without b included

*np.random.random(a, b, c)
	—> returns anywhere from random vector, to matrix to tensor
	
*.linspace()
	—>returns vector of evenly spaced numbers over a specified interval
	—>start and stop, both included in vector
	—> .astype(int) at end to return int instead of float 

.nonzero(a)
	—> returns indices of elements in array(a) that are non-zero

.flip()
	—> returns array with order reversed 

.matmul(a1, b1)
	—> returns new matrix, formed of 2 or more matrices multiplied together

