# Handling the FileNotFoundError Exception
filename = 'chapter 10/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    print(f'Sorry, the file "{filename}" does not exist.')