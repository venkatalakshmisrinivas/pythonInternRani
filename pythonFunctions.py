import sys  
#@purpose : to print count of number of uppercase elements and number of lower case elements using Functions 
#@concept : the idea is to write a basic code and to print the count of number of upper case and lower case elements in a word using functions.
#@Hashtag : #python #coding 
#@code

def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_lowercase = 0
    count_of_uppercase = 0

    for character in arg_1:
        if character.upper() == character:
            count_of_uppercase += 1
        else:
            count_of_lowercase += 1

    print "Count of uppercase elements :",count_of_uppercase
    print "Count of lowercase elements :",count_of_lowercase

word = "PythonMLBigdataJAVA"
print "Input word :",word
count_of_lowercase_and_uppercase_letters(word)
 
#@output : COUNT of lowercase and uppercase 
