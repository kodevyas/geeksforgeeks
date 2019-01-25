#code

t = int(input())

for i in range(t):
    number = list(map(int,list(input())))
    new_number = 0
    for n in number:
        new_number = new_number + n
    
    new_number = list(str(new_number))
    
    pallindrome = True
    for i in range(len(new_number)//2):
        if new_number[i] != new_number[len(new_number) - i - 1]:
            pallindrome = False
            
    if pallindrome == True:
        print('YES')
    else:
        print('NO')
