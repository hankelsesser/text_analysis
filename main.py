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
    songs.append(file1)
    songs.append(file2)
    songs.append(file3)
    songs.append(file4)
    names = ""
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
      freqs[letter]+=1 #add one to established entry
    else:
      freqs[letter]=1 #create new dictionary entry
  return freqs

def sort_freqs(freqs):
    letters = []
    for key in freqs:
        entry = []
        entry.append(freqs[key])#appends quantity first so that it can be sorted by it
        entry.append(key)
        letters.append(entry)
    return(sorted(letters, reverse = True))

def get_length_sucess_data(file, option):
    weeks = []
    lengths = []
    preference_index = 0 #index of the artist
    if option == "title": preference_index = 1 #index of the title
    for song in file:
        weeks.append(song[2])
        lengths.append(len(song[preference_index]))
    return(lengths, weeks)

def orginize_data(file1, file2, file3, file4, function, option):
    x1, y1 = function(file1, option)
    x2, y2 = function(file2, option)
    x3, y3 = function(file3, option)
    x4, y4 = function(file4, option)
    return(x1, y1, x2, y2, x3, y3, x4, y4)

def create_title_sucess_graph(file1, file2, file3, file4):
    x1, y1, x2, y2, x3, y3, x4, y4 = orginize_data(file1, file2, file3, file4, get_length_sucess_data, "title")
    plt.stem(x1, y1, linefmt = "blue", markerfmt='s', label='Songs from the 1980s')
    plt.stem(x2, y2, linefmt = "green", markerfmt='v',label='Songs from the 1990s')
    plt.stem(x3, y3, linefmt = "red", markerfmt='o',label='Songs from the 2000s')
    plt.stem(x4, y4, linefmt = "teal", markerfmt='D',label='Songs from the 2010s')
    plt.title("Popularity of Songs Verses the Lengths of Their Titles.")
    plt.xlabel("Characters in a Title")
    plt.ylabel("Weeks at #1")
    plt.legend()
    plt.show()

def create_artist_sucess_graph(file1, file2, file3, file4):
    x1, y1, x2, y2, x3, y3, x4, y4 = orginize_data(file1, file2, file3, file4, get_length_sucess_data, "artist")
    plt.stem(x1, y1, linefmt = "blue", markerfmt='s', label='Songs from the 1980s')
    plt.stem(x2, y2, linefmt = "green", markerfmt='v',label='Songs from the 1990s')
    plt.stem(x3, y3, linefmt = "red", markerfmt='o',label='Songs from the 2000s')
    plt.stem(x4, y4, linefmt = "teal", markerfmt='D',label='Songs from the 2010s')
    plt.title("Popularity of Songs Verses the Lengths of Their Artist's Name.")
    plt.xlabel("Characters in Artist's Name")
    plt.ylabel("Weeks at #1")
    plt.legend()
    plt.show()

def main():
    songs1980 = get_info("songs1980.txt")
    songs1990 = get_info("songs1990.txt")
    songs2000 = get_info("songs2000.txt")
    songs2010 = get_info("songs2010.txt")
    frequent_letters_artist = sort_freqs(get_freqs(clean_string(get_names(songs1980, songs1990, songs2000, songs2010, "artist"))))
    frequent_letters_title = sort_freqs(get_freqs(clean_string(get_names(songs1980, songs1990, songs2000, songs2010, "title"))))
    print("most common letters in popular artist's names:",frequent_letters_artist[:5])
    print("most common letters in popular song titles:",frequent_letters_title[:5])
    create_artist_sucess_graph(songs1980, songs1990, songs2000, songs2010)
    #create_title_sucess_graph(songs1980, songs1990, songs2000, songs2010)
main()


#commit!
