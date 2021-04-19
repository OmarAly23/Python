# Python program to check for phone number validity , HackerRank problem , regex section
import re

def ValidNum(string) :
    if not string.isdigit() :
        return False
    if len(string) != 10 :
        return False 
    elif len(string) == 10 :  
        if string.startswith('7') | string.startswith('8') | string.startswith('9') : 
            return True



if __name__ == "__main__" :
   N = int(input('Enter a value: '))
   while N > 0 :
        s = str(input('Enter a phone number: '))
        v=ValidNum(s)
        if v == True :
            print("YES")
        else :
            print("NO")
        N-=1








    





