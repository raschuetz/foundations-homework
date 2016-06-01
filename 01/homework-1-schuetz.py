#Rebecca Schuetz
#May 23, 2016
#Homework 1
birthyear = int(input("What's your year of birth?"))
if birthyear > 2016:
    birthyear = int(input("What's your year of birth?"))
age = 2016-birthyear
print("You are about", age, "years old.")
#human heart
#assuming your heart beats 42048000 times a year, not taking leap years into account
print("Your heart has beat approximately", int((round((age * 42048000),-9))*(.000000001)), "billion times.")
#blue whale heart
#assuming a blue whale's heart beats 6 times per minute (3153600 times a year), not taking leap years into account
#http://www.cardio-research.com/quick-facts/animals
#print("whale")
#print(6*60*24*365)
print("A blue whale's heart has beat approximately", int((round((age * 3153600),-6))*(.000001)) , "million times in your lifetime.")
#rabbit heart
#assuming a rabbit's heart beats 150 times per minute (78840000 times a year), not taking leap years into account
#print("rabbit")
#print(150*60*24*365)
print("A rabbit's heart has beat approximately", int((round((age * 78840000),-9))*(.000000001)), "billion times in your lifetime.")
#venus years
#assuming venus takes 224.7 Earth days to complete one orbit, taking leap years into account
#http://www.universetoday.com/14319/how-long-is-a-year-on-venus/
#one venus year is 365.2/224.7 earth years
print("On Venus, you are", int((age * (365.2/224.7))), "years old,", (int((age * (365.2/224.7))) - age), "years older than you are on Earth.")
#neptune years
#assuming neptune takes 60,182 Earth days to complete one orbit, taking leap years into account
#assuming neptune takes 0.67125001 Earth days to complete one rotation, taking leap years into account
#tried to figure out how many days, but gave up> but", int(age * (0.67125001/365.2)), "days old."
#http://www.universetoday.com/37507/years-of-the-planets/
print("On Neptune, you are", round((age * (365.2/60182)),2), "years old,", (age - round((age * (365.2/60182)),2)), "years younger than you are on Earth.")
#odd or even birthyear
if birthyear % 2 == 0:
    print("You were born on an even year.")
else:
    print("You were born on an odd year.")
#Pittsburgh Superbowl Wins (1974, 1975, 1978, 1979, 2005, 2009)
#assuming that if they've been alive in a year, they weren't born after the Superbowl
if birthyear < 1975:
    print ("The Steelers have won 6 Superbowls while you've been alive.")
elif birthyear >= 2009:
    print ("The Steelers have won 0 Superbowls while you've been alive.")
elif birthyear >= 2006:
    print ("The Steelers have won 1 Superbowl while you've been alive.")
elif birthyear >= 1980:
    print ("The Steelers have won 2 Superbowls while you've been alive.")
elif birthyear >= 1979:
    print ("The Steelers have won 3 Superbowls while you've been alive.")
elif birthyear >= 1976:
    print ("The Steelers have won 4 Superbowls while you've been alive.")
elif birthyear >= 1975:
    print ("The Steelers have won 5 Superbowls while you've been alive.")
#president (since FDR)
if birthyear > 2008:
    print ("Barack Obama was president when you were born.")
elif birthyear > 2000:
    print ("George W. Bush was president when you were born.")
elif birthyear > 1992:
    print ("Bill Clinton was president when you were born.")
elif birthyear > 1988:
    print ("George Bush was president when you were born.")
elif birthyear > 1980:
    print ("Ronald Reagan was president when you were born.")
elif birthyear > 1973:
    print ("Gerald Ford was president when you were born.")
elif birthyear > 1968:
    print ("Richard Nixon was president when you were born.")
elif birthyear > 1962:
    print ("Lyndon B. Johnson was president when you were born.")
elif birthyear > 1960:
    print ("John F. Kennedy was president when you were born.")
elif birthyear > 1952:
    print ("Dwight D. Eisenhower was president when you were born.")
elif birthyear > 1944:
    print ("Harry S. Truman was president when you were born.")
elif birthyear > 1932:
    print ("Franklin D. Roosevelt was president when you were born.")
else:
    print ("Wow, you've seen some politics in your day!")
