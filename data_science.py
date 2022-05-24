#!/bin/python3
users=[
    {"id":0,"name":"Hero"},
    {"id":1,"name":"Dunn"},
    {"id":2,"name":"Sue"},
    {"id":3,"name":"Chi"},
    {"id":4,"name":"Thor"},
    {"id":5,"name":"Clive"},
    {"id":6,"name":"Hicks"},
    {"id":7,"name":"Devin"},
    {"id":8,"name":"Kate"},
    {"id":9,"name":"Klein"}
]

friendship_pairs=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

friendships={user["id"]:[] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id=user["id"]
    friend_ids=friendships[user_id]
    return len(friend_ids)

total_connections=sum(number_of_friends(user)for user in users)

num_users=len(users)
num_users
avg_connecations=total_connections/num_users
avg_connecations

num_friends_by_id=[(user["id"],number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1],reverse=True)
num_friends_by_id

for countdown in 5,4,3,2,1, "heeey! :)":
    print(countdown)

spells = [
    "Riddikulus!",
    "Wingardium Leviosa!",
    "Avada Kedavra!",
    "Expecto Patronum!",
    "Nox!",
    "Lumos!",
    ]
print(spells[3])

#quotes is a variable that names a Python dictionary, a collection of unique keys and associated values
#Using dictionaries helps store and look up things by name, useful alternative to a list
quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
}
stooge = "Curly"
print(stooge,"says:",quotes[stooge])

#Square brackets [] are used to make lists, and curly brackets {} to make dictionaries
#Colons (:) are used to associate each key in the dictionary with its value
#JSON format (JavaScript Object Notation), a human-readable text format that describes the types, values, and order of the data within it
#Python programs can translate JSON text into Pyhton data structures

from msilib.schema import ServiceControl
from re import A
import webbrowser
import json
from urllib.request import urlopen


print("Let's find an old website")
site=input("Type a website URL: ")
era=input("Type a year, month, and day, like 20150613: ")
url="http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents=response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)

#Java, C, C++ are static languages. They require to specify some low-level details like data types
#Dynamic languages (scripting languages) do not force to declare variable types before using them

#Pyhton, fastest growing major programming language. Popular in data science and machine learning. General-purpose, high-level language.
#Readable, makes it easy to learn and remember. More writable

#Objects are chunks of data that contain at least: a type (defines what it can do), a unique id, a value (consistent with its type), and a reference count (tracks how often the object is used)
#Mutable = can an object be changed after creation (lists, bytearrays, sets and dictionaries are mutable)
#When creating a variable, data types do not need to be defined
#Python is strongly typed, the type of an object does not change, even if its value is mutable 

help("keywords")

x = 5
y = x + 12
y

#When a value is not assigned to a variable, that variable is considered uninitialized
#Variables are just names, assignments do not copy a value, they attach a name to the object that contains the data
#The name is a reference to the thing rather than the thing itself

a = 7
print(a)
b = a
print(b)

#To check the type of anything (a variable or a literal value). type() is a Python built-in function
type(7)
type(7)==int
isinstance(7,int)

#A class is the definition of an object. "class" and "type" mean the same thing
#When an object's reference count reaches zero, it doesn't need to stick around. Garbage collector reuses the memory of things that are no longer needed

#It's possible to assign a value to more than one variable name at the same time
two = deux = zwei = 2
two
deux
zwei 

#Changing the value assigned to a name just makes the name point to a new object. The reference count of the old object is decremented, and the new one's incremented
#If the object is immutable, its value cannot be changed. Both names are essentially read-only
x=5
x
y=x
y
x=29
x
y

#If both names point to a mutable object, the object's value can be changed via either name, and the changed value is seen with either name
a=[2,4,6]
b=a
a
b
a[0]=99
a
b

#Things to do
prince = 99
print(prince)
type(5)
type(2.0)
type(5+2.0)

#The python function bool() can convert any Python data type to a boolean. However, any zero valued one is considered False
bool(True)
bool(1)
bool(45)
bool(-45)
bool(False)
bool(0)
bool(0.0)

#Integers are whole numbers (no fractions, no decimals). You can't have an initial 0 followed by a digit between 1 and 9.
#Commas are NOT used as digit separators, underscores (_) are. 100_000_000 or 1_2_3, they are just ignored
#Math operators are used to perform normal arithmetic. + - * / // (integer division, gives whole numbers as answers) % (remainder) ** (exponentiation)
#Variables and literals can be mixed during operations
a = 95
a - 3 
#Answer=92. This does NOT change the value of a (a = 95). To do that:
a = a - 3
#Simplified notation
a -= 3
#Works the same with +, *, /, // or -
#The % has a lot of uses in Python. When it is between two number, it produces the remained when the first is divided by the second
#The divmod() function calculates the truncated quotient and remained at once
divmod(9,5)

#Multiplication has higher precedence than addition, it's easier to just add parentheses
#Integers are assumed to be decimal (base 10) unless you use a prefix to specify another base. 0b (base 2), 0o (base 8), 0x (base 16)
#The chr() function converts an integer to its single-character string equivalent, ord() goes the other way
chr(65)
ord("A")

#To change other Python data types to an integer, use the int() function. It takes one input argument and returns one value, the integerized equivalent 
#of the input argument. This keeps the whole number and discards ny fractional parts
int(True)
int(False)
#The bool() function returns the boolean equivalent of an integer
bool(1)
bool(0)

#The int() function converts something into an integer
a = '99' #Because it is bewteen '', it's a str
type(a) #<class> 'str'
int('99') #Transforms a string into an integer
int(a) #Transforms the str into an int ('99' to 99)

#The int() function will make integers from floats or strings of DIGITS, but it won't handle strings containing decimal points or exponents
#In Python3, an int can be any size, even greater than 64 bits. There are even googols or googolplexes
#Trying this would cause an integer overflow, where the number would need more space than the computer allowed for it, with various bad effects.
#Python handles googoly integers with no problem 

#Floating-point numbers (called floats) have decimal points or exponents (e)
#Floats are handled similarly to integers, the operators and divmod() function are still used
#To convert other types to floats, you use the float() function. Booleans act like tiny integers, integers gain a decimal point and strings become numbers
float(True)
float(False)
float(98)
float('97.7')

#When ints and floats are mixed, Python promotes the integer values to float values
43 + 2.

#Things to do
seconds_per_hour = (60 * 60)
seconds_per_day = seconds_per_hour * 24
seconds_per_hour//seconds_per_day

#Continuation characters (\) are used to continue lines, with these Python will act as if you are still in the same line
sum = 0
sum +=1
sum +=2
sum +=3
sum +=4
sum
#Is exactaly the same as
sum = 1 + \
      2 + \
      3 + \
      4
sum
#Or the same as
sum = (
    1 +
    2 +
    3 + 
    4)
sum

#If, elif and else, are conditionals. These statements check wether a condition is a boolean True value
#print() is Python's built in function to print things (to your screen)

disaster = True
if disaster: 
    print("Woe!")
else:
    print("Whee!")

furry = False
large = True
if furry:
    if large:
        print("It's a yeti!")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")

#In Python, indentation determines how the if and else sections are paired. 
#If there are more than two possibilities to test, use if for the first, elif for the middle ones, and else for the last.
color = "periwinkle"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple": 
    print("I don't know what that is, but only bee can see it")
else: 
    print("I've never heard of the color", color)

#Equality, ==. Inequality !=. Less and greater than <, >. >= and <=. These return boolean values (T or F)
#A single equal sign is used to assign a value to a variable. X = 5 
x = 5
x == 6
x > 3
10 < x
x == 6 - 1

#If you need to do multiple comparisons at once, you use logical operators, and, or, not. 
#Logical operators have lower precedence than the chunks of code they're comparing. Chunks are calculated first, then compared
x = 5
5 <= x and x > 10
4 < x or x > 1

y = 4
y > 2 and not y < 1
y == 4 and y > 3

#You can also "and" multiple comparisons at once
y>3<5
5 > y < 10
5 > y < 10 < 100

#Many things are considered Flase by Python, like null, zeros, empty strings, lists, dictonaries, etc...
#Anything else is considered True. Python programs use these definitions of “truthiness” and “falsiness” 
#to check for empty data structures as well as False conditions
some_list = ["Hola",1,"Dos",3]
some_list
if some_list:
    print("There's something there!")
else:
    print("Hey, it's empty!")

letter = "o"
if letter == "a" or letter == "e" or letter == "i" \
    or letter == "o" or letter == "u":
    print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")

#If you need to make a lot of comparisons, separator by or, use Python's membership operator in. It can be used with a lot of data types (sets, lists, tuples, dictionaries...)
vowels = 'aeiou'
letter = 'o'
letter in vowels
if letter in vowels:
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
 

vowel_dict = {'a':'apple', 'e':'elephany','i': 'impala', 'o':'ocelot','u':'unicorn'}
letter in vowel_dict

#The walrus operator (:=) is used to combine assignments and tests
tweet_limit = 280
tweet_string = "HOLAAA " * 100
tweet_string
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

tweet_limit = 280
tweet_string_2 = "holiii" * 100
len(tweet_string_2)
if diff := tweet_limit - len(tweet_string_2) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

#Things to do
secret = 6
guess = 7
if guess > secret:
    print("Too high!")
elif guess < secret:
    print("Too low!")
else:
    print("You got it!")

small = True
green = False
if small:
    if green:
        print("It's a pea")
    else:
        print("It's a cherry")
else:
    if green:
        print("It's a watermelon")
    else: 
        print("It's a pumpkin")


#Strings are a example of a Python sequence, a sequence of characters
#A character is the smallest unit in a writing system, it includes letters, digits, symbols, punctutation, and even white space
#A character is defined by its meaning (how it's used), noy how it looks.
#Strings in Python are immutable. You can't change a string in place, but you can copy parts to another string to get the same effect
#f strings, formatting
#raw strings, preven escape sequences in the string
#fr strings, raw f-strings
#u, unicode strings
#b, bytes
#You can have quotes inside double-quoted strings, or double quotes inside single-quoted strings
"'Nay!' said the naysayer. 'Neigh?' said the horse."
'A "two by four" is actually 1 1/2" x 3 1/2"'

#You can also use three single quotes (''') or three double quotes ("""). Their most common use is to create multiline strings.
'''Boom!'''
"""Eek!"""
'''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''

#The print function is meant for human output
#Python uses the str() function internally when you call print() with objects that are not strings and when doing string formatting
#By preceding a character with a backslash (\), you give it special meaning. The most common escape sequence is \n, means to begin a new line
palindrome = 'A man \nA plan \nA canal: \nPanama.'
print(palindrome)

#The escape sequence \t (tab) is used to align text:
print('\tabc')
print('a\tbc')
print('ab\tc')

#You might also need \' or \" to specify a literal single or double quote inside a string that's quoted in the same character
testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
testimony
print(testimony)

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)

#If you need a literal backslash, type two of them (the first escapes the second)
speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)

#A raw string negates these escapes
info = r'Type a \n to get a new line in a normal string'
print(info)

#You can combine literal strings or string variables in Python using the + operator
#You can also combine literal strings just by having one after the other
#Python does NOT add spaces when concatenating strings. They must be added explicitly. It does add a space between each argument to a print() statement a newline at the end
#You can use the * operator to duplicate a string. It has a higher precedence than +

#To get a single character from a string, specify its offset inside square brackets after the string's name
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
letters[22]

#If you specify an offset that is the length of the string or longer, you’ll get an exception
letters[26]

#Because strings are immutable, you can’t insert a character into a str or change the character at a specific index
#You can use some combination of functions like replace() to do so. The value of the variable does not change, only the result is printed
name = "Henny"
name.replace('H','P')
name
'P'+name[1:]
name

