n = int(input("enter the no. :"))

def is_palindrome(n):
    if n < 0:
        return False
    
    m = n
    reversed_no = 0
    
    while m > 0:
        digit = m % 10
        reversed_no = (reversed_no * 10) + digit
        m = m // 10
    if reversed_no == n:
        print("is pelindrome")
        return True
    
    else:
        print("not a pelindrome")
        return False
    
is_palindrome(n)
    