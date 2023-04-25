# Python is mostly used in data science, but can also be used in web development 

# Naming conention 
# snake_case 

# Core Syntax 
# Python uses line breaks and whitespace instead of semicolors and curly braces
# Colons replace curly brackets in js 

# variables 
# by default, all variables are locally scope, so you can just do name ="jonathan", instead of let nam="jonathan"

# Floats and integers 
# unlike JS, python has seperate data types for integers and floats 

#Booleans 
# True or False, you would not see null


# OPERATORS 
# Loose vs Strict Comparison 
# == in python os the === strict compairosn operator in JS



#============================
# 4.24 Monday April 24, 2023
# Introduction to single line comment 

'''
This is a multiline comment, so you can use the triple quotes to do this 

'''

# There is no difference between using "" or ''
# the equivalent to console log is print 
print("Hello world")

print("This is how we add a \n new line")


# String interpolation 
thing_to_do = "Take it"
way_to_do = "easy"
pronoun = "dude"

# .format() method is apprendeed to a string and takes parameters of strings to be concatenated 
print(
  "{} {} {}. But {}".format(thing_to_do, way_to_do, pronoun, thing_to_do)
)

# this is doing the same thing but using indexes of the parameters
print(
  "{0} {1} {2}. But {0}".format(thing_to_do, way_to_do, pronoun)
)

# A newer and better option is called f strings and was introducted in Python 3.6, similar to string interpolation in js
print(
  f"{thing_to_do} {way_to_do} {pronoun}. But {thing_to_do}!"
)

# list in python 
animals = ["lions", "tigers", "bears"]

print(animals[0])

# we can also use negative indexes
# with -1 returning the last item and then -2 returning the second to last
print(animals[-1])

# the len() method is used to get the length of a list in python 
print(len(animals))

# Now we can MERGE lists together 
secret_files = ["TOP SECRET", "ALSO TOP SECRET", "DON'T EVEN LOOK AT THIS"]
new_secret_files = ["PRETTY DARN SECRET", "WE SEEM NOT TO BE TRUSTED QUITE AS MUCH WITH TOP SECRET", "MAYBE IT'S THAT WE LEAVE SECRETS IN ALL CAPS IN PLAIN TEXT"]

# now lets merge these lists together
secret_files = secret_files + new_secret_files
print(secret_files)


# we can use the .append method instead of push() in js 
secret_files.append("He's Guilty.")
print(secret_files)

# we cna use the .pop() method to remove the last element from a list 
secret_files.pop() 
print(secret_files)


# now we can also choose where we want to remove, remove the second element 
secret_files.pop(1)
print(secret_files)

# if we want to remove a specific element we can use the remove
secret_files.remove("TOP SECRET")
print(secret_files)


# =========================================
# Dictionaries 
# Dictionaries are similar to objects in js 

student = {
  'name': 'Jonathan',
  'course': 'Data Science Immersive',
  'current_week': 4
}

# dictionaries are unordered just like in javascript
# they are also mutable 
name = student['name']
print(name)

# now we can change the dictionary 
student['name'] = 'Turtle'
name = student['name']
print(name)

# how to create a new key value pair 
# birthdate = student['birthdate']
# print()


# lets try to get a value for a key if we are not sure it exists 
print(student.get("birthday", "Value not in list"))
# None is the equivalent of null, meaning no value exists 


# you can use the in operator to see if a value exists 
#for if statements there are no curly brackets only indentation, and we need colons
import datetime
# if 'birthdate' in student:
#   today = datetime.datetime.today()
#   is_birthday = (student['birthdate'].month == today.month and student['birthdate'].day == today.day)

# creating a new key value 
student['age'] = 21
print(student['age'])

# deleting a key value 
# del operator delete an item form a dictionary 
del student['age']
# print(age in  student)
# we will get age is not defined since it was deleted

print(student)

# count the key value pairs 
print(len(student))