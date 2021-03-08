import numpy 

# Making a list to a numpy array...
arandomlist = [1, 2, 4, 8, 3, 6]

myarray = numpy.array(arandomlist)
print(myarray) 
 # OUTPUT - [1 2 4 8 3 6]
  
  
# Ascending order 
# We use the numpy array for this...
h = numpy.sort(myarray)
print(h)
# Outputs - [1 2 3 4 6 8]

# Descending order 
# The same shit...
i = -numpy.sort(-myarray)
print(i)
# Outputs - [8 6 4 3 2 1]

# Multiply the array with 2 :)
j = numpy.sort(myarray)
print(2*myarray)
