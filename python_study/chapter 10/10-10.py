# Common Words

PDL = 'chapter 10/life_snippet.txt'
with open(PDL) as book:
    # Using count method to counter number of words in txt file.
    counts = PDL.count('a')

print(counts)