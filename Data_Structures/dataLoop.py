#CHAPTER 4
# Looping througn an entire list

magnicians = ['alice', 'david', 'carolina']
for magnician in magnicians:
    print(magnician)

    #Doing many works within a for loop
print(f"{magnician.title()}, that was realy great effort!")

#Adding second line to our message

magnicians = ['alice', 'david', 'carolina']
for magnician in magnicians:
    print(f"{magnician.title()}, that was realy great effort!")

    print(f"I can't wait you up to that, {magnician.title()}.\n")
    print("Thank you every one. That was a great magic shows!") #doing something after for loop : Python 
#  finds at least one indented line after the for statement

#indenting unneccessary
# if you indent a line that doesn't need to be indented, python informs you about the unexpected indent
message = "Hello python"
    # print(message) #Unexpected error


magnicians = ['alice', 'david', 'carolina']
for magnician in magnicians:
    print(f"{magnician.title()}, that was realy great effort!")
    print(f"I can't wait you up to that, {magnician.title()}.\n")
    
    print("Thank you every one. That was a great magic shows!") #Indenting unnessecary after loop

#forgeting colon
# The colon at the end of a for statement tells Python to interpret the next 
# line as the start of a loop.
# when we forget this we get syntax error

#As a Exerice

# 4-1.  Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a f or loop to print the name of each pizza.

My_Pizza = ['egg', 'creame', 'pepperoni']
#     Modify your for loop to print a sentence using the name of the pizza 
# instead of printing just the name of the pizza. For each pizza you should 
# have one line of output containing a simple statement like I like pepperoni 
# pizza.

My_Pizza = ['egg', 'creame', 'pepperoni']
for pizzas in My_Pizza:
    print(f"I like {pizzas.title()} pizza.\n")

# Add a line at the end of your program, outside the for loop, that states 
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence, such as 
# I really love pizza!
print(f"How much would you like pizza? \n")
print(f"I like pasta pizza!")
print(f"I like tomatoe pizza!")
print(f"I like fruit pizza!")
print(f"I realy love pizza!\n")

#4-2.  Animals: Think of at least three different animals that have a common char-acteristic. 
    # Store the names of these animals in a list, 
    #and then use a  for loop to print out the name of each animal.
Animals = ['cow', 'ox', 'sheap']
for animal in Animals:
    print(f"I'm {animal.title()}. I can live with human being!")

    # Modify your program to print a statement about each animal, such as 
    # A dog would make a great pet.
    print(f"{animal.title()} will make great pet.\n")

    #   Add a line at the end of your program stating what these animals have in 
    # common. You could print a sentence such as  Any of these animals would 
    # make a great pet!
print(f"What this animal have in common?")
print(f"Any of these animals would make a great pet!")

#Making numerical list
    # In data visualizations, you’ll 
    # almost always work with sets of numbers, such as temperatures, distances, 
    # population sizes, or latitude and longitude values, among other types of 
    # numerical sets.

#Using the range() functions

for value in range(1, 6):
    print(value)

#Using range() to make a list of numbers
number = list(range(1, 5)) 
print(number)

#How to list even numbers:
even_number = list(range(2, 11, 2)) 
print(even_number)

#How list odd numbers:
odd_number = list(range(1, 11, 2))  #range(1,11) == range(1, 11, 1)
print(odd_number)

#We can also use square
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#To write this code more concisely
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#Simple Statistics with a List of Numbers
lists = [2, 9, 5, 1, 0]
list = max(lists)
list_m = min(lists)
print(f"The max of the list is {list} and the minimum is {list_m}")

#List Comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

#As exercise
        # 4-3.  Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for number in range(1, 20):
    print(number)

    # 4-4. One Million: Make a list of the numbers from one to one million, and then use a f or
    # loop to print the numbers. (If the output is taking too long, stop it by 
# for numbers in range(1, 1_000_000):
#     print(numbers)
#     Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and 
# ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
# check this
# listing = list(range(1, 1000000))
# minima = min(listing)
# print(minima)

    # 4-6.  Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers 
    # from 1 to 20. Use a f or loop to print each number.
# number = list(range(1, 20, 2))
# print(number)

#     Threes: Make a list of the multiples of 3 from 3 to 30. 
# Use a  for loop to print the numbers in your list.
multiple = [value**3 for value in range(3,30)]
print(multiple)

# the above code and this is also the same but different in structure form
multiple = []
for value in range(3,30):
    multiples = value**3
    multiple.append(multiples)
print(multiple)

    #     4-8.  Cubes: A number raised to the third power is called a  cube. For example, 
    # the cube of 2 is written as  2**3 in Python. Make a list of the frst 10 cubes (that is, 
    # the cube of each integer from 1 through 10), 
    # and use a  for loop to print out the value of each cube.

cubes = []
for value in range(1, 10):
    cube = value**3
    cubes.append(cube)
print(cubes) #1, 8, 27, 64, ...

    #   Cube Comprehension: Use a list comprehension to generate a list of the frst 10 cubes.
cubes = [value**3 for value in range(1, 10)]  #has form of cube comprehenstion
print(cubes)

#SLICING A LIST
# you specify  the index of the first and last element you want to work with
name = ['jon', 'tom', 'doe', 'wako', 'abdi']
print(name[0:4])
# print out from the second item to the end
print(name[1:])

print(name[-3:])

# Looping through slice
print("here are the first three players name in my team:")
for value in name[:3]:
    print(value.title())

#Copying a list
My_Foods = ['egg', 'bayant', 'shiro', 'firfir']
my_friend_foods = My_Foods[:]  #we are copying all of My_Foods() item and holding for my_friend_foods

print('My favorite foods are:')
print(My_Foods)

print("\nHere are my friends favorite foods:")
print(my_friend_foods)

My_Foods.append("meet")
my_friend_foods.append("cabbage")

print("My favorite foods are:")
print(My_Foods)

print("\nMy friend favorite foods are:")
print(my_friend_foods)

#As exercise 
        #4-10. Slices: Using one of the programs you wrote in this chapter, add several 
        # lines to the end of the program that do the following:
#         Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
Students = ['chala', 'Wako', 'Kena', 'Sifen']
print(Students[:3])

#          Print the message Three items from the middle of the list are:. Use a slice to 
# print three items from the middle of the list.
print(Students[1:])

#             Print the message The last three items in the list are:. Use a slice to print the 
# last three items in the list
print(Students[2:])