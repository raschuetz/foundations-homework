# Homework 9
#
# We're going to make a Lil' QuakeBot!!!! Please write this code as a .py file, not a Notebook.
#
# First, tips:
# READ THROUGH THE ENTIRE ASSIGNMENT BEFORE YOU BEGIN
# Be careful that you're doing all of your math with ints or floats instead of strings that look like ints or floats.
# When you write your functions, you can pass either the entire dictionary to the function
# OR just the part you're curious about
# (e.g., when you're getting the day you could send the whole earthquake dictionary or just what's in the 'time' key.)
# Writing empty functions that always return the same thing are a great way to start off.
# You can start saying every earthquake is shallow and then fill in the actual code later.
# Find out what each column name in the database means by visiting
#http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php and clicking the links for each column.
# PART ZERO: Overall description
#
# Given an earthquake defined like this...
#
#     earthquake = {
#       'rms': '1.85',
#       'updated': '2014-06-11T05:22:21.596Z',
#       'type': 'earthquake',
#       'magType': 'mwp',
#       'longitude': '-136.6561',
#       'gap': '48',
#       'depth': '10',
#       'dmin': '0.811',
#       'mag': '5.7',
#       'time': '2014-06-04T11:58:58.200Z',
#       'latitude': '59.0001',
#       'place': '73km WSW of Haines, Alaska',
#       'net': 'us',
#       'nst': '',
#       'id': 'usc000rauc'}
#
# I want to be able to run
#
#     print(eq_to_sentence(earthquake))
#
# and get the following:
#
# A DEPTH POWER, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE LOCATION.
#
# So, for example, "A deep, huge 4.5 magnitude earthquake was reported
#Monday morning on June 22 73km WSW of Haines, Alaska".
#
# DEPTH, POWER, MAGNITUDE, DAY, and TIME_OF_DAY should all come from separate functions.
#More details are in PART ONE and PART TWO.
#
# PART ONE: Write your few tiny functions
#
# First you'll need to write a few functions to help describe an earthquake.
# Try out each of these functions individually. You will probably require:
# depth_to_words will describe the earthquake's depth
# magnitude_to_words will describe the earthquake's power
# day_in_words should be the day of the week
# time_in_words should be "morning", "afternoon", "evening" or "night"
# date_in_words should be "Monthname day", e.g. "June 22"
# Any other functions as necessary
# DEPTH can be determined from the USGS website -
#http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php -
#it should be either 'shallow', 'intermediate' or 'deep'
#
# POWER should be evocative words like like 'easily ignored' or 'huge' or 'very destructive' (feel free to pick your own) - look on Google Image Search for "richter scale" to see some possible descriptors.
#
# MAGNITUDE should be the actual numerical magnitude.
#
# DAY should be the day of the week.
#
# TIME_OF_DAY should be morning, afternoon, evening or night.
#
# DATE should be "Monthname day", e.g. "June 22".
#
# TIP: You probably (a.k.a. definitely) need to convert 'time' - which is a string - into a Python datetime object which can do .hour, .day, .strftime("%Y %b %d") and other fun things. Convert it and test the conversion like this:
#
# import dateutil.parser
# timestring = '2014-06-04T11:58:58.200Z'
# yourdate = dateutil.parser.parse(timestring)
# print("The hour is", yourdate.hour)
# print("We can do things with strftime like", print(yourdate.strftime("%Y %b")))
#
# You'll need to pip install dateutils.
#
# PART TWO: Write the eq_to_sentence function
#
# Write a function called eq_to_sentence that, when called, returns the whole sentence mentioned above, "A DEPTH DESCRIPTION, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE LOCATION."
#
# Print out the result for the sample earthquake.
#
# PART THREE: Doing it in bulk
#
# Read in the csv of the past 30 days of 1.0+ earthquke activity from http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv (tip: read_csv works with URLs!)
#
# Because we haven't covered looping through pandas, use the following code to convert a pandas DataFrame into a list of dictionaries that you can loop through.
#
# earthquakes_df = pd.read_csv("1.0_month.csv")
# earthquakes = earthquakes_df.to_dict('records')
#
# (If you really want to do it with pandas, it's for index, row in earthquakes_df.iterrows():)
#
# Loop through each earthquake, printing sentence descriptions for the ones that are above or equal to 4.0 on the Richter scale.
#
# PART FOUR: The other bits
#
# If the earthquake is anything other than an earthquake (e.g. explosion or quarry blast), print
#
# There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.
#
# For example,
#
# There was also a magnitude 1.29 quarry blast on June 19 12km SE of Tehachapi, California.
#
# with TYPE_OF_EVENT being explosion, quarry blast, etc and LOCATION being 'place' - e.g. '0km N of The Geysers, California'.
