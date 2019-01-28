t = int(input())

for i in range(t):
    n = int(input())
    factorial = 1
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        for i in range(1,n+1):
            factorial *= i
        print(factorial)
