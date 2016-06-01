#Rebecca Schuetz
#May 31, 2016
#Homework 3

#LISTS
print('LISTS')
print(' ')
#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['United States of America', 'Mexico', 'Taiwan', 'France', 'United Kingdom']
#2) Using a for loop, print each element of the list
print('List of countries:')
for country in countries:
    print (country)
print(' ')
#3) Sort the list permanently.
sortedcountries = sorted(countries)
#4) Display the first element of the list
print('First country alphabetically:')
print(list(sortedcountries)[0])
print(' ')
#5) Display the second-to-last element of the list using a line of code
#that will work no matter what the size of the list is (hint: len will be helpful)
print('Second-to-last country alphabetically:')
print(list(sortedcountries)[-2])
#or you could say: print(list(sortedcountries)[len(sortedcountries)-2])
print(' ')
#6) Delete one of the countries from the list using its name (we didn't learn this in class).
sortedcountries.remove('United Kingdom')
#7) Using a for loop, print each element of the list again, which should now be one element shorter.
print('The sorted list without the United Kingdom:')
for country in sortedcountries:
    print(country)
print(' ')

#DICTIONARIES
print('DICTIONARIES')
print(' ')
#These will require LATITUDE and LONGITUDE.
#You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*.
#You can also use http://itouchmap.com/latlong.html.
#Store the latitude and longitude without the N/S/E/W -
#if the latitude is S, make it negative. If the longitude is W, make it negative.
#See here for explanation: https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8

#1) Make a dictionary called 'tree' that responds to
#'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'.
#Pick a tree from here: https://en.wikipedia.org/wiki/List_of_trees
#took the age from here: https://en.wikipedia.org/wiki/Hyperion_(tree)
#took the coordinates from here: http://wikimapia.org/25798449/Hyperion-tree
tree = {'name': 'Hyperion', 'species': 'Coast Redwood', 'age': '750', 'location_name': 'Redwood National and State Parks', 'latitude': 41, 'longitude': -124}
#2) Print the sentence "{name} is a {years old} tree that is in {location_name}"
print(tree['name'], "is an approximately", tree['age'] + "-year-old tree that is in", tree['location_name'] + '.')
#3) The coordinates of New York City are 40.7128° N, 74.0059° W.
#Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is.
#If it isn't, print "The tree {name} in {location} is north of NYC"
if tree['latitude'] < 40.7128:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is south of NYC.')
elif tree['latitude'] > 40.7128:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is north of NYC.')
else:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is on the same latitude as NYC.')
print(' ')
#4) Ask the user how old they are. If they are older than the tree,
#display "you are {XXX} years older than {name}."
#If they are younger than the tree, display "{name} was {XXX} years old when you were born."
userage = int(input('How many years old are you?'))
if userage > int(tree['age']):
    print('You are', userage - int(tree['age']), 'years older than', tree['name'] + '.')
elif userage < int(tree['age']):
    print(tree['name'], 'was', int(tree['age']) - userage, 'years old when you were born.')
else:
    print("What a coincidence! You're the same age as", tree['name'] + '!')
print(' ')
#LISTS OF DICTIONARIES
print('LISTS OF DICTIONARIES')
print(' ')
#1) Make a list of dictionaries of five places across the world -
#(1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago.
#Each dictionary should include each city's name and latitude/longitude (see note above).
places = [
    {'name': 'Moscow', 'lat': 55.7558, 'long': 37.6173},
    {'name': 'Tehran', 'lat': 35.6892, 'long': 51.3890},
    {'name': 'Falkland Islands', 'lat': -52.7963, 'long': -59.5236},
    {'name': 'Seoul', 'lat': 37.5665, 'long': 126.9780},
    {'name': 'Santiago', 'lat': -33.4489, 'long': -70.6693}
]

#2) Loop through the list, printing each city's name and
#whether it is above or below the equator (How do you know? Think hard about the latitude.).
#When you get to the Falkland Islands, also display the message
#"The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
for place in places:
    if place['name'] == 'Falkland Islands':
        print('The Falkland Islands are a biogeographical part of the mild Antarctic zone.')
    elif place['lat'] > 0:
        print(place['name'], 'is above the equator.')
    elif place['lat'] < 0:
        print(place['name'], 'is below the equator.')
    else:
        print(place['name'], 'is on the equator.')
print(' ')
#3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for place in places:
    if place['lat'] > tree['latitude']:
            print(place['name'], 'is north of', tree['name'] + '.')
    elif place['lat'] < tree['latitude']:
            print(place['name'], 'is south of', tree['name'] + '.')
    else:
            print(place['name'], 'is on the same latitude as', tree['name'] + '.')
