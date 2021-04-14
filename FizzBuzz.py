#Python Homework 5

def isPrime(n) : # isPrime is a function that returns true if a number is prime and false otherwise 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True



for num in range(2,100):
    if num%3==0 and num%5==0: # if a number is divisible by both 3 and 5 print fizzbuzz
        print("fizzbuzz")
    elif num%3==0: # if a number is only divisible by 3 print fizz
        print("fizz")
    elif num%5==0: # if a number is only divisible by 5 print buzz
        print("buzz")
    elif  (isPrime(num) == True): # if a number is prime print prime
        print("prime")
    elif num%3!=0 and num%5!=0 and isPrime(num)==False : # if a number has none of the above characteristics print the number itself
        print(num)
    
    
