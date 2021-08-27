# The following is the note about Ch4.1 Python for data analysis
import numpy as np

np.random.seed(12345)

# The time cost for numpy is much less than python itself
my_arr = np.arange(1000000)
my_list = list(range(1000000))

import time

start = time.time()
my_arr2 = my_arr * 2
end = time.time()
print(f"Runtime of the numpy program is {end - start}")

start = time.time()
my_list2 = [x * 2 for x in my_list]
end = time.time()
print(f"Runtime of the python program is {end - start}")

# Array
# create 2*3 array in normal distribution
data = np.random.randn(2, 3)
print(data)

print(data.shape)

# *3 in list only operates coping
data1 = [[1, 5, 8],[3, 5, 6]]
print(data1 * 3)
# create array by array function
arr1 = np.array(data1)
print(arr1 * 3)
print(arr1.dtype)

# create array by array function
print(np.arange(5))

#create zero arrat
print(np.zeros(10))
print(np.empty((2, 3, 2)))

#convert type use astype
print(arr1.dtype)
float_arr1 = arr1.astype(np.float64)
print(float_arr1.dtype)

# arithmetic with array, element-wise function(same position)
print(arr1 * arr1)
print(arr1 - arr1)
arr2 = arr1 * 3
print(arr2)
print(arr2 > arr1)

# Slice
# Unlike list, any modification to the slice of array will change the original array
data2 = [1, 2, 3, 9]
arr3 = np.array(data2)
arr3_slice = arr3[0:3]
arr3_slice[2] = 5

print(arr3_slice)
print(arr3)

list1 = [1, 2, 3, 9]
list_slice = list1[0:3]
list_slice[2] = 5

print(list_slice)
print(list1)

#Array index
arr1d = np.array([3, 4, 6, 7 ,8])
print(arr1d[:2])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d.shape)
print(arr2d[2])
print(arr2d[2][2])
print(arr2d[2, 2])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[1])
print(arr3d[1,0])

# Using boolean to index
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
print(data)

print(names == 'Bob')
print(data[names == 'Bob', 1:])

print(names != 'Bob')
# print data not bob, pay attention to the bracket
print(data[~(names == 'Bob')])

# abbreviation
cond = names == 'bob'
print(data[~cond])

# | means OR, cannot use "and" "or"
mask = (names == 'Bob') | (names == 'Will')
print(data[mask])