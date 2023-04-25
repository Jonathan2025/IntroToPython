#Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. 
def sum_to(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum

print(sum_to(25))


# Write a function named largest() that takes a list parameter and returns the largest element in that list. 
# You can assume the list contents are all positive numbers. For example:

def largest(array):
    largestNum = max(array)
    return largestNum

print(largest([10, 4, 2, 231, 91, 54]))


# Write a function named occurrences() that takes 
# two string parameters and counts the number of occurrences of the second string inside the first string.

# first we see how many characters are there in the second string 
# if there are 1 character than thats how many we divide the first stirng by 
# if there are 2 characters, then the 1st string we divide by every two character
# plan is to first seperate the first string into individual characters
# then set up a counter
# now set up a for loop that goes through each character and then sees if the character == the second string 
# if it does then add to the counter


def occurences(string1, string2):
    len_string2 = len(string2)
    
    # based on the length of the second string divide it by the len of the 2nd string 
    # when we looked up how to divide a string, we found out about list comprehension
    string_1_divided = [(string1[i:i+len_string2]) for i in range(0, len(string1), len_string2)]

    # return string_ 1_divided --> will return the string divided 
    counter = 0
    for i in string_1_divided:
        if i == string2:
            counter+=1
    return counter

print(occurences('fleep floop', 'e'))

# another way is to do this 
def occurences(p1, p2):
   return p1.count(p2)
# The count() method is a built-in method of Python lists and strings that returns the number of occurrences of a given element or substring, respectively.

# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. 
#To do this you might have to google *args!

def product(*args):
    # WE MUST INITIALIZE total_product before the loop
    total_product = 1
    for arg in args:
        total_product *= arg
    return total_product

print(product(1,2,3))
