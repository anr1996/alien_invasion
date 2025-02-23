forloops = ''
variables = ''
strings = ''
integers = ''
floats = ''

programming_words = {
    'Forloops' : forloops,
    'Variables' : variables,
    'Strings' : strings,
    'Integers' : integers,
    'Floats' : floats,
}

print("\n")

for define_word in programming_words:
    programming_words[define_word] = input(f"Enter the definiton of {define_word}:\n")
    
print("\n")
    
for definition in programming_words:
    print(f"{definition}:\n{programming_words[definition]}\n\n")