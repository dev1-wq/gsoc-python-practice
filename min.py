# n = int(input("enter the total no. of elements : "))

# my_list = []
# print("enter the elements : ")
# for i in range (n) :
#     element = int(input())
#     my_list.append(element)
    
# def find_min ()



n = int(input("Enter the number of elements: "))

my_list = []
print("Enter the elements:")
for i in range(n):

    element = int(input())
    my_list.append(element)

def find_minimum(lst):
    if len(lst) == 0:
        return None

    min_val = lst[0]
    
    for num in lst:
        if num < min_val:
            min_val = num
            
    return min_val
minimum = find_minimum(my_list)

if minimum is not None:
    print("The minimum element is:", minimum)
else:
    print("The list is empty.")
    