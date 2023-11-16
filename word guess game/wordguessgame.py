import random
words = ["tiger","lion","giraffee","cow","bear","fox","banana"] #storing various words
selectWord=(random.choice(words))   #selecting random word
actualWord=list(selectWord)     #typecasting word into list
allGuessedLetters=[]        #initialising empty list
flag=6      #initialising flag
empty=list("_"*len(actualWord)) #empty list to store user entered correct value
while flag>0:
    print("Guess the word:",','.join(empty))
    if len(allGuessedLetters)!=0: 
        print("Guessed letters:",",".join(allGuessedLetters))
    print(f"Guesses remaining:{flag}")
    guessedLetter=input("Enter a letter: ").lower()
    if guessedLetter.isalpha() and len(guessedLetter)==1 and guessedLetter.isspace()==False:    #validation
        if guessedLetter not in allGuessedLetters:
            allGuessedLetters.append(guessedLetter)
            if guessedLetter in actualWord:         #checking user entered value whether it is in actual word
                print("Correct!")
                for count,value in enumerate(actualWord):   #getting the index of the user entered letter in actual word
                    if value==guessedLetter:            
                        empty[count]=value          #storing the value in empty list
            else:
                print("incorrect")
                flag-=1
                   #removing list brackets        
        else:
             print("you already guessed that letter")
        if empty==actualWord:       #checking whether user entered all the letters of actual word
            print("Congratulations,you guessed the word!")
            break
    else:
        print("please enter only a single alphabet letter")

else:
    print("sorry,you ran out of guesses.the word was",selectWord)
