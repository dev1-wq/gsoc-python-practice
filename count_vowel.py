# Count vowels in a string

s = input("Enter a string : ")
def count_vowel (s) :
    vowels = "aeiouAEIOU"
    
    # return sum(1 for el in s if el in vowels )
    count = 0
    for el in s :
        if el in vowels :
            count += 1
            
    return count


print(s)
print(count_vowel(s))
    
    


 