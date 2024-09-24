""" def describe_pet(pet_name, animal_type='dog'): # def default value for each parameter
    """"Display information about a pet."""""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.") 
describe_pet(pet_name='willie') """



""" def describe_pet(pet_name, animal_type='dog'): # def default value for each parameter
    """"Display information about a pet."""""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.") 
describe_pet('willie') """


""" def describe_pet(pet_name, animal_type='dog'): # defining multiple parameters, assigning value 'dog' to parameter 'animal_dog'.
    """"Display information about a pet."""""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.") 
describe_pet(pet_name='harry', animal_type='hamster') # assigning new values to parameters.
 """

""" def describe_pet(pet_name, animal_type='dog'):

# A dog named Willie.
# all of the following print calls would work for this function.
    describe_pet('willie')
    describe_pet(pet_name='willie')

# A hamster named harry.
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry') """
    






""" 
def make_shirt(type_size='', text_type=''): # defining two parameters
    print(f"\nmy shirt size is {type_size} and i want my name {text_type} on the shirt")
make_shirt(type_size='large', text_type=('johnny')) # assigning two values to parameters using keyword arguments.



def make_shirt(type_size='', text_type=''): # defining two parameters
    print(f"\nmy shirt size is {type_size} and i want my name {text_type} on the shirt\n")
make_shirt('large', 'johnny') # assigning two values usings positional arguments.
 """


# 8-4 Large shirts:
""" def make_shirt(text_type, type_size='large'): # setting default value for parameter.
    print(f"\nI would like a {type_size} shirt that says {text_type}.\n") 
make_shirt(text_type="'I love Python'") # assigning value to parameter 'text_type'.
make_shirt(text_type="'I love Python'", type_size='medium')
make_shirt(text_type="'I Java!'", type_size='extra large')
 """


#8-5. Cities
""" def describe_city(person_name, country_locale='Ireland'): # defining multiple parameters, assigning one parameter a default value.
    print(f"\n{person_name.title()} is from {country_locale.title()}.\n")
describe_city(person_name='John')
describe_city(person_name='micheal')
describe_city(person_name='james')
describe_city(person_name='tim', country_locale='austraila') # assigning new value to parameter 'country_locale'
 """

 
 # Return Values.
""" def get_formatted_name(first_name, last_name): # defining parameters
    """"Return a full name, neatly formatted""""
    full_name = f"{first_name} {last_name}" # assigning multiple parameters to value 'full_name'.
    return full_name.title() # assigning return value to variable 'full_name'.

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
 """


# Making an Argument Optional
""" def get_formatted_name(first_name, last_name, middle_name=''):
    """"Return a full name neatly formatted""""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}" # assigning an optional argument 'middle_name'
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician) """



# Returning a dictionary
""" def build_person(first_name, last_name):
    """"Return a dictionary of information about a person.""""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician) """




""" def build_person(first_name, last_name, age=None):
    """"Return a dictionary of information about a person.""""
    person = {'first': first_name, 'last': last_name}
    if age:                 
        person['age'] = age 
        return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician) """





""" def famous_person(first_name, last_name, power=None): # assigning placeholder value 'None' for parameter power.
    person = {'first': first_name, 'last': last_name}
    if power:
        person['power'] = power 
        return person
original = famous_person('bruce', 'lee', power=100)
print(original) """


# Using a Function with a while loop.
""" def get_formatted_name(first_name, last_name):
    """"Return a full name, neatly formatted."""""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print(f"\nPlease tell me your name:")
    print("(enter q at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break # break statement to end forloop.

    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!") """
    


# 8-6
# City Names.
""" def get_location_info(city_origin, country_origin):

   """"Return location information""""
    person_location = f"{city_origin} {country_origin}"
    return person_location.title()

while True:
    print(f"\nPlease tell me where your are from:")
    print("(enter q at any time to quit)")
    locale_city = input("City: ")
    
    if locale_city == 'q':
        break

    locale_country = input("Country: ")

    location_info = get_location_info(locale_city, locale_country)
    print(f"your place of origin is {location_info.title()}.") """ 
  
 
 

# 8-7



""" def get_make_album(artist_name, album_title): # defining parameters
    artist_info = {'artist': artist_name, 'album': album_title} # creating dictionary
    return artist_info

while True:
    print(f"\nWhat kind of music do you like?:")
    print("(enter q at any time to quit)")
    artist_id = input("Artist name: ")

    if artist_id == 'q':
        break

    album_id = input("Album Title: ")

    make_album = get_make_album(artist_id, album_id)
    print(f"Saving {make_album} to your ipod.") 
 """


""" music_playlist = []
def get_make_album(artist_name, album_title):
    artist_info = {'artist': artist_name, 'album': album_title}
    return artist_info

playlist = get_make_album('micheal jackson', 'beatz')
print(playlist)

playlist = get_make_album('micheal jackson', 'jamz')
print(playlist)

playlist = get_make_album('micheal jackson', 'chill beatz')
print(playlist)  """


""" music_playlist = []
def get_make_album(artist_name, album_title, songs=None): # defining parameters
    artist_info = {'artist': artist_name, 'album': album_title} # assigning values to parameters.
    if songs: # if a value assigned to songs..
        artist_info['songs'] = songs # assign string to songs
    return artist_info # return variable artist_info
    
artist = get_make_album('micheal jackson', 'beatz', songs=30)
print(artist)
 """

# 8-8
# User Albums
""" music = [] # creating an empty list

def get_artist_info(artist_name, album_title):
    artist_info = f"{artist_name, album_title}"
    return artist_info

while True:
    print("\nWhat kind of music do you like?: ")
    print(f"type q to quit:")

    name_artist = input("Artist: ")
    if name_artist == 'q':
        break

    title_album = input("album: ")

    complete_info = get_artist_info(name_artist, title_album)
    print(f"\n{complete_info} saved to your music")
    music.append(complete_info)

print(music) """

# passing a list
""" def greet_users(names): # defining parameter and assigning it the variable 'names'.
    """"Print a simple greeting to each user in the list.""""
    for name in names: # for loop
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot'] # creating list with values representing names.
greet_users(usernames) # passing a list to a function. """


""" unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """"Simulate printing each design until none are left. Move to completed_models after printing.""""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """"Show all the models that were printed. """"
    print(f"\nThe following models have been printed: ")
    for completed_model in completed_models:
         print(completed_model)
 """

""" 
print_models(unprinted_designs ,completed_models)
show_completed_models(completed_models)
print_models(unprinted_designs[:], completed_models)
 """

# 8-9 Messages.

""" short_messages = ['Where there is a will there is a way', 'fear is just a mindset', 'mind over matter'] # creating list
def get_message(short_messages): # defining parameter for list 'short_messages'
    while True:                 # while loop.
        print(f"\nWould you like to hear some cool quotes? ")
        response = input(": ")
        if response == 'yes':
            for message in short_messages:
                print(message)
        else:
            print("Okay, have a nice day.")
            break
get_message(short_messages) """


# 8-10
# sending messages
""" 
send_messages = ['Where there is a will there is a way', 'fear is just a mindset', 'mind over matter'] # creating list
def get_message(send_messages, sent_messages): # defining parameter for list 'short_messages'
    while True:                 # while loop.
        print(f"\nWould you like to recieve my messages? ")
        response = input(": ")
        if response == 'yes':
            for message in send_messages:
                print(f"\n{message}")
        else:
            print(f"Okay, have a nice day.")
            break
    while send_messages:
        current_messages = send_messages.pop()
        print(f"Printing recent messages: {current_messages}")
        sent_messages.append(current_messages)

def show_recieved_messages(sent_messages):
    print(f"\nthe following messages have been recieved ")
    for sent_message in sent_messages:
        print(sent_message)

sent_messages = []
    
get_message(send_messages, sent_messages)
show_recieved_messages(sent_messages)
print(f"\nsent_messages") """


""" # 8-10
def get_message(send_messages, sent_messages): # defining parameter for list 'short_messages'
    while True:                 # while loop.
        print(f"\nWould you like to recieve my messages? ")
        response = input(": ")
        if response == 'yes':
            for message in send_messages:
                print(f"\n{message}")
        else:
            print(f"Okay, have a nice day.")
            break
    while send_messages:
        current_messages = send_messages.pop()
        print(f"Printing recent messages: {current_messages}")
        sent_messages.append(current_messages)

def show_recieved_messages(sent_messages):
    print(f"\nthe following messages have been recieved ")
    for sent_message in sent_messages:
        print(sent_message)

send_messages = ['Where there is a will there is a way', 'fear is just a mindset', 'mind over matter'] # creating list
sent_messages = []

get_message(send_messages[:], sent_messages)
show_recieved_messages(sent_messages)
print(f"\n{send_messages}")
print(f"\n{sent_messages}")
 """

# Passing an Arbitrary Number of Arguments
""" def make_pizza(*toppings): # defining function 'make_pizza' and creating tuple to store any values in.
    """"Print the list of toppings that have been requested.""""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

 """

""" def make_pizza(*toppings): # defining function 'make_pizza' and creating tuple to store any values in.
    """"Summarize the pizza we are about to make."""" 
    print(f"\Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
 """

# Mixing Positional and Arbitrary Arguments.
""" def make_pizza(size, *toppings): # passing multiple argument types, the arbitrary argument must be placed in the last parameter.
    """"Summarize the pizza we are about to make."""""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}") 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""


# Using Arbitrary Keyword Arguments
# pg 148




""" def build_profile(first, last, **user_info):
    """"Build a dictionary containing everything we know about a user.""""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)  """
""" 
def character_profile(name, origin, **user_info):
    """"building oblivion character""""
    user_info['user_name'] = name
    user_info['place_of_birth'] = origin
    return user_info
user_ready = character_profile('Sir Rich', 'Red Mountains', 
                                main_level = 10,
                                 strength = 15, 
                                 stamina = 10, 
                                 endurance = 7)
print(user_ready)  """
 
# 8-12. 

""" def sandwich_build(*sandwich_info):
    """"building sandwich""""
    print(f"\n sandwich made with the following: \n{sandwich_info}")

sandwich_build('salami')
sandwich_build('pepperoni', 'ham', 'provalone cheese')
sandwich_build('bacon', 'cheddar cheese') """

# 8-13.
# User Profile

""" def user_build(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_ready = user_build('Adrian', 'Rich', location = 'Keizer Oregon', age = 26, career = 'Programmer')
print(user_ready)
# too tired to add comments now, add more comments later to the code above for explanation . """


""" def make_car(car_type, model, **additional_info):
    additional_info['Type of car'] = car_type
    additional_info['Model of car'] = model
    return additional_info
car_ready = make_car('honda', 'civic', year = 1996, condition = 'brand new')
print(car_ready) """





    
    












