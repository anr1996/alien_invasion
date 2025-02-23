# glossary 2

print("\n")

programming_words = {}

while True:
    
    key = ''
    value = ''
    
    key = input(f"\nEnter the programming word:\n\n")
    if key.lower() == 'exit':
        break
    
    value = input(f"\nEnter the definiton:\n\n")
    if value.lower() == 'exit':
        break
    programming_words[key] = value


print("\n")
for word in programming_words:
    print(f"{word.title()}:\n{programming_words[word]}\n\n")
    

