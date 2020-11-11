def get_songs(file):
    songs = open(file).readlines()
    return(songs)
rawsongs = get_songs("songs2010.txt")

def get_info(string):
    songs = []
    for i in range(len(string)):
        song = ""
        firstq = string[i].find('"')
        #find author
        song += string[i][:firstq]
        song += "-"
        #find title
        song += string[i][firstq:(string[i].find('"', firstq+1))]
        song+="  "
        #find number of weeks
        song+= string[i][string[i].find('"', firstq+1):string[i].find("n")-1]

        songs.append(song)

print(get_info(rawsongs))
