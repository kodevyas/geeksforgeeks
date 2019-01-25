
t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
        
for i in range(t):
    a, b = map(int,input().split())
    gcd_of_ab = gcd(a,b)
    print(gcd_of_ab)
    
    
