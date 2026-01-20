word = input("enter the element of the ")

def vowel_count(word) :
    vowels = "aeiouAEIOU"
    
    # return sum(1 for el in word if el in vowels)

    count = 0
    for el in word :
        if el in vowels :
            count+=1
    return count
    
print (word)

print(vowel_count(word))  
            
            