#Variables

character_name = "Anna"    #storing strings
character_age = "22"       #storing numbers as string for concatenation
age = 50                   #store numbers
is_Female = True           #storing boolean

print("There was a person named " + character_name + " and was " + character_age + " years old")

#Working with Strings

print("Zero\nHero")    #New lines
print("Zero\"Hero")    #Print "" with \ 
print("Zero\Hero")

phrase = "Hello"
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase)
    #Indexing
print(phrase[0])
print(phrase.index("e"))
print(phrase.replace("Hello","good"))


#Working with Numbers

print(8 % 3)        #Gives Remainder aka modulus operator
num = -10
print(str(num))     #Turn number to string
print(abs(num))     #Absoluote value
print(pow(3,2))     #Square
print(max(4,6))
print(round(3.7))

# Import more math functions

from math import *

print(floor(3.3))  #Rounds to Lower Number
print(ceil(3.1))   #Rounds to Higher number
print(sqrt(36))    #Square Root


# Get input from user

name = input("Enter your name: ")
age = input("Enter age: ")
print("Hello " + name + "! You are " + age)


# Build Calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)      #Can also use int() for whole numbers only, float does decimal as well       

print(result)


# Mad Libs
color = input("Enter a color: ")
noun = input("Enter a noun: ")
person= input("Enter a person: ")

print("Roses are " + color)
print(noun + " are blue")
print("I like " + person)


# Lists

friends = ["Kat", "Bob", "Lex", "Ellen", "Tobby"]
print(friends)
print(friends[1])
print(friends[-1])
print(friends[2:4])
friends[1] = "Mike"

    #List Functions

scores = [20, 4, 5 , 5, 7 , 8]
players = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Toby"]
players.extend(scores)
print(players)
players.append("Creed")
print(players)
players.insert(1,"KELLY")
print(players)
players.remove("Kevin")
print(players)
# removes everything players.remove()
players.pop("Oscar")
print(players)

print(players.count("Toby"))

print(scores.sort())
print(scores.reverse())

players2 = players.copy()
print(players2)



#Tuples- not changeable= immutable;used for when data never change

coordinates = (4,5)
print(coordinates[0])

#Functions

def say_hi(name, age):
    print("Hello" + name + "you are" + age)

say_hi("Mike" , 8)


def cube(num):
    return num*num*num

print(cube(3))


# IF statements



























































