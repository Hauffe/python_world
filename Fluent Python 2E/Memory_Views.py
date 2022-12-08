from array import array

octets = array('B', range(6)) #Build array of 6 bytes (typecode 'B').
m1 = memoryview(octets)
m1.tolist()
m2 = m1.cast('B', [2,3]) #Build new memoryview from that previous one, but with 2 rows and 3 columns.
m2.tolist()
m3 = m1.cast('B', [3,2])
m3.tolist()
m2[1,1] = 22 #Overwrite byte in m2 at row 1, column 1 with 22.
m3[1,1] = 33
octets