
for i in range(t):
    n = int(input())
    no_list = []
    
    for i in range(n+1):
        no_list.append(True)
    
    
    no_list[0] = False
    no_list[1] = False
    for i in range(2,n+1):
        if no_list[i] == True:
            for j in range(i*2, n+1, i):
                no_list[j] = False
    
    enumerated_list = list(enumerate(no_list))
    for i in enumerated_list:
        if i[1] == True:
            print(i[0], end=' ')
        
    print('')
