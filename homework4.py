# Homework 4 Python
myUniqueList = [] # A unique list
myLeftOvers = [] # an array of leftovers 


def addTolist(variable) : # A list that adds variables to a list , only if they are unique , otherwise it adds them to an array
    if variable in myUniqueList: # To check whether or not the variable is unique 
        myLeftOvers.append(variable) # if not , add it to an array
        return False

    else :
        myUniqueList.append(variable) # is unique , add it to the list
        return True


addTolist('This')
addTolist('Is')
addTolist('Homework4')
addTolist('Python')
addTolist(3)
addTolist(3)
addTolist('Homework4')
addTolist('Python')

print(myUniqueList)
print(myLeftOvers)