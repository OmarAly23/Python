
Vacation_Spots = ["London", "Paris", "New York", "Iceland", "Australia"]


File = open("data2", "w")

for spots in Vacation_Spots :
    File.write(spots + "\n")


print("The File has been processed.")

File.close()

File = open("data2", "r")

for line in File:
    print(line, end="")

File.close()

FinalSpot = "Thailand"

File = open("data2", "a")
File.write(FinalSpot)
File.close()