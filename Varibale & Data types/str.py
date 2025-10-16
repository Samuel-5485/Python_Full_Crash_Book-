#Stripping WhiteSpace

lang = " Python"
print(lang)

lang.rstrip()
print(lang)

#You can remove space from the left using: rstrip() or you can use strip() for the both side.
# for the left side:
progr = "Python is best  "
lang.rstrip() #to remove right
lang.lstrip() #to remove left
lang.strip() # ... both
print(progr)

#UnderScore in numbers
long_num = 32_456_788_123  #but python will not print '_'
print(long_num)

#Multiple assignment
x, y, z = 8, 8, 8
print(x)
print(y)
print(z)

#Constants
#when you want to treat your variable as a constant make it all in capital letter
MAX_FOLLOWER = 400

print(MAX_FOLLOWER)

#Zen of python
import this

# The Zen of python by tim peters
# Beutiful is better than ugly