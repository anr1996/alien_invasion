def make_album(artist, album, songs = None):
    artist_info = {}
    artist_info[artist] = album
    
    if songs:
        artist_info['number of songs'] = songs
    
    return artist_info

musician_1 = make_album('michael jackson', 'thriller',9)
musician_2 = make_album('madonna', 'like a virgin',10)
musician_3 = make_album('prince', 'purple rain',)

print(f"\n{musician_1}\n")
print(f"\n{musician_2}\n")
print(f"\n{musician_3}\n")


