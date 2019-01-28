
t = int(input())

for i in range(t):
    binary = list(input())
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal + int(binary[i])*(2**(len(binary)-1-i))
        
    print(decimal)
