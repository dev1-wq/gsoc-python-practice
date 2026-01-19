n = int(input("enter the no. : "))

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    if n == 0:
        return 1
    
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
        
    return fac

print(factorial(n))