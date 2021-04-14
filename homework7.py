# Homework 7 Python : Sets and Dictionary , The purpose of the program is to create a dictionary of music attributes and print them


# The dictionary where we store the attributes with thier Key 
Music_Dict = { "Artist" : "Abel Tesfaye", "StageName" : "The Weeknd",
"Genre" : "R&B" , "Album" : "After Hours", "Song" : "Blinding Lights",
"yearReleased" : "2019" , "DurationInMin" : "4", "DurationInSec" : "22", 
"Nominations" : "Song of the year" }

# Loop to print the attributes 
for info in Music_Dict :
    print(info ," : ", Music_Dict[info])


# A fuction that takes two parameters , A key and A guessed value from the user , returns True if the guessed value is correct 
# Returns False otherwise 
def guess_the_value(Key,Value) :
    if Value == Music_Dict[Key] :
        return True
    else :
        return False

Key = str(input("\nEnter the key at which you wish to guess the value : "))
Value = str(input("\nEnter the value : "))
print(guess_the_value(Key,Value))

