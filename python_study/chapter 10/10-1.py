# Learning Python:

""" filename = 'chapter 10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_string = ''
for line in lines:
    learning_string += line 

print(3*learning_string)
 """



""" filename = 'chapter 10/learning_python.txt'

with open('chapter 10/learning_python.txt') as file_object:
    contents = file_object.read()
print(3*contents)
 """





""" with open('chapter 10/learning_python.txt') as file_object:
    contents = file_object.read()

learning_string = ''
for content in contents:
    learning_string += content 
print(contents) 
    
     """


filename = 'chapter 10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_string = ''
for line in lines:
    learning_string += line 

print(learning_string)
# using replace method to replace Python with C.
print(learning_string.replace('Python', 'C'))

