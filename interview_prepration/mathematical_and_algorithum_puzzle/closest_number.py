
t = int(input())

for i in range(t):
    n,m = map(int,input().split(' '))
    output = 0
    if abs(n%m)> abs(m)/2:
        output = (n//m + 1)*m
    elif abs(n%m) == abs(m)/2:
        output1 = (n//m + 1)*m
        output2 = output=(n//m)*m
        if abs(output1) > abs(output2):
            output = output1
        else:
            output = output2
    else:
        output=(n//m)*m
        
        
    print(output)
