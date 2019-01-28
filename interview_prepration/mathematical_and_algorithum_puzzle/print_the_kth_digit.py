t = int(input())

for i in range(t):
    a, b, r = map(int, input().split(' '))
    
    a_power_b = list(str(a**b))
    
    print(a_power_b[-r])
    
