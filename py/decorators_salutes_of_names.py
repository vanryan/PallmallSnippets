# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
l = [raw_input().split() for i in range(n)]
l = sorted(l, key=lambda x: int(x[2]))

def salutes_of_names(func):
    def wrapper(l):
        func([("Mr." if i[3]=="M" else "Ms.") + " " + i[0] + " " + i[1] for i in l])
    return wrapper

@salutes_of_names
def process(l):
    print '\n'.join(l)

process(l)

'''
sorted is not in place.

In:
(lines follow each containing the space separated values of the first name, last name, age and sex, respectively)

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Out:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''