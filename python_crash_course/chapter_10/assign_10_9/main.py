filename = "/Users/adrianrich/Documents/python/python_crash_course/chapter_10/assign_10_9/dogs.txt"
filename_2 = "/Users/adrianrich/Documents/python/python_crash_course/chapter_10/assign_10_9/cats.txt"

try:

    with open(filename, 'r') as file_object:
        content = file_object.read()
        print(f"\n{content}")


except FileNotFoundError:
        pass


 
 
try:

    with open(filename_2, 'r') as file_object:
        content = file_object.read()
        print(content)

except FileNotFoundError:
        pass


        