from itertools import product
from math import sqrt

t = int(input())


def no_of_primes(n):
    no_list = []
    
    for i in range(n+1):
        no_list.append(True)
        
    no_list[0] = False
    no_list[1] = False
    
    for i in range(2, n+1):
        if no_list[i] ==  True:
            for j in range(2*i, n+1, i):
                no_list[j] = False
                
    enumerated_list = list(enumerate(no_list))
    
    
    prime_factors = []
    for i in enumerated_list:
        #print(i)
        if i[1] == True:
            prime_factors.append(i[0])

    return prime_factors
            
    
    
if __name__ == '__main__':
    for i in range(t):
        n = int(input())
    
        prime_factors = no_of_primes(n//2)
        pair_of_primes = list(product(prime_factors, prime_factors))

        
        for i in pair_of_primes:
            if i[0]*i[1] <= n:
                print(*i, end=' ')
        print('')
    
    

