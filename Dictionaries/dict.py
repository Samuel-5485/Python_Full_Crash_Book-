#UNIT 6:DICTIONARY

alien_game = {
    "name":"Snake",
    "phone":"Sumsung",
    "amount": 45
}
print(f"\nHey it's {alien_game['name']}")

#Adding New Key-Value Pairs
alien_game["x_position"] = 4
alien_game["y_position"] = 20 
print(f"the new one.{alien_game}")

#Starting with an Empty Dictionary
info = {}
info['name'] = 'John'
info['id'] = '3254'
info['works'] = 'student'
print(f"\nThese are our student information:")
print(info)

#Modifying Values in a Dictionary
colors = {
    'green':'for beuty',
    'red': 'for motivation',
    'amount':50
}
print(f"\nSome colors identinty {colors['green']}")
colors['green'] = 'nice' #here we are modifying value to nice.
print(f"\tcan you print out for me value of green? yes it's {colors['green']}")

alien_games = {
    'x_position': 0,
    'y_position': 20,
    'speed': 'medium'
}

if alien_games['speed'] == 'slow':
    x_increement = 1
elif alien_games['speed'] == 'medium':
    x_increement = 2
else:
    x_increement = 3

#The new position is the old position plus the x_increement value
alien_games['x_position'] = alien_games['x_position'] + x_increement
print(f"\nNew positions: {alien_games['x_position']}")

remove_method = {
    'programming': 'python',
    'level': 'experience two years',
    'salary': '$45'
}
del remove_method['salary']
print(f"\nI have deleted the salary from the list:\n{remove_method}")

#Using get() to access value
#without getting an error we use get() if the value the key-value is exist we get the value of that
#unless since we want to use get() without seeing the errors we see the message of the value!

    #If there’s a chance the key you’re asking for might not exist, consider 
    #using the get() method instead of the square bracket notation.
value = remove_method.get('salary', 'No salary assigned!')
print(value)

#As an Exercise 
    #6-1. Person: Use a dictionary to store information about a person you know. 
        # Store their first name, last name, age, and the city in which they live. You 
        # should have keys such as first_name, last_name, age, and city. Print each 
        # piece of information stored in your dictionary.
Person = {
    'first_name' : 'Abdi',
    'last_name' : 'Bulte',
    'age' : 23,
    'city' : 'nedjo'
}
print(f"the following are the information one person he is:\n{Person}")
print("Hey, friend thanks for your behavior you have!!!")


    #6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
        # Think of five names, and use them as keys in your dictionary. Think of a favorite 
        # number for each person, and store each as a value in your dictionary. Print 
        # each person’s name and their favorite number. For even more fun, poll a few 
        # friends and get some actual data for your program.
My_Favorite_numbers = {
    'Tohm' : 3,
    'John' : 12,
    'Doe' : 20,
    'Simon' : 35,
    'Jesica' : 15
}

print(f"\nHey friends what is your favorite numbers? \n{My_Favorite_numbers}")

#Looping through a dictionary
user_name = {
    'username' : 'fermento',
    'first' : 'enrico',
    'last' : 'fermi'
}
for key, value in user_name.items():
    print(f"\nKey, {key}")
    print(f"\tValue, {value}\n")

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rubby'
}
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}\n")

#Looping Through All the Keys in a Dictionary
for name in favorite_language.keys(): #key shows for only the key word not include value on it
    print(f"These are only for the key:\n{name.title()}\n")

friends = ['robica', 'philina']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you bye language {language}!")