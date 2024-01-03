#Any type of cariables can be put in the lists. Python is going to be fine with it.
friends = ['Rolf', 'Bob', 'Jen', 'Anne', 'Jim', 'Joe']
lucky_numbers = [4, 8, 15, 16, 23, 42]
print(friends)
print(friends[2:5])

#list functions
friends.append('Swathi')  #appending another item in the end of the kist
print(friends)
#insert function that takes two parameters, first is index and name of the element
friends.insert(13, 'Karthik')
print(friends)
friends.remove('Jim')
print(friends)
print(friends.index('Swathi'))  #To check if a certain eleent is in the list
print(friends.count(
    'Swathi'))  #Will tell us how many times the element is in the list
friends.sort()  #To sort the list in asccending order
print(friends)
friends.reverse()  #To reverse the list
print(friends)

friends.extend(lucky_numbers) #adding 2 lists together
print(friends) 
friends2 = friends.copy() #Friends2 has all the attributes of the friends list.
print(friends2)



friends.pop()  # To get rid of the last element in the array.
print(friends)
friends.clear() #To get rid of everything in the list
print(friends) 