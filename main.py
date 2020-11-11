def get_songs(file):
    songs = open(file).readlines()
    return(songs)
rawsongs = get_songs("songs2010.txt")

def get_info(string):
    songs = []
    for i in (len(string)):
        song = ""
        firstq = string[i].find('"')
        song += string[i][:firstq]
        song += "-"
        #find title
        song += string[i][firstq:(string[i].find('"', firstq+1)]
        song+="  "
        songs+= string[i][string[i].find('"', firstq+1):string[i].find("\n")]

        songs.append(song)

print(get_info(rawsongs))

#hi
def get_sentences(file):
  startP = 0
  sentences = []
  for i in range(len(file)):
    lastP = file.find(".", startP)
    nextP = file.find(".", lastP+1)
    startP = nextP+1
    sentences.append(file[lastP+1:nextP+1])
  return(sentences)
