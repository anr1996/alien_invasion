def build_profile(first, last, **user_info):
    
    user_info['first name'] = first
    user_info['last name'] = last
    print("\n")
    for info, person in user_info.items():
        print(f"{info}: {person}")
    print("\n")
        

build_profile('adrian', 'rich', location = 'Oregon')