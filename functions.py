# Python Homework 2

def Genre(string):  # Function that returns the genre 
    genreName = "R&B"
    return genreName



def Artist(string): # Function that returns the name of the artist 
    artistName = string
    return artistName


def Song(string): # Function that returns the name of the son
    songName = string
    return songName

def Year(number): # Function that returns the year the song was released 
    yearReleased = number 
    return yearReleased

def boolFunc(value): # A Boolean function that compares the year the song was released and the parameter 
    num = Year(year)
    if value == num:
        return True
    else:
        return False


# The following info regarding the artist 
genre = "R&B"
artist = "Abel tesfaye"
song = "Blinding Lights"
year = 2019

print(Genre(genre))
print(Artist(artist))
print(Song(song))
print(Year(year))

# using the bool function , to compare between the input year the song was released and the actual value
print("Enter a year : ")
value1 = int(input()) # input a year to be compared with the year the song was released  
print(boolFunc(value1)) # return True if value1 is equal to the year released , and false otherwise 







