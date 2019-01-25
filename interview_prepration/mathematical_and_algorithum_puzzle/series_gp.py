#code
from math import floor
t = int(input())

for i in range(t):
    a, b = map(int, input().split(' '))
    r = b/a
    
    n = int(input())
    
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
        
    else:
        n_term = a*(r**(n-1))
        print(floor(n_term))
