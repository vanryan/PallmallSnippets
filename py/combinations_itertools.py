import itertools
s, k = raw_input().split()
s = sorted(list(s))
for i in range(1, int(k)+1):
    g = itertools.combinations(s, i)
    print '\n'.join(''.join(f) for f in g)


# Even more clean:
import itertools
s, k = (lambda x: (sorted(list(x[0])), int(x[1]))) (raw_input().split())
print '\n'.join(''.join(f) for i in range(1, k+1) for f in itertools.combinations(s, i))

'''
input: HACK 2

output:
A
C
H
K
AC
AH
AK
CH
CK
HK
'''