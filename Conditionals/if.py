#CHAPTER 5: IF Statement
#Simple Statement
Cars = ['nme', 'ytr', 'uyu', 'fdg']
for Car in Cars:
    if Car == 'uyu':
        print(Car.upper())
    else:
        print(Car.title())

#Ignoring case when checking for equality
Car = 'AUDI'
Car.lower() == 'audi'

#Checking for the inequality
your_choise = 'Dinner'
if your_choise != 'dinner':
    print('What happen?')

#Numerical comparations
age = 23
if age != 32:
    print('You have not the same age bro!')

#Checking Whether a Value Is in a List
name = ['Sena', 'Sifo', 'Sami']
user = 'Chali'
if user not in name:
    print(f"{user.title()}, try to give response is good!")

# if user in name:
#     print(f"{user.title()}, already you have presented for us.")

#Boolean Exepression
#is value is defined as true of false

age_1 = 12
age_2 = 13
My_age = (age_1 <= age_2) and (age_2 >= age_1)
print(My_age)

#SIMPLE IF STATEMENTS
age = 20
if age >= 18:
    print('You are older!')

#IF ELSE STATEMENT
age = 43
if age >= 44:
    print("You can participate in the party!")

else:
    print("Hey, sorry we skiped your invitation for now!")

#IF-ELIF-ELSE STATEMENTS

Class = 50
if Class >= 54:
    print("We have to separate this class!")
elif Class <=50:
    print("We need to add students in the class!")
else:
    print("It's good to focus why the class lost students!!!")

#Using Multiple elif Blocks


age = 13
if age < 4:
    price = 1
elif age > 15:
    price = 5
elif age >=40: #the 1st we have used elif for multiple block
    price = 43
elif age < 40:#the 2nd we have used elif for multiple block
    price = 65
else: 
    price = 15
print(f"Your Admision cost is ${price}")

#Omitting the else block
# python doesn't require an else block at the end of an elif-chain.

#Testing multiple conditions
#You have to know this code doesn't work for if-else-elif because it check the first and stop 
# running for others
requested_topping = ['pizza', 'juice']
if 'pizza' in requested_topping:
    print('Adding pizza')
if 'juice' in requested_topping:
    print('Adding juice')
if 'milk' in requested_topping:
    print('Adding milk')
print(f"\nAlready i have finished your order. Thanks!")

#In summary if you want only one code you use the if-else-block otherwise use only 
# if independent statement!

# As exercise
        # 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
        # variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color = 'green'
        # Write an if statement to test whether the alien’s color is green. If it is, print 
        # a message that the player just earned 5 points.

#         Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)
if alien_color == 'red':
    print('\nYou have earned 5 points.')
if alien_color == 'green':
    print('\nYou have earned 5 points')
if alien_color == 'yellow':
    print('\nYou have just earned 5 points.')
print(f"\nCongrats, your have a big chance {alien_color}!")


# If the alien’s color is green, print a statement that the player just earned 
# 5 points for shooting the alien.

alien_color = 'green'
if alien_color == 'red':
    print('You have just earned 10 points for shooting the alien.')
else:
    print('You have earned 5 points for shooting the alien.')
print(f'\nNice you were have best marks {alien_color} colors')

        # 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You have earned 10 points.')
else:
    print('You have earned 15 points.')
print(f"\nYou have just got the point thank you for the game!{alien_color}")

        # 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
        # stage of life. Set a value for the variable age, and then:
age = 20
if age <=2:
    print('You are baby.')
elif age >= 2 and age <= 4:
    print('You are toddler.')
elif age >=3 and age <= 13:
    print('You are a kid.')
elif age >= 13 and age <= 20:
    print('You are leenager')
elif age >=20 and age <= 65:
    print('You are an adult.')
elif age >=65:
    print('You are an elder.')
print(f"\tHey, you are correctly determined your age.So you are {age} years old.")


        # 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
        # independent if statements that check for certain fruits in your list.
favorite_fruits = ['apple', 'avocado', 'banana']
        # Write five if statements. Each should check whether a certain kind of fruit 
        # is in your list. If the fruit is in your list, the if block should print a statement, 
        # such as You really like bananas!
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'pinapple' in favorite_fruits:
    print('You really like pinapple!')
if 'avocado' in favorite_fruits:
    print('You really like avocado!')
print(f"\nWhat an amazing choice, you're really loved it!")
