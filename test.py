from lib.song import Song

song1 = Song("Pull Up", "Skeng", "Dancehall")
song2 = Song("Mad Bad", "Skeng", "Dancehall")
song3 = Song("Duppy", "Skeng", "Dancehall")

print(Song.count)           # 3
print(Song.artists)         # ["Skeng"]
print(Song.genres)          # ["Dancehall"]
print(Song.genre_count)     # {"Dancehall": 3}
print(Song.artists_count)   # {"Skeng": 3}