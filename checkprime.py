
n = int(input("Enter the Number : "))
def checkprime(n):
    if n <= 1:
        print(n, "is not a prime no.")
        return
    
    isprime = True
    

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            isprime = False
            break
        
    if isprime:
        print(n, "is prime")
    else:
        print(n, "is not a prime no.")
        
checkprime(n)
        
         