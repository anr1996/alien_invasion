
""" f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close() """
""" 
f = open("sample.txt", "w")
integer = 10
f.write(str(integer))
f.close() """

filename = "project(alien invasion)/high_score.txt"
with open(filename, "w") as file_object:
    integer = 10
    file_object.write(str(integer))
    file_object.close()
