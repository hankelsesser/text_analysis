def get_song(file):
    songs = open(file).readlines()
    return(songs)

def get_info(file):
    rawdocument = get_song(file)
    songs = []
    for i in range(len(rawdocument)):
        song = []
        firstq = rawdocument[i].find('"') #location of first quotation mark
        secondq = rawdocument[i].find('"', firstq+1) #location of second quotation mark
        song.append(rawdocument[i][:firstq-1]) #find author
        song.append(rawdocument[i][firstq+1:secondq]) #find title
        song.append(rawdocument[i][secondq+2:-1]) #find number of weeks at #1
        songs.append(song) #append song to list of songs
    return(songs)

def get_names(file1, file2, file3, file4, option):
    songs = []
    names = ""
    songs.append(file1)
    songs.append(file2)
    songs.append(file3)
    songs.append(file4)
    preference_index = 0
    if option == "song": preference_index = 1
    for document in range(4):
        for song in range(17):
            names += songs[document][song][preference_index]
    return(names)



def main():
    songs1980 = get_info("songs1980.txt")
    songs1990 = get_info("songs1990.txt")
    songs2000 = get_info("songs2000.txt")
    songs2010 = get_info("songs2010.txt")
    print(get_names(songs1980, songs1990, songs2000, songs2010, "artist"))
main()


#commit!
