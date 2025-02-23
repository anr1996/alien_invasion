def make_album(artist, album, songs = None):
    artist_info = {}
    artist_info[artist] = album
    
    if songs:
        artist_info['number of songs'] = songs
    
    return artist_info


divider = "-" * 70
print(divider)

while True:
    
    artist = ''
    album = ''
    
    response = input("Enter the name of the artist:\n")
    if response.lower() == 'quit':
        break
    else:
        artist = response
        
    response = input("Enter the name of the album:\n")
    if response.lower() == 'quit':
        break
    else:
        album = response
        
    musician_info = make_album(artist, album)
    print(f"\n{musician_info}")
        
    print(divider)
        
    
        