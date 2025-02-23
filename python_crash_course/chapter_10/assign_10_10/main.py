file_name = "/Users/adrianrich/Documents/python/python_crash_course/chapter_10/assign_10_10/desert_moon.txt"

print("\n")

with open(file_name, 'r') as file_object:
    word = file_object.read()
    num_words = word.count('the')
    print(num_words)
    
    
print("\n")
   
   
with open(file_name, 'r') as file_object:
    word = file_object.read()
    num_words = word.count('the ')
    print(num_words)

print("\n")

with open(file_name, 'r') as file_object:
    word = file_object.read()
    num_words = word.lower().count('the')
    print(num_words)
    
    
print("\n")
   
   
with open(file_name, 'r') as file_object:
    word = file_object.read()
    num_words = word.lower().count('the ')
    print(num_words)

print("\n")

