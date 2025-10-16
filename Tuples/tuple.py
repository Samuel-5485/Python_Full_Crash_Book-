# TUPLE
# python refers value that can't change as immutable, and an immutable list is calles tuple. 

        #Definition of tuple
        # tuple looks just list but it uses parentheses () instead of square bracket[] 
dimensions = (600, 60)
print(dimensions[0])

# can you assign new value
# dimensions[0] = 400
# print(dimensions) #TypeError: 'tuple' object does not support item assignment

#Loop all the values through a list

for values in dimensions[0:1]:
    print(values)

#Writing over a tuple
dimension = (300, 35)
print('Original dimension.')
for dimensions in dimension:
    print(dimensions)

dimension = (400, 43)
print('\nModifiyed dimension.')
for dimensions in dimension:
    print(dimensions)

#Comparation between list and tuple.
#tuple is the simple data structures and use them when you to store a set of values that
#shouldn't change through out the life of program

    #4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
#simple foods, and store them in a tuple.
buffet = ('Sun chips', 'anchote', 'chebchebsa', 'cororsa', 'marka')
print(buffet)
    #Use a for loop to print each food the restaurant offers.
for food in buffet:
    print(food)

        #The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.

    #4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/
# dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting 
# to skim through it.
    