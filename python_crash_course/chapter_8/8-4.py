slogans = [
    "Just Do It",
    "Keep Calm and Carry On",
    "I'm With Stupid →",
    "Love",
    "Peace",
    "Classic",
    "Vintage",
    "Game Over",
    "Believe",
    "Fight Like a Girl",
]

sizes = [
    "Small (S)",
    "Medium (M)",
    "Large (L)",
    "Extra Large (XL)",
    "Double Extra Large (XXL)",
    "Triple Extra Large (XXXL)",
]

divider = "-" * 70
print(divider)
def t_shirt(size = "Large (L)", text = "I love Python"):
    print(f"\nT-shirt size:\n{size}\n")
    print(f"T-shirt slogan:\n{text}\n")
    print(divider)
    

t_shirt()
t_shirt(size = sizes[1])

t_shirt(size = sizes[3], text = slogans[0])


