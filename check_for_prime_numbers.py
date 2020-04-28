## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here

for number in check_prime: #looping through the list of numbers
    for i in range(2, number): #initializing a counter that starts at 2 and loops until reach the value of the number in the list.  The step is 1.
        if number%i == 0: #Evaluating the condition to check if the number is prime.
            print("{} is NOT a prime number, because {} is a factor of {}".format(number,i,number))
            break
        if i == number-1: #i will continue growing until reach the value number-1.  Of course if the i reaches this value, that nmeans that 
            #doesn't have smaller factors.
            print("{} Is a primer number".format(number))
 

## HINT: You can use the modulo operator to find a factor