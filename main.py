def get_songs(file):
    songs = open(file).readlines()
    return(songs)
rawsongs = get_songs("songs2010.txt")

def get_info(string):
    songs = []
    for i in range(len(string)):
        song = []
        firstq = string[i].find('"')
        #find author
        song.append(string[i][:firstq])
        #find title
        song.append(string[i][firstq:(string[i].find('"', firstq+1))])
        #find number of weeks
        song.append(string[i][string[i].find('"', firstq+1):string[i].find("n")-1])

        songs.append(song)
    return(songs)

print(get_info(rawsongs))
