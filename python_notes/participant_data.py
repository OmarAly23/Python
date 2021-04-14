"""ParticipantNumber = 2
participantData = []
outputFile = open("Participant_Data.txt", "w")

registeredParticipants = 0
while(registeredParticipants < ParticipantNumber) :
    tempPartData = [] #name,country of origin , age
    name = input("Enter your name : ")
    tempPartData.append(name)
    country = input("Enter your country of origin : ")
    tempPartData.append(country)
    age = int(input("Enter your age : "))
    tempPartData.append(age)
    participantData.append(tempPartData)
    registeredParticipants+=1



for participant in participantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")

    outputFile.write("\n")


outputFile.close()

print("The file has been processed successfully.")
"""

inputFile = open("Participant_Data.txt", "r")

inputList = []

for line in inputFile:
    tempLine = line.strip("\n").split()
    inputList.append(tempLine)

print(inputList)

Age = {}
for data in inputList:
    tempAge = int(data[-1])
    if tempAge in Age:
        Age[tempAge]+=1
    else:
        Age[tempAge ]=1
print(Age)

Oldest = 0
Youngest = 1000
MostOccuringAge = 0
counter = 0
for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    elif tempAge<Youngest:
        Youngest = tempAge
    if Age[tempAge] > counter:
        counter = Age[tempAge]
        MostOccuringAge = tempAge


print("The Oldest age is : ", Oldest)
print("The Youngest age is : ", Youngest)
print("The most occuring age is :", MostOccuringAge, "with", counter, "occurances")



inputFile.close()