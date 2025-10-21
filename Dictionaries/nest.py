#NESTING
alien_0 ={
    "name": "chala",
    "age": 23
    }
alien_1 = {
    "skill":"python",
    "experience": 3
}
aliens = [alien_0, alien_1]
for alien in aliens:
    print(alien)

#make an empty list for storing aliens
aliens = []

#make 30 green alien
for alien_number in range(20):
    new_alien = {
        "color": "red",
        "points": "6",
        "speed": "slow"
    } 
    aliens.append(new_alien)
#we can modify our given dictionary values through this 
#also by pointing to from what index your output will print
#So, as we see from the following for loop the values of each key change from [:4] means 0 -> 4
#and the rest of it as it is (original.)
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'fast'
#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


#A List in a Dictionary
#Rather than putting a dictionary inside a list, it’s sometimes useful to put 
#a list inside a dictionary.

#store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'topping':['mushrooms', 'extra cheese']
}

#summarize the order
print(f"You ordered a {pizza['crust']} -crust pizza. With the following toppings:")

for toppings in pizza['topping']:
    print("\t" + toppings)
#when we create dictionary we can nest list inside of it eg;our value should be in a list and 
#can contains many items.

favorite_languages = {
    'jen': ['python', 'rubby'],
    'sarah': ['c'],
    'edward': ['rubby', 'go']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.title()}")

#Dictionary in Dictionary
#inside of dictionary you can create another dictionary but your code become complicated.

users = {
    'john':{
        'first': 'doe',
        'last': 'jackson',
        'location': 'california'
    },
    'tedex':{
        'first': 'tohm',
        'last': 'simon',
        'location': 'senegal'
    },
}
for username, user_info in users.items():
    print(f"\nUserName: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullName: {fullname.title()}")
    print(f"\tLocation: {location.title()}")