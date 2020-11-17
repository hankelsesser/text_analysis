
songs1980 = getsong("songs1980.txt")
songs1990 = getsong("songs1990.txt")
songs2000 = getsong("songs2000.txt")
songs2010 = getsong("songs2010.txt")

def get_song(file):
    songs = open(file).readlines()
    return(get_info(songs))

def get_info(file):
    rawdocument = get_songs(file)
    songs = []
    for i in range(len(rawdocument)):
        song = []
        #location of first quotation mark
        firstq = rawdocument[i].find('"')
        #location of second quotation mark
        secondq = rawdocument[i].find('"', firstq+1)
        #find author
        song.append(rawdocument[i][:firstq-1])
        #find title
        song.append(rawdocument[i][firstq+1:secondq])
        #find number of weeks at #1
        song.append(rawdocument[i][secondq+2:-1])
        songs.append(song)
    return(songs)

print(songs1980[1])

#commit!
