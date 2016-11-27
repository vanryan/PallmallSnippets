'''
1 GB memory can hold the int objects from 0 to 89478486, if a PyIntObject has a size of 12 bytes.

In int_dealloc, no memory will be given back to the system heap until the python process is over, which is kind of like memory leak.

Run in Python 2.7.11, on Macbook Pro mid 2015, 2.5 Ghz i7, 16 GB 1600 MHz DDR3, num1 in this process takes around 2.72GB memory
'''

l = list()

num1 = 89478486
num2 = 178956971

def cal():
	for i in range(0, num1):
	    l.append(i)
	    if len(l) % 10000000 == 0:
	        l[:] = []

#dis.dis(cal)

'''
for i in range(0, 178956971):
    pass
'''
