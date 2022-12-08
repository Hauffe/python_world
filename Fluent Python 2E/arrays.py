from array import array
from random import random

flaot_values = array('d', (random() for i in range(10**7)))
flaot_values[-1]
fp = open('floats.bin', 'wb')
flaot_values.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2 == flaot_values
#should be true
