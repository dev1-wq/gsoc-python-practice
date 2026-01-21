"""Problem 1: Fibonacci Series"""

# n = int(input("enter the no. : "))

# def fibonacci_series (n) :
    
#     fib_series = []
#     n1 = 0
#     n2 = 1
#     count = 0
#     if n <= 0 :
#         print("please enter the positive integer ")
#         return []
    
#     elif n == 1 :
#         return n1
    
#     else :
#         while count < n :
#             fib_series.append(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count+=1
    
#     print(fib_series)
#     return fib_series

# fibonacci_series (n)





"""problem 2 : Armstrong Number"""

n = int(input("Enter a number: "))

m = n
sum_of_powers = 0

n_str = str(n)
power = len(str(n))

while m > 0:
    digit = m % 10      
    sum_of_powers += digit ** power 
    m //= 10                
    
if n == sum_of_powers:
    print(n , "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")






    
    
    
    

