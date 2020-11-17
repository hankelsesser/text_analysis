import matplotlib.pyplot as plt


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
    preference_index = 0 #index of the artist
    if option == "title": preference_index = 1 #changes to index of song title
    for document in range(4):
        for song in range(17):
            names += songs[document][song][preference_index]
    return(names)

def clean_string(string):
    string = string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    clean = ""
    for i in range(len(string)):
        if string[i] in alphabet:
            clean+=string[i]
    return(clean)

def get_freqs(string):
  freqs = {}
  for letter in string:
    if letter in freqs:
      freqs[letter]+=1
    else:
      freqs[letter]=1
  return freqs

def sort_freqs(freqs):
    letters = []
    for key in freqs:
        entry = []
        entry.append(freqs[key])
        entry.append(key)
        letters.append(entry)
    return(sorted(letters, reverse = True))

def get_length_sucess_data(file, option):
    weeks = []
    length = []
    preference_index = 0
    if option == "title": preference_index = 1
    for song in file:
        weeks.append(song[2])
        length.append(len(song[preference_index]))
    return(length, weeks)

def create_graph(x, y, x1, y1, x2, y2, x3, y3):
    #plt.plot('length of title', 'weeks at #1', data=dataset)
    plt.stem(x, y, linefmt = "blue", markerfmt='s')
    plt.stem(x1, y1, linefmt = "green", markerfmt='v')
    plt.stem(x2, y2, linefmt = "red", markerfmt='o')
    plt.stem(x3, y3, linefmt = "teal", markerfmt='D')
    plt.title("Popularity of Songs Verses the Lengths of Their Titles.")
    plt.xlabel("Characters in a Title")
    plt.ylabel("Weeks at #1")
    plt.legend((line1, line2, line3), ('label1', 'label2', 'label3'))
    plt.show()


def main():
    songs1980 = get_info("songs1980.txt")
    songs1990 = get_info("songs1990.txt")
    songs2000 = get_info("songs2000.txt")
    songs2010 = get_info("songs2010.txt")
    names = get_names(songs1980, songs1990, songs2000, songs2010, "artist")
    freqs = get_freqs(clean_string(names))
    x, y = get_length_sucess_data(songs1980, "title")
    x1, y1 = get_length_sucess_data(songs1990, "title")
    x2, y2 = get_length_sucess_data(songs2000, "title")
    x3, y3 = get_length_sucess_data(songs2010, "title")
    create_graph(x, y, x1, y1, x2, y2, x3, y3)
main()


#commit!
