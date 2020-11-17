
songs1980 = getsong("songs1980.txt")
songs1990 = getsong("songs1990.txt")
songs2000 = getsong("songs2000.txt")
songs2010 = getsong("songs2010.txt")

def get_song(file):
    songs = open(file).readlines()
    return(get_info(songs))

def get_info(string):
    songs = []
    for i in range(len(string)):
        song = []
        #location of first quotation mark
        firstq = string[i].find('"')
        #location of second quotation mark
        secondq = string[i].find('"', firstq+1)
        #find author
        song.append(string[i][:firstq-1])
        #find title
        song.append(string[i][firstq+1:secondq])
        #find number of weeks at #1
        song.append(string[i][secondq+2:-1])
        songs.append(song)
    return(songs)

print(songs1980[1])

#commit!
