import lyricsgenius

genius = lyricsgenius.Genius("GENIUS_API_KEY")
genius.excluded_terms = [
    "(Remix)", "(Live)", "Remix", " - Live", "Demo", "Cover",
    "Mashup", "Version", "clean", "Acoustic", "Rework"
    ]
artist = genius.search_artist("Dua Lipa", max_songs=50, allow_name_change=True)

for song in artist.songs:
    song_file = open(f'dua_lipa/{song.title}.txt', 'w')
    song_file.write(song.lyrics)
    song_file.close()
