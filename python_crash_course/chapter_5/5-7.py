# Favorite fruit

import sys

favorite_fruit = ['mango', 'strawberry', 'blackberry']

fruits = [
    "Acai", "Apple", "Apricot", "Avocado", "Banana", "Blackberry", 
    "Blackcurrant", "Blueberry", "Boysenberry", "Breadfruit", 
    "Cantaloupe", "Carambola", "Cherimoya", "Cherry", "Clementine", 
    "Coconut", "Cranberry", "Date", "Dragonfruit", "Durian", 
    "Elderberry", "Feijoa", "Fig", "Goji berry", "Gooseberry", 
    "Grape", "Grapefruit", "Guava", "Honeydew", "Huckleberry", 
    "Jabuticaba", "Jackfruit", "Jambul", "Jujube", "Juniper berry", 
    "Kiwano (horned melon)", "Kiwi", "Kumquat", "Lemon", "Lime", 
    "Longan", "Loquat", "Lychee", "Mandarin", "Mango", "Mangosteen", 
    "Marionberry", "Melon", "Miracle fruit", "Mulberry", "Nectarine", 
    "Orange", "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", 
    "Physalis", "Pineapple", "Pitaya (Dragon fruit)", "Plantain", "Plum", 
    "Pomegranate", "Pomelo", "Prune (Dried plum)", "Quince", "Rambutan", 
    "Raspberry", "Redcurrant", "Salak", "Satsuma", "Soursop", 
    "Star apple", "Star fruit", "Strawberry", "Tamarillo", "Tamarind", 
    "Tangerine", "Tomato", "Ugli fruit", "Watermelon", "White currant", 
    "White sapote", "Yuzu", "Zucchini (Courgette)"
]

vegetables = [
    "Artichoke", "Arugula", "Asparagus", "Aubergine (Eggplant)", "Amaranth", 
    "Legumes", "Alfalfa sprouts", "Azuki beans (or adzuki)", "Bean sprouts", 
    "Black beans", "Black-eyed peas", "Borlotti bean", "Broad beans", 
    "Chickpeas", "Green beans", "Kidney beans", "Lentils", "Lima beans", 
    "Mung beans", "Navy beans", "Pinto beans", "Runner beans", "Split peas", 
    "Soy beans", "Peas", "Mangetout (Snap peas)", "Beet greens", "Bok choy", 
    "Broccoli", "Brussels sprouts", "Cabbage", "Calabrese", "Carrots", 
    "Cauliflower", "Celery", "Chard", "Collard greens", "Corn salad", 
    "Endive", "Fiddleheads", "Frisee", "Fennel", "Greens", "Beet greens", 
    "Dandelion greens", "Kale", "Mustard greens", "Spinach", "Herbs and spices", 
    "Anise", "Basil", "Caraway", "Cilantro", "Coriander", "Chamomile", 
    "Dill", "Fennel", "Lavender", "Lemon Grass", "Marjoram", "Oregano", 
    "Parsley", "Rosemary", "Sage", "Thyme", "Lettuce", "Arugula", 
    "Mushrooms (technically not a vegetable, but often used as one)", 
    "Nettles", "New Zealand spinach", "Okra", "Onions", "Chives", "Garlic", 
    "Leek", "Onion", "Shallots", "Spring onion (Scallion)", "Parsley", 
    "Peppers", "Bell pepper", "Chili pepper", "Jalapeño", "Habanero", 
    "Paprika", "Tabasco pepper", "Cayenne pepper", "Radish", "Rhubarb", 
    "Root vegetables", "Beetroot", "Carrot", "Celeriac", "Daikon", 
    "Ginger", "Parsnip", "Rutabaga", "Turnip", "Radish", "Sweet potato", 
    "Taro", "Yam", "Wasabi", "Horseradish", "White radish (Daikon)", 
    "Squash", "Acorn squash", "Butternut squash", "Banana squash", 
    "Courgette (Zucchini)", "Cucumber", "Delicata", "Gem squash", 
    "Hubbard squash", "Marrow", "Patty pans", "Pumpkin", "Spaghetti squash", 
    "Tomato (technically a fruit, but used as a vegetable)", "Tubers", 
    "Jicama", "Jerusalem artichoke", "Potato", "Sunchokes", "Sweet potatoes", 
    "Taro", "Water chestnut", "Watercress"
]

meats = [
    "Beef", "Pork", "Chicken", "Turkey", "Lamb", "Mutton", 
    "Duck", "Goose", "Quail", "Pheasant", "Rabbit", "Venison", 
    "Buffalo", "Elk", "Moose", "Caribou", "Antelope", "Kangaroo", 
    "Ostrich", "Emu", "Rattlesnake", "Alligator", "Crocodile", 
    "Guinea fowl", "Partridge", "Grouse", "Boar", "Hare", 
    "Squab (young pigeon)", "Goat", "Horse", "Camel", "Yak", 
    "Veal (young beef)", "Bison", "Zebra", "Frog legs", 
    "Wild boar", "Bear", "Reindeer", "Squirrel", "Snail (Escargot)", 
    "Shark", "Whale", "Seal", "Walrus", "Dog (in certain cultures)", 
    "Cat (in certain cultures)", "Bat (in certain cultures)"
]

dairy_products = [
    "Milk", "Butter", "Cream", "Sour cream", "Whipped cream", 
    "Ice cream", "Yogurt", "Greek yogurt", "Skim milk", "Whole milk", 
    "Condensed milk", "Evaporated milk", "Powdered milk", "Buttermilk", 
    "Cheese", "Cheddar", "Mozzarella", "Parmesan", "Gouda", "Swiss cheese", 
    "Blue cheese", "Brie", "Camembert", "Feta", "Goat cheese", 
    "Ricotta", "Cottage cheese", "Cream cheese", "Mascarpone", "Paneer", 
    "Quark", "Kefir", "Clotted cream", "Creme fraiche", "Manchego", 
    "Provolone", "Gorgonzola", "Stilton", "Edam", "Emmental", 
    "Halloumi", "Havarti", "Monterey Jack", "Neufchatel", "Pecorino", 
    "Colby", "Colby-Jack", "Muenster", "Asiago", "Limburger", 
    "Vacherin", "Reblochon", "Taleggio", "Scamorza", "Fontina"
]





while True:
    response = input("\nEnter the fruit you would like to search" +
                     " for in your list of favorite fruits.\n\n")
    
    fav_fruit_found = False
    fruits_found = False
    veggies_found = False
    meats_found = False
    dairy_found = False
    
    for fruit in favorite_fruit:
        if response.lower() == fruit.lower():
            fav_fruit_found = True
            break
    

    for fruit in fruits:
        if response.lower() == fruit.lower():
            fruits_found = True
            break
        
    for veggies in vegetables:
        if response.lower() == veggies.lower():
            veggies_found = True
            break
    
    for meat in meats:
        if response.lower() == meat.lower():
            meats_found = True
            break
    
    for dairy in dairy_products:
        if response.lower() == dairy.lower():
            dairy_found = True
            break
    
    if fav_fruit_found == True:
        print(f"\nI found the fruit {response.title()} in your list of favorite fruits.")
        
    elif fruits_found == True:
        print(f"\n{response.title()} is a fruit, however, it is not in your list of fruits!")
    
    elif veggies_found == True:
        print(f"\n{response.title()} is a vegetable not a fruit.")
        
    elif meats_found == True:
        print(f"\n{response.title()} is a type of animal meat, not a fruit.")
    
    elif dairy_found == True:
        print(f"\n{response.title()} is a type of a dairy product not a fruit.")
    
    elif response.lower() == 'exit':
        sys.exit()
    
    else:
        print(f"\nI dont know what {response.title()} is but it certainly isn't in your list of" 
              + " favorite fruits!")
        
        
    
    
    