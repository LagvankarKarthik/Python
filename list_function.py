friends = ["Shrinidhi", "Bharath", "Alvin", "Akash", "Varun"]
lucky_numbers = [5, 6, 8, 13, 20, 27]

print(friends)
print(lucky_numbers)

# Concatenating 2 lists
friends.extend(lucky_numbers)
print(friends)
# for removing the friends that came from the lucky number list
friends = [friend for friend in friends if friend not in lucky_numbers]
print(friends)

# Adding new element at the end of the list
friends.append("Vivek")
print(friends)
# Insert function
friends.insert(5, "Vighnesh")
print(friends)
friends.remove("Vighnesh")
print(friends)
'''# Removing all the elements from the list
friends.clear()
print(friends)'''
# removing the last element from the list
friends.pop()
print(friends)

# To get the index position of an element
print(friends.index("Varun"))

# Checking if an element exists in the list
if friends.count("Akas") > 0:
   print("yes")
else:
   print("No")

# Counting the number of elements in the list
print(friends.count("Shrinidhi"))

friends.sort()
print(friends)
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends)

