#!/bin/python3

#Lists
print("Lists have brackets:")
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exocist"]

print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("Jaws")
print(movies)

movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exocist"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

print("While loops - Execute as long as True:")	
i = 1
while i <= 10:
	print(i)
	i += 1
	
	
