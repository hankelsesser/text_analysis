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

def get_names(file, option):
    names = ""
    preference_index = 0 #index of the artist
    if option == "title": preference_index = 1 #changes to index of song title
    for song in range(17):
        names += file[song][preference_index]
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

def get_freqs_data(file, option):
    letters = []
    weeks = []
    string = clean_string(get_names(file, option))
    freqs = get_freqs(string)
    combined_data = sort_freqs(freqs)
    for i in range(len(combined_data)):
        letters.append(str(combined_data[i][1]))
        weeks.append(int(combined_data[i][0]))
    return letters, weeks

def get_data(freqs,option):
  sorted_dict = sorted(freqs.items(),key = lambda x:x[1],reverse=True)
  x = [v[0] for v in sorted_dict[:number]]
  y = [v[1] for v in sorted_dict[:number]]
  return x,y



def get_length_sucess_data(file, option):
    weeks = []
    length = []
    preference_index = 0
    if option == "title": preference_index = 1
    for song in file:
        weeks.append(song[2])
        length.append(len(song[preference_index]))
    return(numbers, weeks)


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

def create_popular_letters_graph(dict1, dict2, dict3, dict4):
    x1, y1, x2, y2, x3, y3, x4, y4 = orginize_data(file1, file2, file3, file4, get_data, "title")
    x1 = ["a", "b", "c", "d"]
    y1 = [6, 7, 9, 8]
    plt.barh(x1, y1)
    plt.bar(x2, y2, color = "green", label='Songs from the 1990s')
    plt.bar(x3, y3, color = "red", label='Songs from the 2000s')
    plt.bar(x4, y4, color = "teal", label='Songs from the 2010s')
    plt.legend()
    plt.show()

def main():
    songs1980 = get_info("songs1980.txt")
    songs1990 = get_info("songs1990.txt")
    songs2000 = get_info("songs2000.txt")
    songs2010 = get_info("songs2010.txt")
    #names = get_names(songs1980, songs1990, songs2000, songs2010, "artist")
    #freqs = get_freqs(clean_string(names))
    #create_title_sucess_graph(songs1980, songs1990, songs2000, songs2010)
    create_popular_letters_graph(get_freqs(songs1980), get_freqs(songs1990), get_freqs(songs2000), get_freqs(songs2010))
main()


#commit!
