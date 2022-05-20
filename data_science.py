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

from re import A
import webbrowser
import json
from urllib.request import urlopen

from numpy import infty

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

