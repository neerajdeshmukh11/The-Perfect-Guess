import random
randNumber=random.randint(1,100)
guesses=0
userguess=None
while(userguess!=randNumber):
    userguess=int(input("Enter yor Guess: "))
    guesses+=1
    if(userguess==randNumber):
        print("Bravo!! You guessed it right")   
    else:
        if(randNumber>userguess):
            print("oops!! You guessed it wrong, enter a larger guess")
        else:    
            print("oops!! You guessed it wrong, enter a smaller guess")
print(f"You took total {guesses} chances to guess the number")
