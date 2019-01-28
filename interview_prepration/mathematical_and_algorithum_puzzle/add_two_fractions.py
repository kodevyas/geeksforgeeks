
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
    #Code here
    numx = (num1*den2) + (num2*den1)
    denx = den1*den2
    
    numx_simplified = numx//(gcd(numx,denx))
    denx_simplified = denx//(gcd(numx,denx))
    
    
    print(str(numx_simplified) + '/' + str(denx_simplified))
    
    
    
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
            return(gcd(a, b%a))
