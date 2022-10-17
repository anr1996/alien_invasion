def character_build(name, class_build, **additional_info):
    additional_info['user name'] = name
    additional_info['character class'] = class_build
    return additional_info



character_info = character_build( 'Adrian', 'Warrior', origin = 'Red mountains', power_lvl = 30, magic_lvl = 50)
print(character_info)