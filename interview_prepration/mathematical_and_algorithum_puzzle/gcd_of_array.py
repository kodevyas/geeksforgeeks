
def gcd(a,b):
    if a > b:
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
    else:
        if a == 0:
            return b
        else:
            return gcd(a, b%a)

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        list_of_no = list(map(int,input().strip(' ').split(' ')))
        if len(list_of_no) == 1:
            current_gcd = list_of_no[0]
        else:
            current_gcd = gcd(list_of_no[0], list_of_no[1])
        
            if len(list_of_no) > 2:
                for i in range(2, len(list_of_no)):
                    temp_gcd = gcd(current_gcd, list_of_no[i])
                    current_gcd = temp_gcd
        
        
        print(current_gcd)
