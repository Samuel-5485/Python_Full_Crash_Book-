#How the input functions works!
message = input("Tell me, then i will back it for you!")

name = input("\nEnter Your Name:")
print(f"\tHello, {name}")

prompt = "If you tell who are you, we can personalize the message you see."
prompt += "\nWhat is your name?"
name = input(prompt)
print(f"Hello, {name}")

height = input("\nHow tall are you in inches? ")
height = int(height)

if height >= 21:
    print("you're enough to ride.")
else:
    print("you will ride when you grow.")
print(f"your age is {height}!")


#The modulo operator
modulo = input("determine numbers whether it is even of odd? ")
modulo = int(modulo)

if modulo % 2 == 0:
    print("Hey, that's even.")
else:
    print("no matter it's odd.")
print(f"And here it's you entered {modulo}.")

#Introducing while Loops