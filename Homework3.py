# Writing a function that takes in 3 parameters and checks for equality between two or more parameters 
# Returns true for that case and false otherwise
def comparison(integer , integer1 , integer2):
    if int(integer) == int(integer1) or int(integer) == int(integer2) :
        return True
    elif int(integer1) == int(integer) or int(integer) == int(integer2):
        return True
    elif int(integer2) == int(integer1) or int(integer2) == int(integer):
        return True
    else:
        return False


num1, num2, num3 = 4 , '4', 3
print(comparison(num1,num2,num3))
num4, num5, num6 = 5, 5 ,6
print(comparison(num4,num5,num6))
num7, num8, num9 = 7, 8, 9
print(comparison(num7,num8,num9))

