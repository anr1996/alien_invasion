
text_file = "/Users/adrianrich/Documents/python/"\
    "python_crash_course/chapter_10/assign_10_1/learning_python.txt"
print("\n")
with open(text_file) as file_object:
    contents = file_object.read()
print(contents)

with open(text_file) as file_object:
    for line in file_object:
        print(line.rstrip())
print("\n")

with open(text_file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n")
