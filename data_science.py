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

from logging import captureWarnings
from msilib.schema import ServiceControl
from re import A
import threading
from types import DynamicClassAttribute
import webbrowser
import json
from urllib.request import urlopen
from xml.dom.expatbuilder import theDOMImplementation

from numpy import percentile


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

#You can extract a substring from a string by using a slice. You define a slice by using square brackets, a start offset, an end offset, and an optional step count between them
#Some of these can be omitted. The slice will include characters from offset start to one before end
#[:] extracts the entire sequence from start to end
#[ start :] specifies from the start offset to the end
#[: end] specifies from the beginning to the end offset minus 1
#[start : end] indicates from the start offset to the end offset minus 1. 
#[ start : end : step] extracts from the start offset to the end offset minus 1, skipping characters by step

#Offsets go 0,1, and so on from the start to the right, and -1,-2 and so forth from the end to the left. 
#If you don't specify start, the slice uses 0 (the beginning). If you don't specify end, it uses the end of the string

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[:]
letters[20:]
letters[10:]
letters[-3:]
letters[18:-3]
letters[-6:-2]
letters[::7]
letters[4:20:3]
letters[19::4]
letters[:21:5]
letters[-1::-1]
letters[::-1]

#The len() function counts characters in a string
len(letters)
empty = ""
len(empty)

#There are other functions specific to strings. To use a string function, type the name of the string, a dot, the name of the function, and any arguments that the function needs
#string.function(arguments)

#The split() function is used to break a string into a list of smaller strings based on some separator. A list is a sequence of values, separated by commas and surrounded by square brackets
tasks = "get gloves,get mask, give cat vitamins,call ambulance"
tasks.split(',')

#If you don't specify a separator, split() uses any sequence of white space characters-newlines, space, and tabs
#You still need the parentheses when calling split with no arguments - that's how Python knows you are calling a function

#The join() function is the opposite of split(): it collapses a list of strings into a single string. 
#You specify the string that glues everything together first, and then the list of strings to glue: string.join(list)
#To join the list lines with separating newlines, you would say '\n'.join(lines)

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join  (crypto_list)
print('Found and signing book deals:', crypto_string)

#You use replace() for simple substring substitution. It returns the changed string but does not modify the original string
#If you omit the final count argument, it replaces all instances

setup = "a duck goes into a bar..."
setup.replace("duck","goose")
setup
setup.replace("a ", "a famous ", 100)

#The strip() function is used to get rid of whitespace characters (' '. '\t', '\n'). lstrip() strips only from the left and rstrip() from the right
world = "   earth   "
world.strip()
world.strip(' ')
world.lstrip()
world.rstrip()

#You can also tell strip() to remove any character in a multicharacter string
blurt = "What the...?!!"
blurt.strip(".?!!")

import string
string.whitespace
string.punctuation
blurt.strip(string.punctuation)
prospector = "What in tarnation...??!!"
prospector.strip(string.whitespace+string.punctuation)

poem = '''All that doth flow we cannot liquid name \n Or else would fire and water be the same; \n But that is liquid which is moist and wet \n Fire that property can never get. \n Then 'tis not cold that doth the fire put out \n But 'tis the wet that makes it die, no doubt.'''
print(poem)

poem[:13]
len(poem)
poem.startswith("All")
poem.endswith("That\'s all, folks!")

word = 'the'
poem.find(word)
poem.index(word)

poem.rfind(word)
poem.rindex(word)
poem.count(word)
poem.isalnum()

setup = 'a DUCK goes into a BAR...'
setup.strip('.')
#Because strings are immutable, none of these examples actually changes the string. Each example just takes the valuye, does something to it, and returns the result as a new string
#Capitalize the first word
setup.capitalize()
#Capitalize all the words
setup.title()
#Convert all characters to uppercase
setup.upper()
#Convert all characters to lowercase
setup.lower()
#Swap uppercase and lowercase
setup.swapcase()
#Center the string within 30 spaces
setup.center(30)
#Left justify
setup.ljust(30)
#Right justify
setup.rjust(30)
#Combine functions
setup.capitalize().center(30)

#Data interpolation is used to produce reports, forms, and other outputs where appearances need to be just so
#Three additional ways of formatting strings: old style (Python 2 and 3), new style (Python 2.6 and up), and f-strings (Python 3.6 and up)

#Old style
#%s string, %d decimal integer, %x hex integer, %o octal integer, %f decimal float, %e exponential float, %g decimal or exponential float, %% a literal %
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

"My wife's favorite actor is %s" % actor
"Our cat %s weighs %s pounds" % (cat,weight)

#The %s inside the string means to interpolate a string. The numner of % appearances in the string needs to match the number of data items after the % that follows the string
#Multiple data must be grouped into a tuple (such as (cat, weight))
#Even though weight is an integer, the %s inside the string converted it to a string
#You can add other values in the format string between the % and the type specifier to designate min and max wigths, alignment, and character filling

#New style: {} and fomat()
#Used for Python 3, but f-strings are better
#Has the form format_string.format(data)
thing = 'woodchuck'
'{}'.format(thing)

#The arguments to the format() function need to be in the order as the {} placeholders in the format string
place = 'lake'
'The {} is in the {}.'.format(thing, place)

#You can also specify arguments by position:
'The {1} is in the {0}.'.format(place, thing)

#The arguments to format() can also be named arguments
'The {thing} is in the {place}.'.format(thing='duck',place='bathtub')

#F-strings
#Recommended way of formmatting strings. To make one, type the letter f (or F) directly before the initial quote. 
#Include variable names or expressions within curly brackets ({}) to get their values into the string
thing = 'wereduck'
place = 'werepond'
f'The {thing} is in the {place}'

#Expressions are also allowed inside the curly brackets
f'The {thing.capitalize()} is in the {place.rjust(20)}'

#The things you do inside format(), you can do inside a {} in your main string. 
#f-strings use the same formatting langua (widith, padding, alignment) as new-style formatting, after a ':'
f'The {thing:>20} is in the {place:.^20}'

#Print variable names as well as their values. This is handy when debugging. The trick is to have a single = after the name in the {} -enclosed part of the f-string
f'{thing=}, {place =}'

#The name can actually be an expression, and it will be printed literally:
f'{thing[-4:] =}, {place.title() = }'

#The = can be followed by a : and the formatting arguments like width and alignment
f'{thing = :>4.4}'

#Things to do
#Capitalize the word starting with m:
song = '''When an eel grabs your arm, 
And it causes great harm, 
That's - a moray!'''

song.replace(' m',' M')

#Print each list question with its correctly matching answer, in the form: 
#Q: question
#A: answer
questions = ["We don't serve strings around here. Are you a string?","What is said on Father's Day in the forest?", "What makes the sound 'Sis! Boom! Bah!'?"]
answers = ["An exploding sheep.", "No, I'm a frayed knot.", "'Pop!' goes the weasel."]
print('Q: ' + questions[0]+'\nA: ' + answers[1])
print('Q: ' + questions[1]+'\nA: ' + answers[2])
print('Q: ' + questions[2]+'\nA: ' + answers[0])

#Write the following poem by using old-style formatting. Substitute the strings 'roast beef', 'ham', 'head', and 'clam' into this string:
food1 = "roast beef"
food2 = "ham"
body_part = "head"
animal = "clam"
print("My kitty cat likes %s, \nMy kitty cat likes %s, \nMy kitty cat fell on his %s, \nAnd now he thinks he's a %s" % (food1, food2, body_part, animal))

#Write a form letter by using new-style formatting. Save the following string as letter
letter = "Dear {salutation} {name}, \nThank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}. \nSend us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent} less likely to have {verbed}. \nThank you for your support. \nSincerely, \n{spokesman} \n{job_title}"
print(letter)
salutation = "Mrs"
name = "Smith"
product = "blender"
verbed = "exploded"
room = "bathroom"
animals = "cats"
amount = "$99"
percent = "76.59%"
spokesman = "Jonas Wilson"
job_title = "Explosions manager"
letter2 = "Dear {} {}, \nThank you for your letter. We are sorry that our {} {} in your {}. Please note that it should never be used in a {}, especially near any {}. \nSend us your receipt and {} for shipping and handling. We will send you another {} that, in our tests, is {} less likely to have {}. \nThank you for your support. \nSincerely, \n{} \n{}"
print(letter2.format(salutation, name, product, verbed, room, room, animals, amount, product, percent, verbed, spokesman, job_title))

# Use % formatting to print the winning name at the state fair for a prize duck, gourd, and spitz.
duck = "Ducky McDuckface"
gourd = "Gourdy McGourdface"
spitz = "Spitzy McSpitzface"

'%s' % duck
'%s' % gourd
'%s' % spitz

#Do the same, with format() formatting.
'{}'.format(duck)
'{}'.format(gourd)
'{}'.format(spitz)

#Once more, with feeling, and f strings.
f'{duck}'
f'{gourd}'
f'{spitz}'

#The simplest looping mechanism in Python is while
count = 1
while count <= 5:
    print(count)
    count += 1
#The loop continues until count is incremented from 5 to 6 at the bottom of the loop. On the next trip to the top, count <=5 is now False, and the while loop ends

#Infinite loops with break statement (not sure if something within a loop might happen)
while True:
    stuff = input("String to capitalize (title format) [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.title())

#Instead of breaking out of a loop, you can skip ahead to the next iteration
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':        #quit
        break
    number = int(value)
    if number % 2 == 0:     #an even number
        continue
    print(number, "squared is", number*number)

#You can check the use of break with else. The else would be run if the while loop completed but the object was not found
numbers = [1, 3, 5, 8]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found an even number:', number)
        break
    position += 1
else:
    print('No even number found')

#Iteration
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

#There's an easier way to do this. String iteration produces one character at a time
word = "swift"
for letter in word:
    print(letter)

#A break in a for loop breaks out of the loop
for letter in word:
    if letter == "f":
        break
    print(letter)

#for has an optional else that checks whether the for completed normally. If break was not called, the else statement is run
#This is useful to verify that the previous for loop ran to completion instead of being stopped early with a break:
for letter in word: 
    if letter == "x":
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

#The range() function returns a stream of numbers within a specified range, without first having to create and store a larga data structure such as a list or tuple
#This lets you create huge ranges without using all the memory in your computer and crashing your program
#You use range() similar to how you use slices: range(start, stop, step). If you omit start, the range begins at 0, the only required value is stop
#Like zip(), range() returns an iterable object, so you need to step throuugh the values with for ... in, or convert the object to a sequence like a list

for x in range (0,3):
    print(x)

list( range(0,3))

for x in range (2, -1, -1):
    print(x)

list ( range(2, -1, -1))

list ( range(0,11, 2))

#Things to do
#Use a for loop to print the values of the list [3, 2, 1, 0]
for x in range (3,-1, -1):
    print(x)

#Tuples and Lists
#They are sequence structures. They contain zero or more elements. They can be of different types. Each element can be any Python object
#Tuples are immutable (elements can't be changed). Lists are mutable, you can insert and delete elements

#The syntax to make tuples is inconsistent
#Empty tuple
empty_tuple = ()
empty_tuple

#To make a tuple with one or more elements, follow each element with a comma
one_marx = 'Groucho',
one_marx

#Without the comma, you would just get the string
one_marx = ('Groucho')
one_marx
type(one_marx)

#If you have more than one element, follow all but the last one with a comma
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_tuple

#Using parentheses is a little safer, and it helps to make the tuple more visible
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_tuple

#You do need the parentheses for cases in which commas might also have another use
one_marx = 'Groucho',
type(one_marx)
type('Groucho',)
type(('Groucho',))

#Tuples let you assign multiple variables at once. This is called tuple unpacking
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
b
c

#You can use tiyples to exchange values in one statement without using a temporary variable
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
password
icecream

#The tuple() conversion function makes tuples from other things:
marx_list = ['Groucho','Chico', 'Harpo']
tuple(marx_list)

#The + sign is used to concatenate tuples
('Groucho',) + ('Chico', 'Harpo')

#And the * sign is used to duplicate items
('yada',) * 3

#Comparing tuples
a = (7, 2)
b = (7, 2, 9)
a == b
a <= b
a < b

#Tuple iteration is like iteration of other types:
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

#Tuples CANNOT be modified. Like strings, tuples are immutable, so you can't change an existing one.
#You can concatenate tuples to make a new one, as you can with strings
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1+t2
t1+=t2
t1
#When concatenating, Python makes a new tuple from the original tuples pointed to by t1 and t2, and assigned the name t1 to this new tuple
#But the original t1 was not changed. A new one was created and the same name was reused

#Lists are good for keeping track of things by their order, especially when the order and contents might change. Lists are mutable
#You can change a list in place, add new elements, and delete or replace existing elements. The same value can occur more than once in a list

#A list is made from zero or more elements, separated by commas and surrounded by square brackets
empty_list = []
weekdays = ['Monday','Tuesday','Wednesday','Thursday', 'Friday']
big_birds = ['emu','ostrich','cassowary']
first_names = ['Graham','John','Terry','Terry','Michael']
leap_years = [2000,2004,2008]
randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]

#If you want to keep track of only unique values and don't care about order, a Python set might be a better choice than a list

#The list() function is used to create empty lists
another_empty_list = list()
another_empty_list

#The function also converts other iterable data types (such as tuples, strings, sets, and dictionaries) to lists
list('cat')

a_tuple = ('ready','fire','aim')
list(a_tuple)

#You can use split() to chop a string into a list
talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day.split('/')

#If you have more than one separator string in a row, you get an empty string as a list item
splitme = 'a/b//c/d///e'
splitme.split('/')
splitme.split('//')
splitme.split('///')

#You can extract a single value from a list by specifying its offset
marxes = ['Groucho','Chico','Harpo']
marxes[0]
marxes[1]
marxes[2]
marxes[-1]
marxes[-2]
marxes[-3]

#You can extract subsequences with slices
marxes[0:2]

#A slice of a list is also a list
#As with strings, slices can step by values other than one
marxes[::2] #This example starts at the beginning and goes right by 2
marxes[::-2] #Here we start at the end and go left by 2
marxes[::-1] #This reverses a list

#None of these examples changed the marxes list itself, because we didn't assign them to marxes
#To reverse a list in place, use list.reverse(). This function changes the list but doesn't return its value
marxes.reverse()
marxes

#A slice can specifiy an invalid index, but will not cause an exception, it will "snap" to the closest valid index or return nothing
marxes[4:]
marxes[-6:]
marxes[-6:-2]
marxes[-6:-4]

#The traditional way of adding items to a list is to append() them one by one to the end
marxes.append('Zeppo')
marxes

#The append() function adds items only to the end of the list. To add an item before any offset, use insert()
#Offset 0 inserts at the beginning, one beyond the end inserts at the end, like append()
marxes.insert(2, 'Gummo')
marxes

#Duplicate lists with *
['blah'] * 3

#You can merge one list into another by using extend()
others = ['Karl']
marxes.extend(others)
marxes

#You can also change the value of a list item by its offset
marxes[3] = 'Wanda'
marxes

#You cant change a character in a string in this way, because strings are immutable. Lists are mutable, you can change how many items a list contains as well as the items themselves

#You can assign values to a sublist with a slice
numbers = [1,2,3,4]
numbers[1:3] = [7,8,9]
numbers
numbers[1:3] = []
numbers

#Any Python iterable will do, separating its items and assigning them to list elements
numbers[1:3] = (98,99,100)
numbers
numbers[1:3] = 'wat?'
numbers

#Delete an item by offset with del
del marxes[-1]
marxes
#When you delete an item by its position in the list, the items that follow it move back to take the deleted item's space, and the list's length decreases by one
#del is a Python statement, not a list method, it's sort of the reverse of assignment (=): it detaches a name from a Python object and can free up the object's memory if that name were the last reference to it

#To delete an item by value, use remove(). If you have duplicate list items, it deletes only the first one it finds
marxes.remove('Wanda')
marxes

#You can get an item from a list and delete it at the same time by using pop()
#If you call pop() with an offset, it will return the item at that offset; with no argument it uses -1 
#So, pop(0) returns the head (start) of the list, and pop() or pop(-1) returns the tail (end)
marxes.pop()
marxes
marxes.pop(1)
marxes

#If you use append() to add new items to the end and pop() to remove them from the same end, you’ve implemented a data structure known as a LIFO 
#(last in, first out) queue. Commonly known as a stack. pop(0) would create a FIFO (first in, first out) queue.
#Useful when you want to collect data as they arrive and work with either the oldest first (FIFO) or the newest first (LIFO)

#The clear() function clears a list of all its elements
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
work_quotes
work_quotes.clear()
work_quotes

#If you want to know the offset of an item in a list by its value, use index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')

#If the value is in the list more than once, only the offset of the first one is returned
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
simpsons.index('Bart')

#in is used to check for the existence of a value in a list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes

#The same value may be in more than one position in the list. As long as it's in there at least once, in will return True
words = ['a', 'deer', 'a' 'female', 'deer']
'deer' in words
'male' in words

#If you check for the existence of some value in a list often and don’t care about the order of items, 
#a Python set is a more appropriate way to store and look up unique values

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.count('Harpo')
marxes.count('Bob')

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
snl_skit.count('cheeseburger')

#the join() function is useful to combine items. It's a string method, not alist method. join() is the opposite of split()
marxes = ['Groucho', 'Chico', 'Harpo']
', '.join(marxes)

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
joined
separated = joined.split(separator)
separated
separated == friends

#To sort the items in a list by their values rather than their offset, Python provides two functions:
#sort() sorts the list itself in place
#sorted() reutrns a sorted copy of the list 

#If the items in the list are numeric, they're sorted by default in ascending numeric order. If they're strings, they're sorted in alphabetical order
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
sorted_marxes

#sorted_marxes is a new list, creating it did not change the original list
marxes

#Calling the list function sort() on the marxes list does change it
marxes.sort()
marxes

#If the elements of a list are all the same type (such as strings), sort() will work correctly
#Some types, like integers and floats, can be mixed because they are automatically converted to one another by Python
numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers

#The default sort order is ascending, but you can add the argument reverse=True to set it to descending
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
numbers

#len() returns the number of items in a list 
marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)

#When you assign one list to more than one variable, changing the list in one place also changes it in the other
a = [1,2,3]
a
b = a
b
a[0] = 'surprise'
a
b
b[0] = 'I hate surprises'
b
a