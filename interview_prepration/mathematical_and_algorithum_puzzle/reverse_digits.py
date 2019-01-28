t = int(input())
for i in range(t):
    #print(int(input()[::-1]))
    
    
    #x = input()
    #Y = int(x[len(x)-1:0:-1]+x[0])
    #print(Y)
    
    reverse = ''
    num = input()
    
    for i in range(len(num), 0, -1):
        reverse += num[i-1]
        
    print(int(reverse))
