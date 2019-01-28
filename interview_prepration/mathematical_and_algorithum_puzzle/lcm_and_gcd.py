def lcm(a,b):
    # a should be greater than b
    lcm = a
        
    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        else:
            lcm += 1
            
            
def gcd(a,b):
    #a should be greater than b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
        
        
        
        
if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        a, b = map(int, sorted(input().split(' ')))
        
        lcm_ab = lcm(a,b)
        gcd_ab = gcd(a,b)
        
        print(lcm_ab, gcd_ab)
        
