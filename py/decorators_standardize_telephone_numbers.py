n = int(raw_input())
l = []

while True:
    try:
        i=raw_input()
        l.append(i)
    except:
        break

# actually since the number n is given, we can do a for loop like:
#
# l = [raw_input() for i in range(int(raw_input()))]
#
# which is cleaner

def telephone_num(func):
    def wrapper(l): # take the according args of func
        func(["+412 " + i[-7:-4] + " " + i[-4:]  for i in l])
    return wrapper # return the decorator function

@telephone_num
def process(l):
    print '\n'.join(sorted(l))

process(l)

'''
in:
2
6528410
04419990

out:
+412 652 8410
+412 441 9990
'''