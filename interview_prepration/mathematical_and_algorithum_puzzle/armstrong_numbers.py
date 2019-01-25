#code

t = int(input())

for i in range(t):
    n= input()
    number = list(n)
    #print(number)    #for debugging
    armstrong = 0
    for i in number:
        armstrong = armstrong + int(i)**3
        
    if armstrong == int(n):
        print('Yes')
    else:
        print('No')
