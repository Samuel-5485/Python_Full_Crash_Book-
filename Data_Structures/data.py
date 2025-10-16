#LIST

lists = ["sami", "Abdi", "elias"]
print(lists)
print(lists[0]) #indext:refers positions
print(lists[0].title()) #refers make the first letter capitalize()
print(f"My first friend was {lists[-1].title()}") #f-string

#CHANGING, REMOVING & ADDING ELEMENTS

#MODIFYING ELEMENTS

#how to modify elements: what syntax we have to use?
 #1.CHANGING: we can change the value in a list.
motorcycle = ["honda", "Yamaha", "Susuki"]
print(motorcycle)
motorcycle[0] = "Speedx" #syntax we use to change
print(motorcycle)

#2.ADDING: the simplest way to add new item in a list:
#Appending elements to the end of a list.
motorcycle = ["honda", "Yamaha", "Susuki"]
motorcycle.append("ducati") #the way to add using in appending for.
print(motorcycle)

#do you know the other use of append():
#it can also add new item in an empty lists

#but many times why we use this because since we don't know what the useres are going to write.
my_list = []
my_list.append("CS")
my_list.append("IT")
my_list.append("IS")
print(my_list)

#Inserting elements into a list:
# we can add elements whatever place by using insert( ) method and also access it's index.

my_list.insert(0, "Programming") #by using insert(index, "value") method we can add an item into a list
print(my_list)

#REMOVING AN ITEM FROM A LIST
my_list.remove("IS")
print(my_list)

#REMOVING AN ITEM USING DEL STATEMENT
#if you know the position of item you want to remove you can use del statement

del my_list[0] #del statement 
print(my_list)

#REMOVING USING POP() STATEMENT
print(motorcycle)
# motorcycle.pop() #this pop removes the last item
My_Last_Bicyle = motorcycle.pop()
print(motorcycle)
print(f"The last motorcyle i bought was {My_Last_Bicyle.title()}")

#You can also use pop() for others by using within it is index
print(motorcycle)
My_First_Bicyle= motorcycle.pop(0)
print(f"For the first time, i bought this {My_First_Bicyle.title()} from Nework.")

#AS Exercise
#   Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting 
# them to dinner.
My_invite = ["My Dad", "My Mom", "My_Love"]
print(My_invite)

#   Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.

#       Start with your program from Exercise 3-4. Add a print() call at the end 
# of your program stating the name of the guest who can’t make it.
print(f"This is one of my guest can't come to my invite {My_invite.pop()}")

#         Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting.

My_invite.append("My Brother") #modifying
print(My_invite)

#         Print a second set of invitation messages, one for each person who is still 
# in your list.
print(f"Hello, Dear {My_invite[0]} welcome to my invitation!") 

#use insert()
My_invite.insert(0, "Teacher")
print(My_invite)
My_invite.append("Friend")
print(My_invite)

print(f"Oh!My God, now we all are here my {My_invite.pop()}.")

#Shrinking Guest List:
#         Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.

print(F"\nI invite only two people for dinner.")

#         Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner
print(My_invite)
print(f"I am very sorry for the cancelation of your invitation dear {My_invite.pop()} and My lovely {My_invite.pop(-1)}. ")
print(My_invite)

# Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
print(f"\nHey congratulation those who have accepted for my invitation!!!")
print(f"\tHello my best Python {My_invite[0]} and my lovely {My_invite[1]} you have accepted for my invitation nice!")

# Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.

print(My_invite)
del My_invite[0]
print(My_invite)
#The last within empty list.
del My_invite[0]
print(My_invite)

#ORGANIZATION OF LIST

#Sorting method: means ordering the list 
cars = ['bmd', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#We can also sort list in reverse 
cars.sort(reverse=True)  #Now we have permanently change that.
print(cars)

#Sorting a list temporary
mens = ['Chali', 'Tome', 'Sifan']
print('here is the original one.')
print(mens)
print(f"\nhere is the sorted list")
print(sorted(mens))

print(f"\nhere is the original list.")
print(mens)

#Printing a list in reverse order!
print(f"\nReversing the list:")
mens = ['Chali', 'Tome', 'Sifan'] #the end one goes to the first and vise versa
mens.reverse() #This reverse() method is permanenlty reverse the list but you can also revert again to back to original.
print(mens)
#FINDING LENGTH OF A LIST
print(f"\nHow to find length of the list:")
print(len(mens))

#As exercise

# Seeing the World: Think of at least five places in the world you’d like to 
# visit
        # A.Store the locations in a list. Make sure the list is not in alphabetical order.
print(f"\nExercise on what we have learned:")
World_Vist = ['Newyork', 'Canada', 'Dubai', 'German', 'California']
        # B.Print your list in its original order.
print(World_Vist)

        # C.Use sorted() to print your list in alphabetical order without modifying the 
            # actual list.
print(f"\tThis is the sorted list:")
print(sorted(World_Vist))

        # D.Show that your list is still in its original order by printing it.
print(f"\tDo you see original is here as it's.")
print(World_Vist)

        # E.Use sorted() to print your list in reverse alphabetical order without
           #  changing the order of the original list.
print(f"\tUse sorted to list in reverse alphabet:")
print(sorted(World_Vist))

        # Show that your list is still in its original order by printing it.
print(f"\tYou're still in original:")
print(World_Vist)

        # Use sorted() to print your list in reverse alphabetical order without changing 
           # the order of the original list.
print(f"\tUse sorted without without changing the order of the original.")
print(sorted(World_Vist))

        # Show that your list is still in its original order by printing it again
print(f"\tCheck it whether your list is in original for or not!")
print(World_Vist)

        #Use reverse() to change the order of your list. Print the list to show that its 
          # order has changed.
print(f"\tReverse method to change the order of your list.")
World_Vist.reverse()
print(World_Vist)

        #Use reverse() to change the order of your list again. Print the list to show 
            # it’s back to its original order.
print(f"\tCan you change it to the original order!")
World_Vist.reverse()
print(World_Vist)

        #Use sort() to change your list so it’s stored in alphabetical order. Print the 
            # list to show that its order has been changed.
print(f"\tKnow you have to order in alphabet using sort() method.")
World_Vist.sort()
print(World_Vist)

        #Use sort() to change your list so it’s stored in reverse alphabetical order. 
            # Print the list to show that its order has changed.
print(f"\tUse sort that change in reverse way:")
World_Vist.sort(reverse=True)
print(World_Vist)          
        # Identify the length of your list
print(f"\tThis is my list length:")
print(f"Hello i am a list and my length is {len(World_Vist)}.")

# Avoiding Index Errors When Working with Lists

# Self exercise
        # Intentional Error: If you haven’t received an index error in one of your 
# programs yet, try to make one happen. Change an index in one of your programs to produce an index error. 
# Make sure you correct the error before closing the program.

