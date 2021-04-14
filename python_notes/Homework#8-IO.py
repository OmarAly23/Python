#Python Homework 8 input/output 
#creating a note taking program 
import os

filename = input("Enter the name of the file you wish to open : ") # Input a filename 


if os.path.isfile("./" + filename) : # if the file exists in the current directory enter 
    temp = input("Choose an option : \n A) Read the file \n B) Delete the file and start over \n C) Append the file\n D) Replace a single line\n") # the user is then given three choices
    if temp == 'A' : # if the user chooses A , prompt the user to read the file 
        readFile = open(filename , 'r')
        if os.path.getsize(filename) == 0: # check if the file is empty 
            print("The file is empty")
        else :
            for line in readFile : # if the file is not empty, display the contents of the file
                print(line) 
            readFile.close()
            print("The file has been processed\n")
            
    elif temp == 'B' : # if the user chooses option B , prompt them to delete the file and start over 
        os.remove(filename) # a method that removes the file
        print("The file has been deleted") 
        print("A new empty file will be created")
        with open(filename, "w") as write_file: # # open the file again to start over 
            print("Enter your new notes : ")
            newText = input()
            write_file.write(newText + '\n')
            write_file.close()
        print("The file has been processed\n")

    elif temp == 'C' : # if the user chooses option C , prompt them to append the file 
        appendFile = open(filename, 'a')
        notes = input("Enter the notes you wish to append : ")
        appendFile.write(notes + '\n')
        appendFile.close()
        print("The file has been processed\n")
    elif temp == 'D' : # if the user chooses option D , prompt them to enter a line number and replace the line 
        line_num = int(input("Please enter the line number for the replacement: "))
        text = input("Please enter your note: ")
        with open(filename, "r") as read_file:
            lines = read_file.readlines()
        with open(filename, "w") as write_file:
            for index, line in enumerate(lines):
                # print(idx, line)
                if index == line_num - 1:
                    print("Line num {} will be replaced ".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)
    
else : # if the file does not exist, create a new file and prompt the user to input some text to be appended to the file
    print("The file ", filename , "will be created : ")
    writeFile = open(filename, 'w')
    line = input("Enter your lines of text : ")
    writeFile.write(line + '\n')
    writeFile.close()
    print("The file has been processed\n")
    

