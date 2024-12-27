#!/bin/python3

#Importing
print("Importing is important:")

import sys #system functions and parmeters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #Importing with an alias
print(dt.now())

def new_line():
	print('\n')
	
new_line()

#Advanced Strings
print("Advanced strings:")
my_name = "Kevin"
print(my_name[0]) #firt initial	
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word and removing the period at end of sentence

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))
quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #Improved - case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "           hello           "  #adding a bunch of spaces then removing them, all spaces equal only one space. 
print(too_much_space.strip())

full_name = "eath Adams" 
print(full_name.replace("eath", "Heath"))
print(full_name.find("Adams"))

#Place Holders
movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title,author) 
	return fav

print(favorite_book("The Great Gatsby", "F. Scott Fitzgerald"))	

new_line()

#Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russians": 7, "Old Fashioned": 10, "Lemon Drop": 8, "Buttery Nipple": 6} #drink is key, price is value
print(drinks) 

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #add new key: value pair 
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['White Russians'] = 8
print(drinks)

print(drinks.get("White Russians"))
print(drinks.get("Martini")) #Drink that's not in the list, so returns none. 

#List and dictionaries
movies = ["When Harry Met Sally", "The Hangover", "Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Bob", "Leah", "Jeff"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)



