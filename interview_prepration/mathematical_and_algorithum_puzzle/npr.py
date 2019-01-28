
t = int(input())

for i in range(t):
    n, r = map(int, input().split(' '))
    
    npr = 1
    for j in range(n-r+1,n+1):
        npr = npr * j
    
    print(npr)
