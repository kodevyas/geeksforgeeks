from math import sqrt

t = int(input())

for testcase in range(t):
    n = int(input())
    
    factor_sum = 1
    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            factor_sum += i
            factor_sum += n//i
            
            
    if factor_sum == n:
        print(1)
    else:
        print(0)
