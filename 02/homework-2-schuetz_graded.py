# Grade: 14.5 / 5

#Rebecca Schuetz
#May 25, 2016
#Homework 2

#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]
#1) Display the number of elements in the list
print(len(numbers))
#2) Display the 4th element of this list.
print(numbers[3])
#3) Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])
#4) Display the 2nd-largest value in the list.
print(sorted(numbers)[-2])
#5) Display the last element of the original unsorted list
print(list(numbers)[-1])
#6) For each number, display a number: if your original number is less than 10,
#multiply it by thirty. If it's also even, add six.
#If it's greater than 50 subtract ten.
#If it's not negative ten, subtract one.
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even,
#so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)
#print('The answers I know are right')
#for number in numbers:
#    if number < 10:
#        number_less_than_10 = number * 30
#        if number % 2 == 0:
#            if number == -10:
#                print(number_less_than_10 + 6)
#            else:
#                print(number_less_than_10 + 5)
#        else:
#            print(number_less_than_10 - 1)
#    elif number > 50:
#        print(number - 11)
#    else:
#        print(number - 1)

#print('A way of doing it without the awkward minus ones')

# TA-COMMENT: Beautifullll!
for number in numbers:
    newnumber = number
    if number < 10:
        newnumber = number * 30
        if number % 2 == 0:
            newnumber = newnumber + 6
    elif number > 50:
        newnumber = number - 10
    if number == -10:  # TA-COMMENT: No need to include an else if you make your condition != -10.
        print(newnumber)
    else:
        print(newnumber - 1)
#7) Sum the result of each of the numbers divided by two.
print(sum(numbers) / 2)
#DICTIONARIES

#8) Sometimes dictionaries are used to describe multiple aspects of a single object.
#Like, say, a movie. Define a dictionary called movie that works with the following code.
movie = {'title': 'The Life Aquatic', 'year': 2004, 'director': 'Wes Anderson',
'budget': 50000000, 'revenue': 34806726}

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see:
# movie['budget'] = 65000000
# rather than "hard coding" budget and revenue into the initial dictionary.

print("My favorite movie is", movie['title'], "which was released in", movie['year'],
"and was directed by", movie['director'])

#9) Add entries to the movie dictionary for budget and revenue
#(you'll use code like movie['budget'] = 1000), and print out the difference between the two.

#10) If the movie cost more to make than it made in theaters, print "It was a flop".
#If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if movie['revenue'] < movie['budget']:
    print("It was a flop.")
if movie['revenue'] > (movie['budget'] * 5):
    print("That was a good investment.")
#11) Sometimes dictionaries are used to describe the same aspects of many different objects.
#Make ONE dictionary that describes the population of the boroughs of NYC.
#Manhattan has 1.6 million residents,
#Brooklyn has 2.6m,
#Bronx has 1.4m,
#Queens has 2.3m and
#Staten Island has 470,000.
#(Tip: keeping it all in either millions or thousands is a good idea)
population = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3,
'Staten Island': .47 }

#12) Display the population of Brooklyn.
print("Brooklyn has", population['Brooklyn'], 'million people.')
#13) Display the combined population of all five boroughs.
print("All five buroughs have", round(sum(population.values()),2), 'million people.')
#14) Display what percent of NYC's population lives in Manhattan.
print(round(population['Manhattan'] / sum(population.values()) * 100,2), "percent of NYC's population lives in Manhattan.")
