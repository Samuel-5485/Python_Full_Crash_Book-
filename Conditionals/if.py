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