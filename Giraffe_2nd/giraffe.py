phrase = "Karthik Is Cool"

#To convert the phrase to lower and upper case
print(phrase.lower())
print(phrase.upper())

#To check if the phrase is in lower case or upper case
print(phrase.islower())
print(phrase.isupper())
#We get false for both the cases mentioned above

#Using upper() in conjunction with the isupper() function
print(phrase.upper().isupper())

#To check the length of the string
print(len(phrase))

#For grabbing a specific character from the string
print(phrase[2]) #In this case I am grabbing the 3rd char, that is index number 2

#To get the index number of a specific char in the string
print(phrase.index("Is"))

#Replacing something in the phraase
print(phrase.replace("Karthik", "Kaka"))