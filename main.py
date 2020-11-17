def get_songs(file):
    songs = open(file).readlines()
    return(songs)
rawsongs = get_songs("songs2010.txt")

def get_info(string):
    songs = []
    # for i in range(len(songs)):
    #     songs[i] = songs[i].split()

    for i in range(len(string)):
        song = []
        firstq = string[i].find('"')
        secondq = string[i].find('"', firstq+1)
        #find author
        song.append(string[i][:firstq-1])
        #find title
        song.append(string[i][firstq+1:secondq])
        #find number of weeks
        #song.append(string[i][string[i].find('"', firstq+1)+1:string[i].find("n")])
        song.append(string[i][secondq:].replace("\n", ""))
        songs.append(song)

    return(songs)

print(get_info(rawsongs))

#commit!
