


""" #What does this piece of code print ?
h = 0xAB
print(h)
 """


""" Question 16:
What does the given code print as output ?  """



""" What is the output of this code snippet: """


""" print("Good", "Morning", "Programmers", sep=None)
"""  """


# Which of the following statements are correct? 
# A) print(bool(0)) return False 
print(bool(0))

# B) print(bool("73.4")) returns True 
print(bool(73.4))

# C) print(bool("")) returns False
print(bool(""))

# D) print(bool({})) returns False 
print(bool({}))

# E) print(bool(-1)) returns True
print(bool(-1)) """

""" 
radius = int(input())
print(radius) """


""" # What does this piece of code print?
b = 0b111
print(b)
# answer: 7 """


""" msg = 'Betty\'s "Bitter" Butter'
print(msg) """


""" 
o = 0o310
print(o)
# answer: 200
 """

""" 
# What does the following code snippet print?
str = ""A multiline string,
with more than one line""
print(str)
 
 """

""" # What is the output of the following code snippet?
num1 = 0b10111
num2 = 0b10011
print(bin(num1 ^ num2))
# answer: ob100
 """

""" 
Given x and y as two binary numbers, what would the AND (&) operator on these numbers will yield.
Note, the bin() function will produce a binary number from decimal """


""" x = 0b10101
y = 0b11010
print(bin(x & y))
# answer = ob10000 """


""" s = "ABCDEF"
print(s[::2]) """

""" def func(num):
    return_value = False
 
    if num %5 == 0:
        True
 
    return return_value
 
x = func(10)
print(x)
 """

""" 
# What would be the output of the following code:
x = 1
y = 4
 
z = x ** y ** x
 
print(z)
print(f"\n")

 """



"""  #What would be the expected output when you execute this code:
p, q, r, s = [], "", 0, -1
 
print(bool(p), bool(q),bool(r), bool(s)) """


""" # What do you expect to get printed below:
my_values = True, 4 ,"Earth"
print(list(my_values)) """

""" #Question 40:
#What is the output of the following code:
cards = ["Hearts", "Clubs", "Spades", "Diamonds"]
print(len(cards)) """


""" # What do you expect when the following code is executed?
str1 = "Python"
str2 = "pYtHoN"
print(str1 == str2.capitalize())
 """

""" # What would you expect the following code to printout:
lst1 = ["Earth"]
lst2 = ["Earth"]
 
print(id(lst1) is not id(lst2)) """


# What is the expected output when the following code is executed?
""" s = "Piper"
 
print(s[::-1]) """


""" #Question 50:
#What would you expect the following code to printout: """
#lst1 = ["Apples", True,6]
#lst2 = ["Apples", 2 < 3, 6]
#print(lst1 is lst2)
#print(lst1 == lst2) """
  



#Question 1:
#What is the output for the code below ?

""" a=3
b=2
c=5
if a < b:
    if a < c:
        print(a)
elif b < a:
    if b < c:
        print(b)
elif c < a:
    if c < b:
        print(c)
else:
    print('none') """


#What is the output for the given code snippet ?
i=1
while i<=2:
  j=1
  while j<=2:
        print(i,"*",j,'=',i*j)
        j+=1
  i+=1